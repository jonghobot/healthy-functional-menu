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
P3=[
('호흡·등','엎드려 등 뒤로 호흡하기','5호흡 × 2','허리보다 옆구리와 등 뒤가 넓어진다'),
('호흡·갈비뼈','옆으로 누워 옆구리 호흡하기','좌우 5호흡','위쪽 갈비뼈로 숨을 보낸다'),
('옆구리 가동성','아기 자세에서 손 옆으로 걷기','좌우 20~30초 × 2',None),
('흉추 회전','네발 자세에서 팔 겨드랑이로 넣기','좌우 5~8회',None),
('흉추 회전','네발 자세에서 한 팔 천장으로 열기','좌우 5~8회','눈으로 손을 따라간다'),
('흉추 펴기','폼롤러에 등 대고 가슴 열기','5~8회','허리보다 등 위쪽에서 움직인다'),
('옆구리 가동성','벽 짚고 옆구리 늘리기','좌우 20~30초 × 2',None),
('흉추 회전','의자에 앉아 가슴 돌리기','좌우 5~8회','골반은 정면을 유지한다'),
('척추 분절','벽에 기대 등 말아 내려가기','5~8회','목부터 한마디씩 천천히 말아준다'),
('골반·척추','누워서 척추 말아 엉덩이 들기','5~8회','허리를 한 번에 들지 않는다'),
('몸통 조절','네발 자세에서 몸 앞뒤로 흔들기','8~10회','허리 모양을 유지한다')]
P4=[
('고관절 회전','엎드려 발 좌우로 벌리기','좌우 왕복 5~8회',None),
('엉덩이 가동성','누워서 4자 스트레칭','좌우 20~30초 × 2',None),
('고관절 안쪽','누워서 한쪽 다리 옆으로 열기','좌우 6~10회','골반이 따라 돌아가지 않게 한다'),
('고관절 안쪽','개구리 자세에서 엉덩이 뒤로 빼기','6~10회',None),
('고관절 안정','누워서 무릎 바깥으로 밀고 버티기','10~20초 × 2','움직이지 않을 만큼만 힘을 준다'),
('고관절 안정','옆으로 누워 무릎 벌리고 버티기','좌우 10~20초 × 2','골반을 뒤로 넘기지 않는다'),
('고관절 조절','의자 잡고 고관절 원 그리기','좌우 방향별 3~5회','작고 부드러운 원으로 시작한다'),
('엉덩이 가동성','누워서 한쪽 무릎 가슴으로 당기기','좌우 20~30초 × 2',None),
('무릎 펴기','뒤꿈치 받치고 무릎 편하게 펴기','30~60초 × 2','무릎 뒤를 억지로 누르지 않는다'),
('무릎 조절','수건 누르며 허벅지 힘주기','5초 × 8회','무릎 아래 수건을 가볍게 누른다'),
('무릎 가동성','의자에서 무릎 천천히 펴고 굽기','좌우 6~10회',None)]
P5=[
('발가락 조절','엄지와 나머지 발가락 따로 들기','각 5~8회','발바닥을 바닥에 편안히 둔다'),
('발목 조절','앉아서 발목 원 그리기','좌우 방향별 5회','발가락보다 발목에서 움직인다'),
('발목 조절','발뒤꿈치와 발가락 번갈아 들기','8~12회',None),
('종아리 가동성','벽 짚고 종아리 늘리기','좌우 20~30초 × 2','뒤쪽 무릎을 편다'),
('발목 가동성','무릎 굽혀 종아리 아래쪽 늘리기','좌우 20~30초 × 2','뒤꿈치를 바닥에 둔다'),
('균형','발을 일자로 두고 서기','좌우 앞발 20~30초 × 2','필요하면 벽 가까이 선다'),
('균형·협응','벽 짚고 발로 시계 그리기','좌우 방향별 3회','지지하는 발의 아치를 유지한다'),
('균형','쿠션 위에 두 발로 서기','20~30초 × 2','안전을 위해 벽 가까이 선다'),
('발목 안정','밴드를 바깥으로 밀고 버티기','좌우 10~20초 × 2','무릎은 움직이지 않는다'),
('정강이·발목','벽에 기대 발등 들어올리기','8~12회 × 1~2','뒤꿈치는 바닥에 둔다'),
('체중 이동','벽 짚고 체중 좌우로 옮기기','좌우 왕복 8~10회','상체를 기울이지 않는다')]
P6=[
('어깨 가동성','벽에 기대 팔 위아래로 움직이기','6~10회','허리를 과하게 띄우지 않는다'),
('견갑 조절','벽 짚고 날개뼈 시계 그리기','방향별 5회','팔보다 날개뼈를 작게 움직인다'),
('견갑 조절','폼롤러 밀며 팔 위로 올리기','6~10회','어깨를 으쓱하지 않는다'),
('가슴·어깨','문틀 짚고 가슴 앞쪽 늘리기','좌우 20~30초 × 2',None),
('어깨 뒤쪽','팔을 가슴 앞으로 당겨 늘리기','좌우 20~30초 × 2',None),
('어깨 조절','팔 크게 원 그리기','좌우 방향별 3~5회','통증 없는 범위에서 천천히'),
('손목 가동성','손바닥 위로 두고 손목 늘리기','좌우 20초 × 2',None),
('손목 가동성','손등 위로 두고 손목 늘리기','좌우 20초 × 2',None),
('신경 가동성','팔과 손목 부드럽게 신경 움직이기','좌우 5~8회','저림이 생기기 전 범위까지만'),
('목 가동성','의자에 앉아 목 좌우로 돌리기','좌우 5~8회','턱 높이를 유지한다'),
('목·견갑','고개 겨드랑이 쪽으로 숙여 늘리기','좌우 15~20초 × 2','손으로 세게 당기지 않는다')]

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
        if prefix=='p3' and i in (6,9): draw.rectangle((0,0,part.width*.09,part.height),fill='white')
        if prefix=='p6' and i==6: draw.rectangle((part.width*.91,0,part.width,part.height),fill='white')
        part.save(ICONS/f'{prefix}_{i+1:02}.png',quality=95)

for page_no in range(1,7):
    crop_sheet(ROOT/f'page{page_no}_sprites.png',f'p{page_no}')

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
    txt(c,W-30,H-88,f'{page_no} / 6',7,MUTED,'PSemiBold','right')

    margin=30; gap=10; cols=4; rows=3; top=H-105; bottom=38
    cw=(W-2*margin-gap*3)/4; ch=(top-bottom-gap*2)/3
    for i,(tag,name,dose,cue) in enumerate(items):
        col=i%4; row=i//4; x=margin+col*(cw+gap); y=top-(row+1)*ch-row*gap
        c.setFillColor(CARD); c.setStrokeColor(LINE); c.setLineWidth(.7); c.roundRect(x,y,cw,ch,10,fill=1,stroke=1)
        # A slim colored rail makes the dense grid feel editorial rather than tabular.
        c.setFillColor(TEAL); c.roundRect(x,y,3.2,ch,1.6,fill=1,stroke=0)
        pill(c,x+14,y+ch-28,tag)
        txt(c,x+cw-14,y+ch-22,f'{i+1+(page_no-1)*11:02}',7.2,colors.HexColor('#A1AFB7'),'PSemiBold','right')
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
make_page(c,P2,2,'WHOLE BODY','척추 · 발과 발목 · 균형 · 견갑 · 회전 저항 · 힘줄 적응','p2'); c.showPage()
make_page(c,P3,3,'SPINE + RIBS','호흡 · 갈비뼈 · 흉추 회전 · 척추 분절과 몸통 조절','p3'); c.showPage()
make_page(c,P4,4,'HIP + KNEE','고관절 회전과 안정 · 엉덩이 가동성 · 무릎 조절','p4'); c.showPage()
make_page(c,P5,5,'FOOT + BALANCE','발가락 · 발목 · 종아리 · 균형과 체중 이동','p5'); c.showPage()
make_page(c,P6,6,'UPPER BODY','어깨 · 견갑 · 손목 · 목과 신경 가동성','p6'); c.showPage(); c.save()
print(OUT.resolve())
