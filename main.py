从 kivy.应用 进口 App
极好的 __init__(s，t，r，**千瓦): 极好的()。_ _ init __(* *千瓦)；s瓦，s。空间= t，r；南文本，s.字体大小 = 温差(12)；南大小提示=(没有，没有)；南宽度，s.高度 = 数据处理(40)，DP(30)；南背景正常.背景颜色 = ' '、(0.2，0.6，0.2，1)def __init__(s，t，r，**kw): super()。_ _ init _ _(* * kw)；s瓦，s.rm = t，r；s.text，s.font_size = t，DP(12)；s.size_hint=(None，None)；s.width，s.height = dp(40)，DP(30)；s.background_normal，s.background_color = ' '，(0.2，0.6，0.2，1)uix.boxlayout进口方框布局
从kivy.uix.gridlayout进口网格布局
从kivy.uix.scrollview导入scrollview kivy.uix.scrollview导入scrollview
从kivy.uix.button导入按钮kivy.uix.button导入按钮uix.button导入按钮kivy.uix.button导入按钮
从kivy.uix.label导入标签kivy.uix.label导入标签uix.label导入标签kivy.uix.label导入标签
从kivy.uix.popup导入弹出窗口kivy.uix.popup导入弹出窗口uix.popup导入弹出窗口kivy.uix.popup导入弹出窗口
从基维。核心。窗子导入窗口kivy . core . windows导入窗口核心.窗口导入窗口kivy.core.window导入窗口
从基维。公制导入dp kivy .公制导入韵律学导入dp kivy.metrics导入

平铺= ['1万','2万','3万','4万','5万','6万','7万','8万','9万','1筒','2筒','3筒','4筒','5筒','6筒','7筒','8筒','9筒','1条','2条','3条','4条','5条','6条','7条','8条','9条','东','南','西','北','中','发','白',背景_正常1万','2万','3万','4万','5万','6万','7万','8万','9万','1筒','2筒','3筒','4筒','5筒','6筒','7筒','8筒','9筒','1条','2条','3条','4条','5条','6条','7条','8条','9条','东','南','西','北','中','发','白','红中']
套装= {}{}
对于瓷砖中的瓷砖中的t: t:
'如果'万in t: SUIT[t] = '万'如果'万in t: SUIT[t] = '万'
埃利夫筒in t: SUIT[t] = '筒埃利夫筒in t: SUIT[t] = '筒'
埃利夫条in t: SUIT[t] = '条埃利夫条in t: SUIT[t] = '条'
else: SUIT[t] = '字else: SUIT[t] = '字'

人工智能类:AI:
def _ _ init _ _(s):s . h =[]def _ _ init _ _(s):s . h =[]
最佳定义:最佳定义:
sc = {t: (100 if t== '红中else(30 if s . h . count(t)> = 2 else-10 if t in['东','南','西','北','中','发','白]else(20 if s . h . count(t)> = 2 else-15 if int(t[0])in[1，9]else(10 if any(f " { y } { SUIT[t]} " in s . h for y in range(max(1，int(t[0])-1)，min(10，int(t[0])+2))if f"{y}{SUIT[t]} "！= t)else-20))))for t in s . h } { t:(100 if t = = '红中else(30 if s . h . count(t)> = 2 else-10 if t in['东','南','西','北','中','发','白]else(20 if s . h . count(t)> = 2 else-15 if int(t[0])in[1，9]else(10 if any(f " { y } { SUIT[t]} " in s . h for y in range(max(1,int(t[0])-1),min(10,int(t[0])+2))if f"{y}{SUIT[t]}"!=t)else -20)))) for t in s.h}
return min(sc，key=sc.get)return min(sc，key=sc.get)
定义提示定义提示(s，t):
如果t== '红中：返回"赖子保留“如果t==”红中:返回"赖子保留"
如果适合' t]== '字：返回f"{ '对子如果s.h.count(t)>=2 else '孤立'}建议打“如果适合[t]==”字:返回f"{ '对子如果s.h.count(t)>=2 else '孤立'}建议打"
返回f"{ '幺九' if int(t[0])in[1，9]else '中张'}建议打" return f"{ '幺九' if int(t[0])in[1，9]else '中张'}建议打"

ai = AI()AI()

B类（按钮):B(按钮):
def __init__(s，t，**kw): super()._ _ init _ _(* * kw)；s . tile = t；s . text = t；s . font _ size = DP(14)；s.size_hint=(None，None)；s.width，s.height=dp(45)，DP(35)；s . background _ normal =背景颜色=(0.9，0.85，0.75，1)def __init__(s，t，**kw): super()。_ _ init _ _(* * kw)；s . tile = t；s . text = t；s . font _ size = DP(14)；s.size_hint=(None，None)；s.width，s.height=dp(45)，DP(35)；s . background _ normal =“”；背景颜色=(0.9，0.85，0.75，1)

铷类（按钮):RB(按钮):
奔跑

课堂应用程序(App): App(App):
def __init__(s): super()._ _ init _ _()；s . t =[]；s.b={}def __init__(s): super()。_ _ init _ _()；s . t =[]；s.b={}
定义版本:定义版本:
s.ti= '麻将AI’；Window.clearcolor=(0.1，0.1，0.15，1)ti= '麻将AI’；Window.clearcolor=(0.1，0.1，0.15，1)
L = BoxLayout(方向= '垂直,填充=dp(8)，间距=dp(5))BoxLayout(方向= '垂直'，填充=dp(8)，间距=dp(5))
L.add_widget(Label(text='🀄麻将人工智能助手,font_size=dp(22),size_hint_y=none,height=dp(40),color=(1,0.9,0.5,1)))add_widget(label(text='🀄麻将人工智能助手，font_size=dp(22)，size_hint_y=None，height=dp(40)，color=(1，0.9，0.5，1)))
L.add_widget(Label(text= '手牌（点击移除):'，font_size=dp(14)，size_hint_y=None，height=dp(25)，color=(0.8，0.8，0.8，1)))add_widget(Label(text= '手牌（点击移除):'，font_size=dp(14)，size_hint_y=None，height=dp(25)，color=(0.8，0.8，0.8，1)))
s。hs =滚动视图(size _ hint _ y = None，height = DP(45))；s.hl=BoxLayout(spacing=dp(3)，padding = DP(3))；圣罗兰。绑定(minimum _ width = s . HL。setter(' width '))；s . hs。add _ widget(s . HL)；L.add_widget(不锈钢)hs = ScrollView(size_hint_y=None，height = DP(45))；s.hl=BoxLayout(spacing=dp(3)，padding = DP(3))；s . HL . bind(minimum _ width = s . HL . setter(' width '))；s . hs . add _ widget(s . HL)；L.add_widget(不锈钢)
bl = BoxLayout(size_hint_y=None，height=dp(35)，spacing=dp(5))box layout(size _ hint _ y = None，height=dp(35)，spacing = DP(5))
bl.add_widget(Button(text= '清空，on _ press = s . clr))add _ widget(Button(text = '清空，on_press=s.clr))
bl.add_widget(Button(text= '🤖人工智能分析，on_press=s.an，background_color=(0.2，0.5，0.8，1)))add_widget(Button(text= '🤖人工智能分析，on_press=s.an，background_color=(0.2，0.5，0.8，1)))
插件插件插件插件
s.rl = Label(text= '选14张牌，font_size=dp(14)，size_hint_y=None，height=dp(60)，color=(1，1，1，1))rl = Label(text= '选14张牌，font_size=dp(14)，size_hint_y=None，height=dp(60)，color=(1，1，1，1))
L.add_widget(小号rl)添加部件(s.rl)
L.add_widget(Label(text='🃏选牌:',font_size=dp(14),size_hint_y=none,height=dp(25),color=(0.8,0.8,0.8,1)))add_widget(label(text='🃏选牌:'，font_size=dp(14)，size_hint_y=None，height=dp(25)，color=(0.8，0.8，0.8，1)))
SV =滚动视图()；gl=GridLayout(cols=10，spacing=dp(2)，padding = DP(2))；GL。bind(minimum _ height = GL。setter(' height '))scroll view()；gl=GridLayout(cols=10，spacing=dp(2)，padding = DP(2))；GL . bind(minimum _ height = GL . setter(' height '))
对于瓷砖中的t:B = B(t，on _ press = s . sel)；s . b[t]= b；TILES中t的GL . add _ widget(B):B = B(t，on _ press = s . sel)；s . b[t]= b；gl.add_widget(b)
SV。add _ widget(GL)；L.add_widget(服务)add _ widget(GL)；L.add_widget(服务)
返回Lreturn L
定义选择(s，b):定义选择(s，b):
如果len(s.t)>=14: s.pop('提示','14张已满!');返回如果len(s.t)>=14: s.pop('提示','14张已满!');返回
如果乙。瓷砖不在科学技术。中:s . t追加(b。平铺);s . upd()；背景颜色=(0.3,0.7,0.3,1)如果b .瓷砖不在s . t:s . t . append(b .平铺)；s . upd()；背景颜色=(0.3,0.7,0.3,1)
定义rm(s，b):
如果b .瓷砖在s . t:s . t . remove(b .平铺)；标准更新()如果b . tile在s . t:s . t . remove(b . tile)；标准更新()
如果乙。平铺在s . b .:s . b .平铺]。背景颜色=(0.9，0.85，0.75，1)if b.tile in s.b: s.b[b.tile].背景颜色=(0.9,0.85,0.75,1)
定义更新:定义更新:
s。HL。clear _ widgets()HL。clear _ widgets()
对于科学技术中的t: s.hl.add_widget(RB(t，s.rm))for t in s . t:s . HL add _ widget(RB(t，s . RM))
s.rl.text = f'{len(s.t)}/14 '+('✅已满如果len(s . t)= = 14 else”)rl。t)}/14'+('✅已满if len(s.t)==14 else ' ')
定义clr(s，_):def clr(s，_):
s。t =[]；[标准值()]中b的setattr(b，' background_color ')，(0.9，0.85，0.75，1))；s . upd()；s.rl.text= '已清空t =[]；[标准值()]中b的setattr(b，' background_color ')，(0.9，0.85，0.75，1))；s . upd()；s.rl.text= '已清空'
定义一个(s，_):定义一个(s，_):
if len(s.t)！=14: s.pop('提示，f'{len(s.t)}张不行');返回if len(s.t)！=14: s.pop('提示，f'{len(s.t)}张不行');返回
ai.h = s.th = s.t
b = ai.best()best()
s.rl.text = f "💡 建议打人工智能。提示(b)}”；颜色= (0.5，1，0.5，1)rl.text = f "💡 建议打人工智能。提示(b)}”；颜色= (0.5,1,0.5,1)
定义弹出(s，t，m):定义弹出(s，t，m):
c =框布局(orientation = ' vertical '，padding = DP(15))；c.add_widget(Label(text=m，font _ size = DP(16)))；c.add_widget(Button(text='OK '，size_hint_y=None，height=dp(40)，on _ press = lambda _:p . dissolve())框布局(orientation = ' vertical '，padding = DP(15))；c.add_widget(Label(text=m，font _ size = DP(16)))；c.add_widget(Button(text='OK '，size_hint_y=None，height=dp(40)，on _ press = lambda _:p . dissolve()))
p=Popup(title=t，content=c，size_hint=(0.8，0.35))；p.open()Popup(title=t，content=c，size_hint=(0.8，0.35))；p.open()

应用程序().奔跑().奔跑()
