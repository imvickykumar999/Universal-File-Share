
from kivy.app import App
from threading import Thread
from kivy.uix.textinput import TextInput
import socket, webbrowser, kivy
kivy.require('1.11.1')


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


class MyApp(App):
    def build(self):
        Thread(target=self.start_flask).start()
        self.log_text = TextInput(multiline=True, text='Flask is listening on ...\n')

        url = f'\nhttp://{get_ip_address()}:5000\n'
        webbrowser.open(url)

        self.log_text.insert_text(url)
        self.log_text.insert_text('\nPress Ctrl + C to exit.\n')
        return self.log_text

    def start_flask(self):
        from vixsharefile import run_server


if __name__ == '__main__':
    MyApp().run()
