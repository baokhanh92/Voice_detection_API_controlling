import librosa   #for audio processing
import numpy as np
from scipy.io import wavfile#for audio
from scipy.io.wavfile import write
import sounddevice as sd
import soundfile as sf
import time
import os
import pathlib

fs = 44100  # Sample rate
seconds = 1  # Duration of recording
label = 'down'
count = 11
dir_ = './voice/'+ label + '/'
print(dir_)

if not os.path.exists(dir_):
    os.makedirs(dir_)
    
while count <= 20:
#     open_, fs = sf.read('./voice/open.wav', dtype='float32')
#     sd.play(open_, fs)
#     status = sd.wait(seconds)
    i = 0
    filename = dir_ + str(count)

    while i < 3:
        i += 1
        print(i)
        time.sleep(1)
        
    print('Starting recording')
    myarray= sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()

    write( filename, fs, myarray)  # Save as WAV file 
    print('Done')
    print(filename)

#     close_, fs = sf.read('./voice/close.wav', dtype='float32')
#     sd.play(close_, fs)
#     status = sd.wait(seconds)


#     print(filename)
    # Extract data and sampling rate from file
#     data, fs = sf.read(filename, dtype='float32') 
#     sd.play(data, fs)
#     status = sd.wait(seconds)  # Wait until file is done playing

#     sample, sample_rate = librosa.load(filename, sr=8000)

#     sample = librosa.resample(sample, sample_rate, 8000)
    
    count += 1
    time.sleep(2)

#     sd.play(sample, sample_rate)
#     status = sd.wait(seconds)
#     from keras.models import load_model

# model = load_model('./models/speech.h5')

# labels=['unknown', "yes", "no", "up", "down", "left", "right", "on", "off", "stop", "go"]

# def process_voice(filename, rate=1600):
#     sample, sample_rate = librosa.load(filename, sr=16000)
#     sample = librosa.resample(sample, sample_rate, 8000)
#     print(sample_rate, sample.size)
#     return sample

# def predict_voice(sample):
#     test = sample.reshape(1,len(sample),1)
#     prob = model.predict(test)
#     index = np.argmax(prob[0])
#     score = float("%0.2f" % (max(prob[0]) * 100))
#     print(labels[index])
   
#     return labels[index], score
# class Volume(object):
#     def __init__(self):
#         self.level = .5

#     def increase(self, amount):
#         self.level += amount
#         print(f'New level is: {self.level}')

#     def decrease(self, amount):
#         self.level -= amount
#         print(f'New level is: {self.level}')

# vol = Volume()

# prediction = ''
# action = ''
# score = 0
# system_control = True

# print('Ready to play')
# pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load('song.mp3')
# pygame.mixer.music.set_volume(vol.level)
# pygame.mixer.music.play()
# #     pygame.mixer.music.set_pos(50)
# # pygame.mixer.music.pause()
# while pygame.mixer.music.get_busy(): 
#     pygame.time.Clock().tick(10)
    
# k = cv2.waitKey(10)

# # if k == 32:     # If space bar pressed
# sample = process_voice(filename, rate=1600)
# prediction, score = predict_voice(sample)
# if system_control == True:
#     if prediction == 'off':
#         try:
#             action = "Music on"
#             pygame.mixer.music.unpause()
#             while pygame.mixer.music.get_busy(): 
#                 pygame.time.Clock().tick(10)
#         except ConnectionError:
#             system_control = False
#             pass

#     elif prediction == 'on':
#         try:
#             action = 'Music off'
#             pygame.mixer.music.pause()
#         except ConnectionError:
#             system_control = False
#             pass

#     elif prediction == 'down':
#         try:
#             action = 'Volume down'
#             vol.decrease(0.2)
#             pygame.mixer.music.set_volume(vol.level)
#         except ConnectionError:
#             system_control = False
#             pass

#     elif prediction == 'Okay':
#         try:
#             action = 'Volume up'
#             vol.increase(0.2)
#             pygame.mixer.music.set_volume(vol.level)
#         except ConnectionError:
#             system_control = False
#             pass

#     elif prediction == 'unknown':
#         try:
#             action = ''
#         except ConnectionError:
#             smart_home = False
#             pass

#     else:
#         pass

