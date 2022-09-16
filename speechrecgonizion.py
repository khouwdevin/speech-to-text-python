import speech_recognition as sr
import moviepy.editor as mp
import pyautogui, time
import os
import wave
import contextlib
import keyboard, sys

check = 0

#thinking write input so can use anywhere the video
#convert video file to audio
while check != 0:
    video_name = input('Please input the video name : ')
    audio_name = input('Please input the audio name :')
    #clip = mp.VideoFileClip(r"%s", file_name)
    if video_name == '99':
        exit()
    try:
        clip = mp.VideoFileClip(r"%s"%(video_name))
        clip.audio.write_audiofile(r"%s"%(audio_name))
        check = 1
    except:
        print("Directory wrong.")

#define the recognizer
r = sr.Recognizer()

#import audio file

#audio = sr.AudioFile(r"D:\AABinus\ZZZTry\converted.wav")

audio = sr.AudioFile(r'%s'%(audio_name))

#fname = r'D:\AABinus\ZZZTry\converted.wav'
fname = r'%s'%(audio_name)

with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)

os.system('cls')
print('Put your cursor in word document after press enter.')
input("Press enter if you're ready.")

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

print("Printing the convertion.")

for i in range(0, int(duration), 60):
#recognizer the speech from the audio file
    if (i+60) >= int(duration):
        j = int(duration) - i
        with audio as source:
            audio_file = r.record(source, duration=j, offset=i)
        result = r.recognize_google(audio_file, language='id') #export the recognized audio
        if keyboard.is_pressed('esc'):
            break
        pyautogui.typewrite(result) #thinking to export using pyautogui so
        pyautogui.typewrite(" ") #so can write directly in word
        break
    else:
        with audio as source:
            audio_file = r.record(source, duration=60, offset=i)
        result = r.recognize_google(audio_file, language='id') #export the recognized audio
        if keyboard.is_pressed('esc'):
            break
        pyautogui.typewrite(result) #thinking to export using pyautogui so
        pyautogui.typewrite(" ") #so can write directly in word
    
    #with open(r'D:\AABinus\ZZZTry\recognized.txt', mode='w') as file:
    #    file.write(result)
    #   print('\n')
    

os.system('cls')
print("\nWriting finish.")

#with open('recognized.txt',mode ='w') as file: 
#   file.write("Recognized Speech:") 
#   file.write("\n") 
#   file.write(result) 
#   print("ready!")