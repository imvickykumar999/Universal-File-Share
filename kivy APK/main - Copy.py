
import kivy
kivy.require('1.11.1')

from kivy.app import App
from threading import Thread
from kivy.uix.textinput import TextInput

import logging, re
import webbrowser

logger = logging.getLogger('werkzeug')
handler = logging.FileHandler('test.log')
logger.addHandler(handler)


class MyApp(App):
    def build(self):
        Thread(target=self.start_flask).start()
        self.log_text = TextInput(multiline=True, text='Flask listening on ...\n')

        with open('test.log', encoding='utf-8') as f:
            save = f.read()

        urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', save)[1] + ':5000'
        self.log_text.insert_text(f'{urls}\n')

        webbrowser.open(urls)
        return self.log_text


    def start_flask(self):
        from vixsharefile import run_server


if __name__ == '__main__':
    MyApp().run()
