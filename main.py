from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.metrics import dp

TILES = ['1万','2万','3万','4万','5万','6万','7万','8万','9万',
'1筒','2筒','3筒','4筒','5筒','6筒','7筒','8筒','9筒',
'1条','2条','3条','4条','5条','6条','7条','8条','9条',
'东','南','西','北','中','发','白','红中']

class AI:
    def best(self, hand):
        scores = {}
        for t in hand:
            if t == '红中': scores[t] = 100
            elif t in ['东','南','西','北','中','发','白']:
                scores[t] = 30 if hand.count(t)>=2 else -10
            else:
                r = int(t[0])
                if r in [1,9]: scores[t] = 20 if hand.count(t)>=2 else -15
                else: scores[t] = 10 if any(f"{x}{t[1]}" in hand for x in [r-1,r+1] if x>=1 and x<=9 and f"{x}{t[1]}"!=t) else -20
        return min(scores, key=scores.get)
    def tip(self, t, hand):
        if t == '红中': return "赖子保留"
        if t in ['东','南','西','北','中','发','白']: return ("对子" if hand.count(t)>=2 else "孤立")+"建议打"
        r = int(t[0])
        return ("幺九" if r in [1,9] else "中张")+"建议打"

ai = AI()

class B(Button):
    def __init__(s,t,**kw): super().__init__(**kw); s.tile=t;s.text=t;s.font_size=dp(14);s.size_hint=(None,None);s.width, s.height=dp(45),dp(35);s.background_normal='';s.background_color=(0.9,0.85,0.75,1)

class RB(Button):
    def __init__(s,t,r,**kw): super().__init__(**kw); s.tile, s.rm = t, r; s.text, s.font_size = t, dp(12); s.size_hint=(None,None); s.width, s.height = dp(40),dp(30); s.background_normal, s.background_color = '',(0.2,0.6,0.2,1)

class MahjongApp(App):
    def __init__(s): super().__init__(); s.tiles=[]; s.btns={}
    def build(s):
        Window.clearcolor=(0.1,0.1,0.15,1)
        L = BoxLayout(orientation='vertical',padding=dp(8),spacing=dp(5))
        L.add_widget(Label(text='🀄 麻将AI助手',font_size=dp(22),size_hint_y=None,height=dp(40),color=(1,0.9,0.5,1)))
        L.add_widget(Label(text='手牌(点击移除):',font_size=dp(14),size_hint_y=None,height=dp(25),color=(0.8,0.8,0.8,1)))
        s.hs = ScrollView(size_hint_y=None,height=dp(45)); s.hl=BoxLayout(spacing=dp(3),padding=dp(3)); s.hl.bind(minimum_width=s.hl.setter('width')); s.hs.add_widget(s.hl); L.add_widget(s.hs)
        bl = BoxLayout(size_hint_y=None,height=dp(35),spacing=dp(5))
        bl.add_widget(Button(text='清空',on_press=s.clr))
        bl.add_widget(Button(text='🤖 AI分析',on_press=s.an,background_color=(0.2,0.5,0.8,1)))
        L.add_widget(bl)
        s.rl = Label(text='选14张牌',font_size=dp(14),size_hint_y=None,height=dp(60),color=(1,1,1,1))
        L.add_widget(s.rl)
        L.add_widget(Label(text='🃏选牌:',font_size=dp(14),size_hint_y=None,height=dp(25),color=(0.8,0.8,0.8,1)))
        sv=ScrollView(); gl=GridLayout(cols=10,spacing=dp(2),padding=dp(2)); gl.bind(minimum_height=gl.setter('height'))
        for t in TILES: b=B(t,on_press=s.sel); s.btns[t]=b; gl.add_widget(b)
        sv.add_widget(gl); L.add_widget(sv)
        return L
    def sel(s,b):
        if len(s.tiles)>=14: s.pop('提示','14张已满!'); return
        if b.tile not in s.tiles: s.tiles.append(b.tile); s.upd(); b.background_color=(0.3,0.7,0.3,1)
    def rm(s,b):
        if b.tile in s.tiles: s.tiles.remove(b.tile); s.upd()
        if b.tile in s.btns: s.btns[b.tile].background_color=(0.9,0.85,0.75,1)
    def upd(s):
        s.hl.clear_widgets()
        for t in s.tiles: s.hl.add_widget(RB(t,s.rm))
        s.rl.text = str(len(s.tiles))+'/14 '+('✅已满' if len(s.tiles)==14 else '')
    def clr(s,_):
        s.tiles=[]; [setattr(b,'background_color',(0.9,0.85,0.75,1)) for b in s.btns.values()]; s.upd(); s.rl.text='已清空'
    def an(s,_):
        if len(s.tiles)!=14: s.pop('提示',str(len(s.tiles))+'张不行'); return
        b = ai.best(s.tiles)
        s.rl.text = "💡 建议打 【"+b+"】\n\n"+ai.tip(b,s.tiles); s.rl.color = (0.5,1,0.5,1)
    def pop(s,t,m):
        c=BoxLayout(orientation='vertical',padding=dp(15)); c.add_widget(Label(text=m,font_size=dp(16))); c.add_widget(Button(text='OK',size_hint_y=None,height=dp(40),on_press=lambda _:p.dismiss()))
        p=Popup(title=t,content=c,size_hint=(0.8,0.35)); p.open()

MahjongApp().run()
