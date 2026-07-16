const movements = [
  {n:1,g:'pelvis',tag:'호흡·골반',name:'벽에 다리 올리고 90-90 호흡',dose:'5호흡 × 1~2',cue:'숨을 길게 내쉬며 갈비뼈를 낮춘다',img:'p1_01.png'},
  {n:2,g:'pelvis',tag:'골반 조절',name:'누워서 골반 앞뒤로 굴리기',dose:'방향별 5회',cue:'골반을 작게 굴려 앞뒤 위치를 느낀다',img:'p1_02.png'},
  {n:3,g:'pelvis',tag:'장좌 준비',name:'벽에 기대 다리 펴고 앉기',dose:'20~30초 × 2',cue:'무릎을 굽혀도 골반부터 세운다',img:'p1_03.png'},
  {n:4,g:'pelvis',tag:'장좌 준비',name:'수건 받치고 다리 펴고 앉기',dose:'20~30초 × 2',cue:'엉덩이 아래 높이를 충분히 준다',img:'p1_04.png'},
  {n:5,g:'pelvis',tag:'햄스트링',name:'누워서 한쪽 무릎 펴기',dose:'좌우 6~10회',cue:'허벅지는 고정하고 무릎만 편다',img:'p1_05.png'},
  {n:6,g:'pelvis',tag:'햄스트링',name:'앉아서 뒤꿈치 바닥 누르기',dose:'10~20초 × 2',cue:'움직이지 않게 가볍게 누른다',img:'p1_06.png'},
  {n:7,g:'pelvis',tag:'골반·몸통',name:'엉덩이로 벽 터치하기',dose:'6~10회 × 1~2',cue:'허리가 아닌 엉덩이를 뒤로 보낸다',img:'p1_07.png'},
  {n:8,g:'pelvis',tag:'고관절 앞쪽',name:'반무릎 고관절 앞쪽 스트레칭',dose:'좌우 15~30초 × 2',cue:'허리를 꺾지 않고 골반을 작게 말아준다',img:'p1_08.png'},
  {n:9,g:'pelvis',tag:'고관절 안쪽',name:'한쪽 다리 벌리고 엉덩이 뒤로 빼기',dose:'좌우 6~10회',img:'p1_09.png'},
  {n:10,g:'pelvis',tag:'고관절 회전',name:'앉아서 90-90 무릎 넘기기',dose:'좌우 왕복 5~8회',img:'p1_10.png'},
  {n:11,g:'pelvis',tag:'고관절 회전',name:'누워서 무릎 좌우로 넘기기',dose:'좌우 왕복 5~8회',img:'p1_11.png'},
  {n:12,g:'whole',tag:'흉추 회전',name:'옆으로 누워 가슴 열기',dose:'좌우 5~8회',img:'p2_01.png'},
  {n:13,g:'whole',tag:'척추 분절',name:'캣카우',dose:'5~8회 × 1~2',cue:'마디별로 천천히 움직인다',img:'p2_02.png'},
  {n:14,g:'whole',tag:'발목 가동성',name:'뒤꿈치 붙이고 무릎 벽에 대기',dose:'좌우 6~10회',cue:'뒤꿈치를 바닥에 둔다',img:'p2_03.png'},
  {n:15,g:'whole',tag:'발 기능',name:'발가락 편 채 발 아치 만들기',dose:'5~10초 × 5',img:'p2_04.png'},
  {n:16,g:'whole',tag:'균형',name:'벽 짚고 한 발로 서기',dose:'좌우 20~30초 × 2',cue:'벽은 넘어지지 않을 만큼만 짚는다',img:'p2_05.png'},
  {n:17,g:'whole',tag:'견갑 조절',name:'벽에서 팔 위로 미끄러뜨리기',dose:'6~10회 × 1~2',img:'p2_06.png'},
  {n:18,g:'whole',tag:'어깨 안정',name:'밴드를 바깥으로 벌리고 버티기',dose:'10~20초 × 2',cue:'팔꿈치를 몸통 가까이 둔다',img:'p2_07.png'},
  {n:19,g:'whole',tag:'목·상부척추',name:'벽에 기대 턱 당기기',dose:'5~8회 · 각 3초',img:'p2_08.png'},
  {n:20,g:'whole',tag:'측면 안정',name:'무릎으로 벽 밀고 버티기',dose:'좌우 10~20초 × 2',img:'p2_09.png'},
  {n:21,g:'whole',tag:'회전 저항',name:'팔로프 프레스 버티기',dose:'좌우 10~20초 × 2',cue:'몸통이 밴드 쪽으로 돌지 않게 한다',img:'p2_10.png'},
  {n:22,g:'whole',tag:'힘줄·발목',name:'벽 짚고 까치발 버티기',dose:'15~30초 × 2',cue:'반동 없이 편안한 높이에서 멈춘다',img:'p2_11.png'},
  {n:23,g:'spine',tag:'호흡·등',name:'엎드려 등 뒤로 호흡하기',dose:'5호흡 × 2',cue:'허리보다 옆구리와 등 뒤가 넓어진다',img:'p3_01.png'},
  {n:24,g:'spine',tag:'호흡·갈비뼈',name:'옆으로 누워 옆구리 호흡하기',dose:'좌우 5호흡',cue:'위쪽 갈비뼈로 숨을 보낸다',img:'p3_02.png'},
  {n:25,g:'spine',tag:'옆구리 가동성',name:'아기 자세에서 손 옆으로 걷기',dose:'좌우 20~30초 × 2',img:'p3_03.png'},
  {n:26,g:'spine',tag:'흉추 회전',name:'네발 자세에서 팔 겨드랑이로 넣기',dose:'좌우 5~8회',img:'p3_04.png'},
  {n:27,g:'spine',tag:'흉추 회전',name:'네발 자세에서 한 팔 천장으로 열기',dose:'좌우 5~8회',cue:'눈으로 손을 따라간다',img:'p3_05.png'},
  {n:28,g:'spine',tag:'흉추 펴기',name:'폼롤러에 등 대고 가슴 열기',dose:'5~8회',cue:'허리보다 등 위쪽에서 움직인다',img:'p3_06.png'},
  {n:29,g:'spine',tag:'옆구리 가동성',name:'벽 짚고 옆구리 늘리기',dose:'좌우 20~30초 × 2',img:'p3_07.png'},
  {n:30,g:'spine',tag:'흉추 회전',name:'의자에 앉아 가슴 돌리기',dose:'좌우 5~8회',cue:'골반은 정면을 유지한다',img:'p3_08.png'},
  {n:31,g:'spine',tag:'척추 분절',name:'벽에 기대 등 말아 내려가기',dose:'5~8회',cue:'목부터 한마디씩 천천히 말아준다',img:'p3_09.png'},
  {n:32,g:'spine',tag:'골반·척추',name:'누워서 척추 말아 엉덩이 들기',dose:'5~8회',cue:'허리를 한 번에 들지 않는다',img:'p3_10.png'},
  {n:33,g:'spine',tag:'몸통 조절',name:'네발 자세에서 몸 앞뒤로 흔들기',dose:'8~10회',cue:'허리 모양을 유지한다',img:'p3_11.png'},
  {n:34,g:'hipknee',tag:'고관절 회전',name:'엎드려 발 좌우로 벌리기',dose:'좌우 왕복 5~8회',img:'p4_01.png'},
  {n:35,g:'hipknee',tag:'엉덩이 가동성',name:'누워서 4자 스트레칭',dose:'좌우 20~30초 × 2',img:'p4_02.png'},
  {n:36,g:'hipknee',tag:'고관절 안쪽',name:'누워서 한쪽 다리 옆으로 열기',dose:'좌우 6~10회',cue:'골반이 따라 돌아가지 않게 한다',img:'p4_03.png'},
  {n:37,g:'hipknee',tag:'고관절 안쪽',name:'개구리 자세에서 엉덩이 뒤로 빼기',dose:'6~10회',img:'p4_04.png'},
  {n:38,g:'hipknee',tag:'고관절 안정',name:'누워서 무릎 바깥으로 밀고 버티기',dose:'10~20초 × 2',cue:'움직이지 않을 만큼만 힘을 준다',img:'p4_05.png'},
  {n:39,g:'hipknee',tag:'고관절 안정',name:'옆으로 누워 무릎 벌리고 버티기',dose:'좌우 10~20초 × 2',cue:'골반을 뒤로 넘기지 않는다',img:'p4_06.png'},
  {n:40,g:'hipknee',tag:'고관절 조절',name:'의자 잡고 고관절 원 그리기',dose:'좌우 방향별 3~5회',cue:'작고 부드러운 원으로 시작한다',img:'p4_07.png'},
  {n:41,g:'hipknee',tag:'엉덩이 가동성',name:'누워서 한쪽 무릎 가슴으로 당기기',dose:'좌우 20~30초 × 2',img:'p4_08.png'},
  {n:42,g:'hipknee',tag:'무릎 펴기',name:'뒤꿈치 받치고 무릎 편하게 펴기',dose:'30~60초 × 2',cue:'무릎 뒤를 억지로 누르지 않는다',img:'p4_09.png'},
  {n:43,g:'hipknee',tag:'무릎 조절',name:'수건 누르며 허벅지 힘주기',dose:'5초 × 8회',cue:'무릎 아래 수건을 가볍게 누른다',img:'p4_10.png'},
  {n:44,g:'hipknee',tag:'무릎 가동성',name:'의자에서 무릎 천천히 펴고 굽기',dose:'좌우 6~10회',img:'p4_11.png'},
  {n:45,g:'foot',tag:'발가락 조절',name:'엄지와 나머지 발가락 따로 들기',dose:'각 5~8회',cue:'발바닥을 바닥에 편안히 둔다',img:'p5_01.png'},
  {n:46,g:'foot',tag:'발목 조절',name:'앉아서 발목 원 그리기',dose:'좌우 방향별 5회',cue:'발가락보다 발목에서 움직인다',img:'p5_02.png'},
  {n:47,g:'foot',tag:'발목 조절',name:'발뒤꿈치와 발가락 번갈아 들기',dose:'8~12회',img:'p5_03.png'},
  {n:48,g:'foot',tag:'종아리 가동성',name:'벽 짚고 종아리 늘리기',dose:'좌우 20~30초 × 2',cue:'뒤쪽 무릎을 편다',img:'p5_04.png'},
  {n:49,g:'foot',tag:'발목 가동성',name:'무릎 굽혀 종아리 아래쪽 늘리기',dose:'좌우 20~30초 × 2',cue:'뒤꿈치를 바닥에 둔다',img:'p5_05.png'},
  {n:50,g:'foot',tag:'균형',name:'발을 일자로 두고 서기',dose:'좌우 앞발 20~30초 × 2',cue:'필요하면 벽 가까이 선다',img:'p5_06.png'},
  {n:51,g:'foot',tag:'균형·협응',name:'벽 짚고 발로 시계 그리기',dose:'좌우 방향별 3회',cue:'지지하는 발의 아치를 유지한다',img:'p5_07.png'},
  {n:52,g:'foot',tag:'균형',name:'쿠션 위에 두 발로 서기',dose:'20~30초 × 2',cue:'안전을 위해 벽 가까이 선다',img:'p5_08.png'},
  {n:53,g:'foot',tag:'발목 안정',name:'밴드를 바깥으로 밀고 버티기',dose:'좌우 10~20초 × 2',cue:'무릎은 움직이지 않는다',img:'p5_09.png'},
  {n:54,g:'foot',tag:'정강이·발목',name:'벽에 기대 발등 들어올리기',dose:'8~12회 × 1~2',cue:'뒤꿈치는 바닥에 둔다',img:'p5_10.png'},
  {n:55,g:'foot',tag:'체중 이동',name:'벽 짚고 체중 좌우로 옮기기',dose:'좌우 왕복 8~10회',cue:'상체를 기울이지 않는다',img:'p5_11.png'},
  {n:56,g:'upper',tag:'어깨 가동성',name:'벽에 기대 팔 위아래로 움직이기',dose:'6~10회',cue:'허리를 과하게 띄우지 않는다',img:'p6_01.png'},
  {n:57,g:'upper',tag:'견갑 조절',name:'벽 짚고 날개뼈 시계 그리기',dose:'방향별 5회',cue:'팔보다 날개뼈를 작게 움직인다',img:'p6_02.png'},
  {n:58,g:'upper',tag:'견갑 조절',name:'폼롤러 밀며 팔 위로 올리기',dose:'6~10회',cue:'어깨를 으쓱하지 않는다',img:'p6_03.png'},
  {n:59,g:'upper',tag:'가슴·어깨',name:'문틀 짚고 가슴 앞쪽 늘리기',dose:'좌우 20~30초 × 2',img:'p6_04.png'},
  {n:60,g:'upper',tag:'어깨 뒤쪽',name:'팔을 가슴 앞으로 당겨 늘리기',dose:'좌우 20~30초 × 2',img:'p6_05.png'},
  {n:61,g:'upper',tag:'어깨 조절',name:'팔 크게 원 그리기',dose:'좌우 방향별 3~5회',cue:'통증 없는 범위에서 천천히',img:'p6_06.png'},
  {n:62,g:'upper',tag:'손목 가동성',name:'손바닥 위로 두고 손목 늘리기',dose:'좌우 20초 × 2',img:'p6_07.png'},
  {n:63,g:'upper',tag:'손목 가동성',name:'손등 위로 두고 손목 늘리기',dose:'좌우 20초 × 2',img:'p6_08.png'},
  {n:64,g:'upper',tag:'신경 가동성',name:'팔과 손목 부드럽게 신경 움직이기',dose:'좌우 5~8회',cue:'저림이 생기기 전 범위까지만',img:'p6_09.png'},
  {n:65,g:'upper',tag:'목 가동성',name:'의자에 앉아 목 좌우로 돌리기',dose:'좌우 5~8회',cue:'턱 높이를 유지한다',img:'p6_10.png'},
  {n:66,g:'upper',tag:'목·견갑',name:'고개 겨드랑이 쪽으로 숙여 늘리기',dose:'좌우 15~20초 × 2',cue:'손으로 세게 당기지 않는다',img:'p6_11.png'}
];

const catalogue = document.querySelector('#catalogue');
catalogue.innerHTML = movements.map(m => `
  <article class="movement" data-group="${m.g}">
    <div class="movement__meta"><span class="movement__number">${String(m.n).padStart(2,'0')}</span><span class="movement__tag">${m.tag}</span></div>
    <h2>${m.name}</h2>
    <p class="movement__dose">${m.dose}</p>
    <div class="movement__image"><img src="assets/movements/${m.img}" alt="${m.name} 동작 그림" loading="lazy"></div>
    ${m.cue ? `<p class="movement__cue">${m.cue}</p>` : ''}
  </article>`).join('');

document.querySelectorAll('.filter').forEach(button => button.addEventListener('click', () => {
  const selected = button.dataset.filter;
  document.querySelectorAll('.filter').forEach(b => { const active=b===button; b.classList.toggle('is-active',active); b.setAttribute('aria-pressed',String(active)); });
  document.querySelectorAll('.movement').forEach(card => { card.hidden = selected !== 'all' && card.dataset.group !== selected; });
}));
