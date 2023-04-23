
from kivy.app import App
from kivy.lang import Builder
from kivy.logger import LoggerHistory
from kivy.uix.label import Label
from threading import Thread

kv = """
<LogMessage>:
    size_hint_y: None
    height: self.texture_size[1]
    text_size: self.size
    halign: 'left'
    
BoxLayout:
    orientation: 'vertical'
    spacing: 5
    ScrollView:
        BoxLayout:
            padding: 5
            orientation: 'vertical'
            size_hint: 1, None
            size: self.minimum_size
            id: logs
            
    Button:
        text: 'Show Log'
        size_hint_y: None
        height: 48
        on_release: app.show_log()
"""


class LogMessage(Label):
    pass

class LoggerPlay(App):
    def build(self):
        Thread(target=self.start_flask).start()
        return Builder.load_string(kv)

    def show_log(self):
        messages = [m.message for m in LoggerHistory.history]
        for m in messages:
            self.root.ids.logs.add_widget(LogMessage(text=m))

    def start_flask(self):
        from vixsharefile import run_server

if __name__ == '__main__':
    LoggerPlay().run()
