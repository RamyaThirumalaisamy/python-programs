from gtts import gTTS
import os
#give file name as a string which file you want to convert text to speech
file=input()
f=open(file,"r")
text=f.read().replace("\n"," ")
language='en'
speech=gTTS(text=text,lang=language,slow=False)
speech.save("speech.mp3")
os.system("start speech.mp3")
        
