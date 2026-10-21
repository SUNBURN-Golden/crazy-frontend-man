import os,subprocess
from PIL import Image
OUT="/workspace/viral/w1/design/ig"
SANS="Pretendard,'Noto Sans CJK KR','Noto Sans KR',-apple-system,sans-serif"
SERIF="'Noto Serif CJK KR','Noto Serif KR',Georgia,serif"
def P(d): return f'<path d="{d}"/>'
I={ # 100x100 line icons
'kettle':P("M38 34 a12 12 0 0 1 24 0")+P("M30 44 h40 l6 30 a6 6 0 0 1-6 6 H30 a6 6 0 0 1-6-6 z"),
'door':P("M30 80 V20 h34 v60")+P("M22 80 h56")+P("M56 50 h0.1")+P("M70 36 l10 10 l-10 10")+P("M80 46 H62"),
'sauna':P("M20 70 h60")+P("M26 70 v12 M74 70 v12")+P("M36 54 c-6-8 6-12 0-20 M50 54 c-6-8 6-12 0-20 M64 54 c-6-8 6-12 0-20"),
'pen':P("M50 18 L66 50 L50 82 L34 50 Z")+P("M50 50 V82")+'<circle cx="50" cy="50" r="5"/>',
'cal':P("M22 30 h56 v48 H22 z")+P("M22 44 h56 M36 22 v14 M64 22 v14")+P("M38 62 l8 8 l16-16"),
'tree':P("M50 22 V46 M50 46 L28 68 M50 46 L72 68 M50 46 V72")+'<circle cx="50" cy="18" r="6"/><circle cx="28" cy="72" r="6"/><circle cx="50" cy="76" r="6"/><circle cx="72" cy="72" r="6"/>',
'list':P("M38 30 h40 M38 50 h40 M38 70 h40")+'<circle cx="24" cy="30" r="3"/><circle cx="24" cy="50" r="3"/><circle cx="24" cy="70" r="3"/>',
'rise':P("M22 76 L42 54 L54 64 L78 36")+P("M62 36 h16 v16"),
'mail':P("M20 30 h60 v40 H20 z")+P("M20 30 l30 24 l30-24"),
'quote':P("M26 62 c0-14 4-22 16-28 M26 62 a8 8 0 1 0 16 0 a8 8 0 1 0-16 0")+P("M58 62 c0-14 4-22 16-28 M58 62 a8 8 0 1 0 16 0 a8 8 0 1 0-16 0"),
'panel':P("M20 24 h60 v52 H20 z M50 24 v52 M20 52 h30"),
'phone':P("M34 16 h32 a4 4 0 0 1 4 4 v60 a4 4 0 0 1-4 4 H34 a4 4 0 0 1-4-4 V20 a4 4 0 0 1 4-4 z")+P("M40 34 h20 M40 46 h20 M40 58 h12"),
'book':P("M50 30 c-8-6-20-8-30-6 v50 c10-2 22 0 30 6 c8-6 20-8 30-6 V24 c-10-2-22 0-30 6 z M50 30 v50"),
'scale':P("M50 20 V80 M34 80 h32 M22 32 h56")+P("M22 32 l-10 24 h20 z M78 32 l-10 24 h20 z"),
'tag':P("M20 22 h30 l30 30 l-28 28 l-32-32 z")+'<circle cx="34" cy="36" r="5"/>',
'shield':P("M50 18 l28 10 v20 c0 18-12 28-28 34 c-16-6-28-16-28-34 V28 z")+P("M38 50 l8 8 l16-16"),
'rules':P("M28 16 h32 l14 14 v54 H28 z M60 16 v14 h14")+P("M38 46 h26 M38 58 h26 M38 70 h18"),
'opensign':P("M50 18 L30 40 M50 18 L70 40")+'<circle cx="50" cy="18" r="3"/>'+P("M20 40 h60 v30 H20 z")+P("M32 55 h36"),
'heart':P("M50 76 C24 58 18 44 26 34 c7-9 18-6 24 4 c6-10 17-13 24-4 c8 10 2 24-24 42 z"),
}
def icon(k,c,sz,sw=4): return f'<svg width="{sz}" height="{sz}" viewBox="0 0 100 100" fill="none" stroke="{c}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{I[k]}</svg>'
def shot(path,body,w,h,font,bg,keep_src=False):
    html=f"<!doctype html><html><head><meta charset=utf-8><style>*{{margin:0;box-sizing:border-box}}body{{width:{w}px;height:{h}px;overflow:hidden;background:{bg};font-family:{font};word-break:keep-all}}</style></head><body>{body}</body></html>"
    hp=path[:-4]+".html"; open(hp,"w").write(html)
    subprocess.run(["google-chrome","--headless=new","--no-sandbox","--hide-scrollbars","--force-device-scale-factor=1",f"--window-size={w},{h}",f"--screenshot={path}",f"file://{hp}"],capture_output=True)
    if not keep_src: os.remove(hp)
    im=Image.open(path).convert("RGB"); im.quantize(colors=128,method=Image.MEDIANCUT,dither=Image.Dither.NONE).save(path,optimize=True)
A={
'hanset':dict(bg="#F5F2EC",ink="#1A1A1A",mut="#6B665E",line="#D9D3C7",ac="#E4572E",acd="#B83C1A",soft="#EFE6DA",font=SANS,head=SANS,
  mark='<div style="font-size:{s}px;font-weight:800;letter-spacing:-0.04em;color:#1A1A1A;line-height:1">H<span style="color:#E4572E">.</span></div>',
  name="HANSET",hl=[('kettle','HYROX 서울'),('door','드롭인'),('sauna','사우나'),('rules','문신 규정'),('cal','확인일')],
  tiles=[('','HANSET','운동하고, 땀 빼고, 쉬어요'),('SAUNA','문신 있어도 되는 사우나','확인일 YYYY.MM.DD'),('HYROX','HYROX 서울 D-day 체크','저장해 두세요')],
  post=('SAUNA','문신 있어도<br>되는 사우나','곳마다 확인일을 적어 둬요','확인일 YYYY.MM.DD · 출처 사이트 가이드')),
'kitchen-genome':dict(bg="#FAF8F3",ink="#1F1D1A",mut="#5F5A53",line="#E6E1D8",ac="#A3412A",acd="#A3412A",soft="#F4E7E1",font=SANS,head=SANS,mark=None,
  name="키친 게놈",hl=[('tree','계보'),('list','디렉토리'),('opensign','새로 연 가게'),('mail','제보')],
  tiles=[('','키친 게놈','그 셰프, 어느 주방 출신일까요'),('LINEAGE','○○ 출신 셰프들이<br>연 가게','출처 · 확인일 표기'),('TIP','아는 계보 있으면<br>알려주세요','프로필 링크에서 제보해요')],
  post=('LINEAGE','○○ 출신<br>셰프들이 연 가게','계보마다 출처를 붙여요','출처 링크 · 확인일 YYYY.MM.DD')),
'goallit':dict(bg="#FAF9F5",ink="#1A1A1A",mut="#5E5D59",line="#E4E2DD",ac="#C96442",acd="#B85635",soft="#F2E6DF",font=SANS,head=SERIF,
  mark='<div style="font-family:'+SERIF.replace("'","&#39;")+';font-size:{s}px;font-weight:700;color:#1A1A1A;line-height:1">G<span style="color:#C96442">.</span></div>',
  name="Goal Lit",hl=[('quote','오늘의 평론'),('panel','웹툰'),('phone','웹소설'),('book','신간·완결'),('scale','편집원칙')],
  tiles=[('','Goal Lit','잘 읽히는 것과 잘 쓰인 것은 달라요'),('CRITIQUE','“평론 첫 문장이 여기에 들어가요”','작품명 · 작가'),('NEW','이번 주 신간·완결','출처 · 확인일 표기')],
  post=('CRITIQUE','“평론 첫 문장이<br>여기에 들어가요”','작품명 · 작가','출처 · 확인일 YYYY.MM.DD')),
'agamajung':dict(bg="#f8f6f0",ink="#334338",mut="#5f645a",line="#dcded2",ac="#8b6344",acd="#8b6344",soft="#e6eadf",font="'Noto Sans CJK KR','Noto Sans KR',sans-serif",head=SERIF,
  mark='<div style="width:{s}px;height:{s}px;border-radius:{r}px {r}px 6px 6px;background:#e6eadf;display:flex;align-items:center;justify-content:center;font-family:'+SERIF.replace("'","&#39;")+';font-weight:700;color:#334338;font-size:{f}px;letter-spacing:-0.02em">마중</div>',
  name="아가마중",hl=[('tag','가격 비교'),('cal','공구 캘린더'),('shield','셀러 체크'),('heart','육아템')],
  tiles=[('','아가마중','좋은 것은 우리가 골라 둘게요'),('PRICE','트립트랩 가격 비교','공구가 · 공식가 · 해외가 · 중고'),('CHECK','셀러 체크리스트','통신판매업 · 청약철회 7일')],
  post=('PRICE','트립트랩<br>가격 비교','조회 시점 기준이에요','출처 · 확인일 YYYY.MM.DD')),
}
def kglogo(sz,c): return icon('tree',c,sz,5)
ONLY=dict(x.split(':') for x in os.environ.get('ONLY','').split(',') if x)
for k,a in A.items():
    if ONLY and k not in ONLY: continue
    W=ONLY.get(k,'all')
    d=f"{OUT}/{k}"
    # profile
    if k!='kitchen-genome' and W=='all':
        if k=='agamajung': m=a['mark'].format(s=200,r=100,f=64)
        else: m=a['mark'].format(s=190)
        shot(f"{d}/profile_320.png",f'<div style="width:320px;height:320px;display:flex;align-items:center;justify-content:center">{m}</div>',320,320,a['font'],a['bg'])
    # highlights
    for i,(ic,lab) in enumerate(a['hl'],1):
        if W not in('all','hl'): break
        shot(f"{d}/highlight_{i}_{ic}.png",f'<div style="width:1080px;height:1920px;display:flex;align-items:center;justify-content:center"><div style="width:560px;height:560px;border-radius:50%;background:{a["soft"]};display:flex;align-items:center;justify-content:center">{icon(ic,a["acd"],300,4.5)}</div></div>',1080,1920,a['font'],a['bg'])
    # post card
    def card(tag,title,sub,foot,scale=1):
        top=f'<div style="font-size:30px;font-weight:700;letter-spacing:4px;color:{a["acd"]}">{tag}</div>' if tag else (kglogo(180,a['ac']) if k=='kitchen-genome' else (a['mark'].format(s=200,r=100,f=64) if k=='agamajung' else a['mark'].format(s=180)))
        return f'''<div style="width:1080px;height:1350px;padding:110px 96px 90px;display:flex;flex-direction:column;color:{a["ink"]}">
{top}<div style="font-family:{a["head"]};font-size:{104 if tag else 120}px;font-weight:800;line-height:1.18;letter-spacing:-0.02em;margin-top:{80 if tag else 70}px">{title}</div>
<div style="font-size:44px;color:{a["mut"]};margin-top:40px;line-height:1.5">{sub}</div>
<div style="margin-top:auto;border-top:2px solid {a["line"]};padding-top:30px;display:flex;justify-content:space-between;font-size:28px;color:{a["mut"]}"><span>{a["name"]}</span><span>{foot}</span></div></div>'''
    if W=='all':
      shot(f"{d}/post_template_1080x1350.png",card(*a['post']),1080,1350,a['font'],a['bg'],keep_src=True)
      os.rename(f"{d}/post_template_1080x1350.html",f"{d}/post_template.html")
    HL=' / '.join(f'{i} {l} (highlight_{i}_{c}.png)' for i,(c,l) in enumerate(a['hl'],1))
    tiles=[]
    for j,(t,ti,su) in enumerate(a['tiles'] if W!='hl' else []):
        bg=a['bg'] if j!=1 else a['soft']
        shot(f"/tmp/t{j}.png",card(t,ti,su,'',),1080,1350,a['font'],bg); tiles.append(Image.open(f"/tmp/t{j}.png").convert("RGB").resize((540,675),Image.LANCZOS)); os.remove(f"/tmp/t{j}.png")
    if W!='hl':
     g=Image.new("RGB",(540*3+8,675),"#FFFFFF")
     for j,t in enumerate(tiles): g.paste(t,(j*544,0))
     g.quantize(colors=128,method=Image.MEDIANCUT,dither=Image.Dither.NONE).save(f"{d}/grid_first_row.png",optimize=True)
    open(f"{d}/tone-guide.md","w").write(f"""# {a['name']} 첫 줄 그리드 톤 가이드
- 배경 {a['bg']} / 글자 {a['ink']} / 보조 {a['mut']} / 강조 {a['acd']} 한 가지만 써요. 가운데 칸만 연한 면색 {a['soft']}.
- 세 칸 순서: 왼쪽 브랜드 카드 → 가운데 대표 콘텐츠 → 오른쪽 저장·제보 유도.
- 한 장에 제목 1줄(최대 2줄) + 보조 1줄. 1초 안에 읽혀야 해요.
- 상단 태그(영문 대문자, 강조색)로 주제를 구분해요. 사진·외부 이미지는 쓰지 않아요.
- 하단 줄: 왼쪽 계정명, 오른쪽 출처·확인일.
- 하이라이트: {HL}
- 템플릿: post_template.html 텍스트만 바꾸고 1080x1350으로 렌더링해요.
""")
