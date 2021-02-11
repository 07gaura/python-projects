import moviepy.editor
import speech_recognition as sr
from gtts import gTTS
from moviepy.editor import *
import os
from deep_translator import GoogleTranslator

video = moviepy.editor.VideoFileClip("test2.mkv")
audio1 = video.audio
audio1.write_audiofile("2.wav")

sound = "2.wav"
r = sr.Recognizer()
with sr.AudioFile(sound) as source:
    r.adjust_for_ambient_noise(source)
    print("converting audio file to text....")

    audio = r.listen(source)

    try:
        print("Converted Audio is: \n" + r.recognize_google(audio))
        textaud = r.recognize_google(audio)
    except Exception as e:
        print(e)


trans = GoogleTranslator(source='auto', target='hi').translate(textaud)

language = 'hi'
output = gTTS(text=trans, lang=language, slow=False)
output.save("output.mp3")
os.system("start output.mp3")
clip = VideoFileClip("test2.mkv")

audioclip = AudioFileClip('output.mp3')
videoclip = clip.set_audio(audioclip)
videoclip.write_videofile("testingvid.webm")

