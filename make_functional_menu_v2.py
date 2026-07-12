from pathlib import Path
from PIL import Image, ImageChops, ImageDraw
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT=Path('assets/functional_menu'); ICONS=ROOT/'icons'; ICONS.mkdir(exist_ok=True)
OUT=Path('output/pdf/functional_movement_menu.pdf'); OUT.parent.mkdir(parents=True,exist_ok=True)
for n in ('Regular','SemiBold','Bold'):
    pdfmetrics.registerFont(TTFont('P'+n,str(ROOT/f'Pretendard-{n}.ttf')))

W,H=landscape(A4)
BG=colors.HexColor('#F5F7F8'); CARD=colors.white; NAVY=colors.HexColor('#112E46')
TEAL=colors.HexColor('#03989E'); MINT=colors.HexColor('#E4F5F3'); INK=colors.HexColor('#172B3A')
MUTED=colors.HexColor('#70818D'); LINE=colors.HexColor('#E3E9EC'); CORAL=colors.HexColor('#D76755')

P1=[
('호흡·골반','벽에 다리 올리고 90-90 호흡','5호흡 × 1~2','숨을 길게 내쉬며 갈비뼈를 낮춘다'),
('골반 조절','누워서 골반 앞뒤로 굴리기','방향별 5회','골반을 작게 굴려 앞뒤 위치를 느낀다'),
('장좌 준비','벽에 기대 다리 펴고 앉기','20~30초 × 2','무릎을 굽혀도 골반부터 세운다'),
('장좌 준비','수건 받치고 다리 펴고 앉기','20~30초 × 2','엉덩이 아래 높이를 충분히 준다'),
('햄스트링','누워서 한쪽 무릎 펴기','좌우 6~10회','허벅지는 고정하고 무릎만 편다'),
('햄스트링','앉아서 뒤꿈치 바닥 누르기','10~20초 × 2','움직이지 않게 가볍게 누른다'),
('골반·몸통','엉덩이로 벽 터치하기','6~10회 × 1~2','허리가 아닌 엉덩이를 뒤로 보낸다'),
('고관절 앞쪽','반무릎 고관절 앞쪽 스트레칭','좌우 15~30초 × 2','허리를 꺾지 않고 골반을 작게 말아준다'),
('고관절 안쪽','한쪽 다리 벌리고 엉덩이 뒤로 빼기','좌우 6~10회',None),
('고관절 회전','앉아서 90-90 무릎 넘기기','좌우 왕복 5~8회',None),
('고관절 회전','누워서 무릎 좌우로 넘기기','좌우 왕복 5~8회',None)]
P2=[
('흉추 회전','옆으로 누워 가슴 열기','좌우 5~8회',None),
('척추 분절','캣카우','5~8회 × 1~2','마디별로 천천히 움직인다'),
('발목 가동성','뒤꿈치 붙이고 무릎 벽에 대기','좌우 6~10회','뒤꿈치를 바닥에 둔다'),
('발 기능','발가락 편 채 발 아치 만들기','5~10초 × 5',None),
('균형','벽 짚고 한 발로 서기','좌우 20~30초 × 2','벽은 넘어지지 않을 만큼만 짚는다'),
('견갑 조절','벽에서 팔 위로 미끄러뜨리기','6~10회 × 1~2',None),
('어깨 안정','밴드를 바깥으로 벌리고 버티기','10~20초 × 2','팔꿈치를 몸통 가까이 둔다'),
('목·상부척추','벽에 기대 턱 당기기','5~8회 · 각 3초',None),
('측면 안정','무릎으로 벽 밀고 버티기','좌우 10~20초 × 2',None),
('회전 저항','팔로프 프레스 버티기','좌우 10~20초 × 2','몸통이 밴드 쪽으로 돌지 않게 한다'),
('힘줄·발목','벽 짚고 까치발 버티기','15~30초 × 2','반동 없이 편안한 높이에서 멈춘다')]

def crop_sheet(sheet,prefix):
    im=Image.open(sheet).convert('RGB'); cw=im.width/4; ch=im.height/3
    for i in range(11):
        col=i%4; row=i//4
        inset=12
        box=(round(col*cw)+inset,round(row*ch)+inset,round((col+1)*cw)-inset,round((row+1)*ch)-inset)
        part=im.crop(box)
        bg=Image.new('RGB',part.size,'white'); diff=ImageChops.difference(part,bg).convert('L')
        # Ignore faint generation texture; retain illustration and teal/navy marks.
        mask=diff.point(lambda p: 255 if p>18 else 0); bbox=mask.getbbox()
        if bbox:
            l,t,r,b=bbox; pad=10; part=part.crop((max(0,l-pad),max(0,t-pad),min(part.width,r+pad),min(part.height,b+pad)))
        # Remove two tiny neighboring-cell fragments created by the generated sheet.
        draw=ImageDraw.Draw(part)
        if prefix=='p1' and i==9: draw.rectangle((0,0,part.width*.08,part.height),fill='white')
        if prefix=='p2' and i==5: draw.rectangle((0,part.height*.90,part.width,part.height),fill='white')
        part.save(ICONS/f'{prefix}_{i+1:02}.png',quality=95)

crop_sheet(ROOT/'page1_sprites.png','p1'); crop_sheet(ROOT/'page2_sprites.png','p2')

def txt(c,x,y,s,size=8,color=INK,font='PRegular',align='left'):
    c.setFont(font,size); c.setFillColor(color)
    getattr(c,{'left':'drawString','center':'drawCentredString','right':'drawRightString'}[align])(x,y,s)

def fit_image(c,path,x,y,w,h):
    im=Image.open(path); iw,ih=im.size; scale=min(w/iw,h/ih)
    dw,dh=iw*scale,ih*scale
    c.drawImage(ImageReader(im),x+(w-dw)/2,y+(h-dh)/2,dw,dh,mask='auto')

def pill(c,x,y,label):
    tw=pdfmetrics.stringWidth(label,'PSemiBold',6.5)+18
    c.setFillColor(MINT); c.roundRect(x,y,tw,16,8,fill=1,stroke=0)
    txt(c,x+tw/2,y+5.1,label,6.5,TEAL,'PSemiBold','center')

def make_page(c,items,page_no,kicker,focus,prefix):
    c.setFillColor(BG); c.rect(0,0,W,H,fill=1,stroke=0)
    txt(c,30,H-34,'FUNCTIONAL MOVEMENT MENU',7,TEAL,'PBold')
    txt(c,30,H-62,'저강도 기능 움직임',22,NAVY,'PBold')
    txt(c,30,H-82,focus,8.5,MUTED,'PRegular')
    c.setFillColor(TEAL); c.roundRect(W-121,H-71,91,33,16,fill=1,stroke=0)
    txt(c,W-75.5,H-59,kicker,7.2,colors.white,'PSemiBold','center')
    txt(c,W-30,H-88,f'{page_no} / 2',7,MUTED,'PSemiBold','right')

    margin=30; gap=10; cols=4; rows=3; top=H-105; bottom=38
    cw=(W-2*margin-gap*3)/4; ch=(top-bottom-gap*2)/3
    for i,(tag,name,dose,cue) in enumerate(items):
        col=i%4; row=i//4; x=margin+col*(cw+gap); y=top-(row+1)*ch-row*gap
        c.setFillColor(CARD); c.setStrokeColor(LINE); c.setLineWidth(.7); c.roundRect(x,y,cw,ch,10,fill=1,stroke=1)
        # A slim colored rail makes the dense grid feel editorial rather than tabular.
        c.setFillColor(TEAL); c.roundRect(x,y,3.2,ch,1.6,fill=1,stroke=0)
        pill(c,x+14,y+ch-28,tag)
        txt(c,x+cw-14,y+ch-22,f'{i+1+(11 if page_no==2 else 0):02}',7.2,colors.HexColor('#A1AFB7'),'PSemiBold','right')
        txt(c,x+14,y+ch-48,name,10.2,NAVY,'PSemiBold')
        c.setFillColor(colors.HexColor('#EDF3F7')); c.roundRect(x+14,y+ch-68,88,15,7.5,fill=1,stroke=0)
        txt(c,x+58,y+ch-63,dose,6.2,NAVY,'PSemiBold','center')
        fit_image(c,ICONS/f'{prefix}_{i+1:02}.png',x+10,y+25,cw-20,ch-96)
        if cue:
            c.setFillColor(colors.HexColor('#F1F6F6')); c.roundRect(x+12,y+8,cw-24,18,7,fill=1,stroke=0)
            txt(c,x+cw/2,y+13.4,cue,5.9,MUTED,'PRegular','center')
    txt(c,30,17,'편안한 당김까지만',7,TEAL,'PSemiBold')
    txt(c,110,17,'날카로운 통증 · 저림 · 힘 빠짐이 생기면 중단',7,CORAL,'PRegular')
    txt(c,W-30,17,'특정 골반 방향을 억지로 교정하지 않기',7,MUTED,'PRegular','right')

c=canvas.Canvas(str(OUT),pagesize=(W,H)); c.setTitle('저강도 기능 움직임 메뉴판')
make_page(c,P1,1,'PELVIS + HIP','골반을 세우는 감각부터 · 장좌 준비 · 햄스트링과 고관절','p1'); c.showPage()
make_page(c,P2,2,'WHOLE BODY','척추 · 발과 발목 · 균형 · 견갑 · 회전 저항 · 힘줄 적응','p2'); c.showPage(); c.save()
print(OUT.resolve())
