import tkinter as tk
from tkinter import Canvas, Scrollbar, filedialog, Text, Button
import os
from tkinter.constants import RIGHT, Y

import speech_recognition as sr
import moviepy.editor as mp
import pyautogui, time
import wave
import contextlib
import keyboard, sys

filename = "\0"

root = tk.Tk()
root.title("Speech to Text")
root.configure(background="sky blue")

def addApp():
    filename = filedialog.askopenfilename(initialdir="D:", title="Select File",
    filetypes=(("mp4", "*.mp4"), ("all files", "*.*")))

    shortname = filename.split("/")

    file_label = tk.Label(frame, text=shortname[-1], bg="grey")
    file_label.pack()

def TexttoSpeech():
    if filename != "\0":
        check = 0

        #thinking write input so can use anywhere the video
        #convert video file to audio
        while check != 0:
            video_name = filename
            audio_name = filename
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
            

            #with open('recognized.txt',mode ='w') as file: 
            #   file.write("Recognized Speech:") 
            #   file.write("\n") 
            #   file.write(result) 
            #   print("ready!")

canvas = tk.Canvas(root, height=300, width=300, bg="sky blue")

scroll_y = Scrollbar(root)
scroll_y.pack(side=RIGHT, fill=Y)

canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.6, relheight=0.6, rely=0.1, relx=0.2)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Speech to Text", padx=10, pady=5, fg="white", bg="#263D42", command=TexttoSpeech)
runApps.pack()

root.mainloop()

