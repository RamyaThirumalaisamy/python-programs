#import the modules
import speech_recognition as sr
import time
from datetime import datetime
from gtts import gTTS
import os
import webbrowser
r=sr.Recognizer()
def record_audio():
   with sr.Microphone()as source:
       audio=r.listen(source)
       text=''
       try:
           text=r.recognize_google(audio)
       except sr.UnknownValueError:
          print("unrecognizable")
       except sr.RequestError:
          print("no service")
       return text
def respond(text):
   if "what is your name" in text:
      ans="My name is Ramya"
      speech=gTTS(text=ans,lang="en",slow=False)
      speech.save("speech_audio.mp3")
      os.system("start speech_audio.mp3")
      
   if "tell me time" in text:
      t=time.localtime()
      current_time=time.strftime("%I hour %M minutes %p",t)
      ans=current_time
      speech=gTTS(text=ans,lang="en",slow=False)
      speech.save("speech_audio.mp3")
      os.system("start speech_audio.mp3")
   if "search" in text:
      ans="what do you want search for"
      speech=gTTS(text=ans,lang="en",slow=False)
      speech.save("speech_audio.mp3")
      os.system("start speech_audio.mp3")
      search=record_audio()
      url="https://google.com/search?q="+search
      webbrowser.get().open(url)
   if "open youtube" in text:
      ans="what do you want search for"
      speech=gTTS(text=ans,lang="en",slow=False)
      speech.save("speech_audio.mp3")
      os.system("start speech_audio.mp3")
      search=record_audio()
      url="https://www.youtube.com/results?search_query="+search
      webbrowser.get().open(url)
     
      
print("what do you want")
text=record_audio()
respond(text)
#print(text)
            
