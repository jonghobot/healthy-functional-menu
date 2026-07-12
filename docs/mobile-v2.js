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
  {n:22,g:'whole',tag:'힘줄·발목',name:'벽 짚고 까치발 버티기',dose:'15~30초 × 2',cue:'반동 없이 편안한 높이에서 멈춘다',img:'p2_11.png'}
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
