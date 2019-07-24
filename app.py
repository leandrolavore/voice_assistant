from gtts import gTTS
import speech_recognition as sr
import webbrowser as wb
import smtplib as sm
import winsound
import pydub
import time
import os


def talking(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')

    sound = pydub.AudioSegment.from_mp3("audio.mp3")
    sound.export("audio.wav", format="wav")

    winsound.PlaySound('audio.wav', winsound.SND_ASYNC)


def my_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        talking('at your command')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        talking('you said '+command+'\n')


    except sr.UnknownValueError:
        command = ''

    return command


def assistant(command):

    if 'Google' in command:
        winsound.Beep(440, 300)
        internet()

    if 'YouTube' in command:
        winsound.Beep(440, 300)
        youtube()

    if 'email' in command:
        winsound.Beep(440, 300)
        email()

    if 'send email' in command:
        winsound.Beep(440, 300)
        send_email()

    if 'clean disc' in command:
        clean_disc()



# Operations for voice assistant to do################################################


def internet():
    chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    url = 'www.google.com'
    talking('opening google')
    wb.register('chrome', None, wb.BackgroundBrowser(chrome_path))
    wb.get('chrome').open(url)


def youtube():
    chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    url = 'www.youtube.com'
    talking('opening youtube')
    wb.register('chrome', None, wb.BackgroundBrowser(chrome_path))
    wb.get('chrome').open(url)


def email():
    chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    url = 'www.gmail.com'
    talking('your mailbox')
    wb.register('chrome', None, wb.BackgroundBrowser(chrome_path))
    wb.get('chrome').open(url)


def send_email():
    mail = sm.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(os.environ.get("MAIL"), os.environ.get("PASSWORD"))


    mail.close()
    talking('e-mail sent')

def clean_disc():
    os.popen("C:\\WINDOWS\\\system32\\cleanmgr.exe").read()
####################################################################
assistant(my_command())

while True:
    time.sleep(20)
    assistant(my_command())



