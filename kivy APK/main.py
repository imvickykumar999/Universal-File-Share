
import kivy
kivy.require('1.11.1')

from kivy.app import App
from threading import Thread
from kivy.uix.textinput import TextInput

class MyApp(App):
    def build(self):
        Thread(target=self.start_flask).start()
        self.log_text = TextInput(multiline=True, text='Flask is listening either\n')

        self.log_text.insert_text('http://192.168.0.104:5000 or\nhttp://192.168.0.102:5000')
        return self.log_text

    def start_flask(self):
        from vixsharefile import run_server

if __name__ == '__main__':
    MyApp().run()
