import librosa   #for audio processing
import IPython.display as ipd
import numpy as np
from scipy.io import wavfile#for audio
from scipy.io.wavfile import write
import sounddevice as sd
from keras.models import load_model
import pygame
import time
# from tensorflow import keras

model = load_model('models/CNN.h5')
# model = None

labels = ['up', 'off', 'right', 'left', 'down', 'on']
set_up = True

def record():
    fs = 16000  # Sample rate
    seconds = 1  # Duration of recording

    print('Start recording')
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('./voice/output.wav', fs, myrecording)  # Save as WAV file
    print('Done recording')
    
    return './voice/output.wav'

def predict_voice(sample, model=model):
    prob = model.predict(sample)
    pred = np.argmax(prob[0])
    print(f'predict: {pred}')
    label = labels[pred]
    score = float("%0.2f" % (prob[0][pred] * 100))
    print(label, score)
   
    return label, score

def process_voice(filename):
    sample, sample_rate = librosa.load(filename, sr=16000)
    sample = np.array(sample.reshape(1,16000,1))
    print(sample.size)
    
    return sample

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
    pygame.mixer.music.load('music/song.mp3')
#     pygame.mixer.music.set_volume(vol.level)
    pygame.mixer.music.play(-1)
#     pygame.mixer.music.set_pos(50)
    pygame.mixer.music.pause()
    print('music is waiting')


if __name__=="__main__":
    vol = Volume()
    load_music()

    while set_up:
        print('Do you want to start playing music?')
        command = str(input())
        
        if command == 'break': # press ESC to exit
            break
        
        elif command == 'predict':  
            raw_record = record() #recording and return filepath
            sample = process_voice(raw_record)
            action, score = predict_voice(sample)
            # action = str(input("What is action?"))

            if action == 'off':
                try:
                    pygame.mixer.music.pause()
                except:
                    set_up = False
                    pass

            elif action == 'on':
                try:
                    pygame.mixer.music.unpause()
                except ConnectionError:
                    set_up = False
                    pass

            elif action == 'down':
                try:
                    vol.decrease(0.2)
                    pygame.mixer.music.set_volume(vol.level)
                except ConnectionError:
                    set_up = False
                    pass

        elif action == 'up':
            try:
                vol.increase(0.2)
                pygame.mixer.music.set_volume(vol.level)
            except ConnectionError:
                set_up = False
                pass
        else:
            pass


