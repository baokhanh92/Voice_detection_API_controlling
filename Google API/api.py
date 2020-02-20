import speech_recognition as sr
import pygame
import time
from pynput import mouse


def recognize_speech_from_mic(recognizer, microphone):
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print('Speak')
        audio = recognizer.listen(source)
        print('Finish')

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

class Volume(object):
    def __init__(self):
        self.level = .5

    def increase(self, amount):
        self.level += amount
        print(f'New level is: {self.level}')

    def decrease(self, amount):
        self.level -= amount
        print(f'New level is: {self.level}')

def load_music():
    pygame.init()
    pygame.mixer.init()
    vol = Volume()
    pygame.mixer.music.load('music/song.mp3')
    pygame.mixer.music.set_volume(vol.level)
    pygame.mixer.music.play(-1)
# # #     pygame.mixer.music.set_pos(50)
    pygame.mixer.music.pause()
#     print('music is waiting')

load_music()

def onclick():
    state = ""
    def checkclick(x, y, button, pressed):
        nonlocal state
        if button == mouse.Button.left:
            state = 'yes'
            return False
        elif button == mouse.Button.right:
            state = 'quit'
            return False
    with mouse.Listener(on_click=checkclick) as listener:
        listener.join()
    return state

if __name__=="__main__":
    set_up = True
    vol = Volume()
    load_music()
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    time.sleep(4)
    command = ''
    action = ''
    c = 'say'
    while True:
        say = onclick()
        if say == 'yes':
            action = recognize_speech_from_mic(recognizer, microphone)['transcription']
            print(action)
            if action is None:
                continue
        elif say == 'quit':
            break

        if 'off' in action:
            try:
                command = 'pygame.mixer.music.pause()'
            except:
                set_up = False
                pass

        elif 'on' in action:
            try:
                command = 'pygame.mixer.music.play()'
            except ConnectionError:
                set_up = False
                pass

        elif 'down' in action:
            try:
                command = 'vol.decrease(0.5)'
                pygame.mixer.music.set_volume(vol.level)
            except ConnectionError:
                set_up = False
                pass

        elif 'up' in action:
            try:
                command = 'vol.increase(0.5)'
                pygame.mixer.music.set_volume(vol.level)
            except ConnectionError:
                set_up = False
                pass
        eval(command)

