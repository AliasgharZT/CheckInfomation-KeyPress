from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivymd.uix.list import OneLineListItem
from kivymd.toast import toast

Builder.load_file('style.kv')

class Style(MDAnchorLayout):
    # result=ObjectProperty()
    word=ObjectProperty()
    info=['ali','aliakbar','abbas','ahmad','alireza','ahmadreza']
    
    def search(self):
        if self.word.text=='' or self.word.text==' ':
            pass
        elif self.word.text in self.info:
            toast('\n<<< Found >>>\n')
        else:
            toast('\n<<< Not Found >>>\n')

class MainApp(MDApp):
    key=[]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_key_down=self.key_event)

    def build(self):
        self.theme_cls.theme_style='Dark'

        return Style()
    
    def key_event(self, *args):
        # print(args)
        # print(args[-2])
        # Style.result.add_widget(OneLineListItem(text='qq'))   ?}}}ERROR
# --------------------------------------
        # # for s2 in s:
        # #     for s2n in range(len(s2)):
        # #         if key==s2[s2n]:
        # #             t.add_widget(OneLineListItem(text=s2))
# ///////////////////////////////
        key=self.key 
        if args[-3]==42 and args[-4]==8 and len(key)!=0:
            key.pop()
        elif args[-2]!=None:
            key.append(args[-2])
        else:
             pass 
         #print(key)
        #toast(str(args[-3]))
        s=Style.info
        # print(s)
        t=self.root.ids.result
        t.clear_widgets()
        q=''
        for k in key:
            q+=k
        if q!='':
            toast(q)
        for s2 in s:
            if q in s2:
                t.add_widget(OneLineListItem(text=s2))

MainApp().run()
