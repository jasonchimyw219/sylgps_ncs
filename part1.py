html = []
html.append(r"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1">
<title>繁中白板 Primary 1</title>
<style>
:root{
  --pri:#5B5EA6;--pri2:#9B59B6;--ok:#27AE60;--err:#E74C3C;--warn:#F39C12;
  --bg:#F7F7FB;--bg2:#FFFFFF;--txt:#2C2C54;--muted:#888;--border:#E0E0EE;
  --rad:16px;--sha:0 4px 18px rgba(0,0,0,.10);
}
body.dark{
  --bg:#1a1a2e;--bg2:#16213e;--txt:#eee;--muted:#aaa;--border:#2a2a4a;
}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:'Noto Sans TC',sans-serif,system-ui;background:var(--bg);color:var(--txt);
  min-height:100vh;font-size:18px;transition:background .3s,color .3s;}
.screen{display:none;flex-direction:column;min-height:100vh;max-width:820px;margin:0 auto;padding:16px;}
.screen.active{display:flex;}
/* Game header */
.gh{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;flex-wrap:wrap;gap:8px;}
.ghT{font-size:22px;font-weight:900;color:var(--pri);}
/* Buttons */
.btn{padding:12px 22px;border:none;border-radius:12px;font-size:16px;font-weight:700;cursor:pointer;
  background:var(--pri);color:#fff;transition:transform .1s,opacity .1s;touch-action:manipulation;}
.btn:active{transform:scale(.95);}
.bSm{padding:9px 16px;font-size:14px;}
.bSec{background:var(--ok);}
.bErr{background:var(--err);}
.bOut{background:transparent;color:var(--pri);border:2px solid var(--pri);}
.bInf{background:#2980B9;}
.bRow{display:flex;gap:10px;flex-wrap:wrap;margin-top:12px;}
.bRow2{display:flex;gap:10px;flex-wrap:wrap;justify-content:center;margin-top:14px;}
/* Cards */
.card{background:var(--bg2);border-radius:var(--rad);padding:18px;box-shadow:var(--sha);margin-bottom:14px;}
/* Timer */
.timerBox{font-size:15px;font-weight:700;color:var(--warn);background:rgba(243,156,18,.12);
  padding:5px 12px;border-radius:20px;display:none;}
/* Progress dots */
.qdots{display:flex;gap:5px;flex-wrap:wrap;}
.qdot{width:10px;height:10px;border-radius:50%;background:var(--border);}
.qdot.done{background:var(--ok);}
.qdot.cur{background:var(--pri);}
/* Scoreboard */
.sbArea{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px;}
.scCard{background:var(--bg2);border-radius:12px;padding:10px 14px;min-width:90px;text-align:center;
  box-shadow:var(--sha);cursor:pointer;border:2px solid transparent;transition:border .2s;}
.scCard.active{border-color:var(--pri);}
.scCard.lvB{border-left:4px solid var(--warn);}
.scN{font-size:14px;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:80px;}
.scS{font-size:18px;font-weight:900;color:var(--pri);}
.scPick{font-size:11px;color:var(--muted);margin-top:2px;}
/* Complete banner */
.completeBanner{display:none;background:linear-gradient(135deg,var(--pri),var(--pri2));
  color:#fff;border-radius:var(--rad);padding:24px;text-align:center;margin:12px 0;
  box-shadow:0 6px 24px rgba(91,94,166,.35);}
.completeBanner.show{display:block;}
.bigTxt{font-size:22px;font-weight:900;margin-bottom:10px;}
/* Feedback */
.fb{font-size:18px;font-weight:700;min-height:28px;margin:8px 0;text-align:center;}
/* Hint box */
.hintBox{background:rgba(91,94,166,.1);border-radius:10px;padding:10px 14px;
  font-size:15px;color:var(--pri);display:none;margin:8px 0;}
.hintBox.show{display:block;}
/* Toggle buttons */
.tglRow{display:flex;gap:6px;flex-wrap:wrap;}
.tgl{padding:8px 14px;border:2px solid var(--border);border-radius:10px;font-size:14px;
  font-weight:700;cursor:pointer;background:var(--bg2);color:var(--muted);transition:all .2s;}
.tgl.on{background:var(--pri);color:#fff;border-color:var(--pri);}
/* Teacher panel */
.tPanel{background:var(--bg2);border-radius:var(--rad);padding:18px;margin-bottom:14px;box-shadow:var(--sha);}
.tPanel h3{font-size:16px;font-weight:800;color:var(--pri);margin-bottom:12px;}
.setGrid{display:grid;grid-template-columns:1fr 1fr;gap:12px;}
.setItem{background:var(--bg);border-radius:10px;padding:12px;}
.setLbl{font-size:13px;font-weight:700;color:var(--muted);margin-bottom:8px;}
.stRow{display:flex;align-items:center;gap:8px;margin-bottom:10px;flex-wrap:wrap;}
.nameInput{flex:1;min-width:100px;padding:8px 12px;border-radius:10px;
  border:2px solid var(--border);background:var(--bg);color:var(--txt);font-size:15px;}
.lvlRow{display:flex;gap:5px;}
.lvlBtn{padding:6px 10px;border:2px solid var(--border);border-radius:8px;font-size:13px;
  font-weight:700;cursor:pointer;background:var(--bg);color:var(--muted);}
.lvlBtn.on{background:var(--pri);color:#fff;border-color:var(--pri);}
.removeBtn{width:30px;height:30px;border-radius:50%;border:none;background:var(--err);
  color:#fff;font-size:16px;cursor:pointer;line-height:1;}
.progBar{height:8px;background:var(--border);border-radius:4px;overflow:hidden;}
.progFill{height:100%;background:var(--pri);border-radius:4px;transition:width .4s;}
/* G1 - 詞語配對 */
.matchGrid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0;}
.matchWord{background:var(--bg2);border:2px solid var(--border);border-radius:12px;
  padding:14px 10px;text-align:center;font-size:22px;font-weight:900;cursor:pointer;
  transition:all .2s;min-height:70px;display:flex;align-items:center;justify-content:center;}
.matchWord.sel{border-color:var(--pri);background:rgba(91,94,166,.12);transform:scale(1.04);}
.matchWord.done{opacity:.3;pointer-events:none;background:var(--ok);color:#fff;border-color:var(--ok);}
.matchWord.wrong{border-color:var(--err);animation:shake .3s;}
.matchDef{background:var(--bg2);border:2px solid var(--border);border-radius:12px;
  padding:12px 10px;text-align:center;font-size:15px;cursor:pointer;transition:all .2s;
  min-height:70px;display:flex;align-items:center;justify-content:center;}
.matchDef.sel{border-color:var(--ok);background:rgba(39,174,96,.08);}
.matchDef.done{opacity:.3;pointer-events:none;background:var(--ok);color:#fff;border-color:var(--ok);}
.matchDef.wrong{border-color:var(--err);animation:shake .3s;}
/* G2 - 填空 */
.fillSent{font-size:24px;font-weight:700;line-height:1.8;text-align:center;margin:12px 0;padding:16px;
  background:var(--bg2);border-radius:var(--rad);box-shadow:var(--sha);}
.fillBlank{display:inline-block;min-width:80px;border-bottom:3px solid var(--pri);
  text-align:center;color:var(--pri);font-weight:900;padding:0 8px;vertical-align:bottom;}
.fillOpts{display:flex;gap:10px;flex-wrap:wrap;justify-content:center;margin:12px 0;}
.fillOpt{background:var(--bg2);border:2px solid var(--border);border-radius:12px;
  padding:12px 18px;font-size:20px;font-weight:800;cursor:pointer;transition:all .2s;
  touch-action:manipulation;}
.fillOpt:hover{border-color:var(--pri);}
.fillOpt.correct{background:var(--ok);color:#fff;border-color:var(--ok);}
.fillOpt.wrong{background:var(--err);color:#fff;border-color:var(--err);}
/* G3 - 句子重組 */
.sentB{min-height:80px;border:2px dashed var(--border);border-radius:var(--rad);
  padding:12px;display:flex;flex-wrap:wrap;gap:8px;align-items:center;
  background:var(--bg2);margin:10px 0;transition:border-color .2s;}
.sentB.over{border-color:var(--pri);background:rgba(91,94,166,.05);}
.wcard{background:var(--pri);color:#fff;border-radius:10px;padding:10px 14px;
  font-size:20px;font-weight:800;cursor:grab;touch-action:none;user-select:none;
  box-shadow:0 2px 8px rgba(91,94,166,.3);transition:transform .15s,opacity .15s;}
.wcard:active{cursor:grabbing;transform:scale(1.08);}
.wcard.used{opacity:.35;cursor:not-allowed;}
#g3pool{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0;min-height:50px;}
/* G4 - 標點符號 */
.puntSent{font-size:22px;font-weight:700;line-height:2.0;text-align:center;padding:16px;
  background:var(--bg2);border-radius:var(--rad);box-shadow:var(--sha);margin:10px 0;
  display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:2px;}
.pSlot{display:inline-flex;align-items:center;justify-content:center;
  min-width:44px;height:44px;border:2px dashed var(--border);border-radius:8px;
  font-size:20px;font-weight:900;cursor:pointer;transition:all .2s;
  background:var(--bg);color:var(--pri);margin:2px;}
.pSlot.filled{border-style:solid;border-color:var(--pri);background:rgba(91,94,166,.1);}
.pSlot.ok{border-color:var(--ok);background:rgba(39,174,96,.1);color:var(--ok);}
.pSlot.err{border-color:var(--err);background:rgba(231,76,60,.1);color:var(--err);}
.pKeys{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:12px 0;}
.pKey{background:var(--bg2);border:2px solid var(--border);border-radius:10px;
  padding:10px 16px;font-size:22px;font-weight:900;cursor:pointer;transition:all .2s;
  min-width:48px;text-align:center;touch-action:manipulation;}
.pKey:active{background:var(--pri);color:#fff;}
/* G5 - 量詞 */
.mwQ{font-size:26px;font-weight:700;text-align:center;padding:20px;
  background:var(--bg2);border-radius:var(--rad);box-shadow:var(--sha);margin:10px 0;line-height:1.8;}
.mwBlank{display:inline-block;min-width:60px;border-bottom:3px solid var(--pri);
  text-align:center;color:var(--pri);font-weight:900;padding:0 6px;vertical-align:bottom;}
.mwOpts{display:flex;gap:12px;flex-wrap:wrap;justify-content:center;margin:12px 0;}
.mwOpt{background:var(--bg2);border:2px solid var(--border);border-radius:12px;
  padding:16px 24px;font-size:26px;font-weight:900;cursor:pointer;transition:all .2s;
  touch-action:manipulation;min-width:70px;text-align:center;}
.mwOpt:hover{border-color:var(--pri);}
.mwOpt.correct{background:var(--ok);color:#fff;border-color:var(--ok);}
.mwOpt.wrong{background:var(--err);color:#fff;border-color:var(--err);}
.pop{animation:pop .3s;}
/* G6 - 閱讀理解 */
.passText{font-size:18px;line-height:2;background:var(--bg2);border-radius:var(--rad);
  padding:18px;box-shadow:var(--sha);margin:10px 0;max-height:220px;overflow-y:auto;}
.rdQ{background:var(--bg2);border-radius:12px;padding:14px;margin-bottom:12px;box-shadow:var(--sha);}
.rdQT{font-size:16px;font-weight:700;margin-bottom:10px;}
.rdOpts{display:flex;flex-direction:column;gap:8px;}
.rdOpt{padding:10px 14px;border:2px solid var(--border);border-radius:10px;
  font-size:15px;cursor:pointer;transition:all .2s;touch-action:manipulation;}
.rdOpt:hover{border-color:var(--pri);}
.rdOpt.correct{background:var(--ok);color:#fff;border-color:var(--ok);}
.rdOpt.wrong{background:var(--err);color:#fff;border-color:var(--err);}
.rdFill{width:100%;padding:8px 12px;border-radius:8px;border:2px solid var(--border);
  font-size:16px;background:var(--bg);color:var(--txt);}
/* Home game cards */
.gameGrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px;margin:10px 0;}
.gameCard{background:var(--bg2);border-radius:var(--rad);padding:18px 12px;text-align:center;
  cursor:pointer;box-shadow:var(--sha);transition:transform .15s,box-shadow .15s;
  border:2px solid transparent;}
.gameCard:hover{transform:translateY(-3px);box-shadow:0 8px 28px rgba(0,0,0,.14);}
.gameCard:active{transform:scale(.96);}
.gcIco{font-size:36px;margin-bottom:8px;}
.gcNm{font-size:15px;font-weight:800;}
.gcSub{font-size:12px;color:var(--muted);margin-top:3px;}
/* Leaderboard */
.lbRow{display:flex;align-items:center;gap:12px;padding:12px 16px;
  background:var(--bg2);border-radius:12px;margin-bottom:8px;box-shadow:var(--sha);}
.lbRk{font-size:22px;min-width:36px;text-align:center;}
.lbNm{flex:1;font-size:18px;font-weight:700;}
.lbSc{font-size:22px;font-weight:900;color:var(--pri);}
/* Startup screen */
.startCard{background:var(--bg2);border-radius:var(--rad);padding:24px;
  box-shadow:var(--sha);max-width:500px;width:100%;margin:0 auto;}
.startTitle{font-size:28px;font-weight:900;color:var(--pri);text-align:center;margin-bottom:8px;}
.startSub{font-size:15px;color:var(--muted);text-align:center;margin-bottom:20px;}
.stInput{width:100%;padding:12px 16px;border-radius:12px;border:2px solid var(--border);
  font-size:18px;background:var(--bg);color:var(--txt);margin-bottom:10px;}
/* Chapter badge */
.chBdg{display:inline-flex;align-items:center;gap:6px;padding:5px 12px;border-radius:20px;
  font-size:13px;font-weight:700;color:#fff;}
.ch1{background:#E74C3C;}.ch2{background:#E67E22;}.ch3{background:#27AE60;}.ch4{background:#2980B9;}
/* Animations */
@keyframes shake{0%,100%{transform:translateX(0);}25%{transform:translateX(-6px);}75%{transform:translateX(6px);}}
@keyframes pop{0%{transform:scale(1);}50%{transform:scale(1.25);}100%{transform:scale(1);}}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px);}to{opacity:1;transform:translateY(0);}}
.fadeIn{animation:fadeIn .3s ease;}
/* Confetti canvas */
#confetti{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:999;}
/* Dark mode toggle */
.iBtn{background:none;border:none;font-size:20px;cursor:pointer;padding:4px 8px;border-radius:8px;}
.iBtn:hover{background:var(--border);}
/* Responsive */
@media(max-width:500px){
  .setGrid{grid-template-columns:1fr;}
  .matchGrid{grid-template-columns:1fr 1fr;}
  .matchWord{font-size:18px;padding:10px 6px;}
}
</style>
</head>
<body>
<canvas id="confetti"></canvas>
""")

with open('/sessions/exciting-fervent-edison/mnt/outputs/index.html','w',encoding='utf-8') as f:
    f.write('\n'.join(html))
print(f"Part 1 done: {sum(len(h) for h in html)} chars")
