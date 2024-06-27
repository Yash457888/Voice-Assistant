                                                 
                                                   # Project-1 [ VOICE ASSISTANT] , Level-1

import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
     speak("Good Morning")

    elif hour>=12 and hour<18:
       speak("Good Afternoon")

    else:
       speak("Good Evening")

    speak("I am Alexa mam. Please tell me how may i help you")  

def takecommand():
   # It takes microphone input from the user and returns strings output

   r = sr.Recognizer()
   with sr.Microphone()as source:
      print("Listening....")
      r.pause_threshold = 1
      audio = r.listen(source)

      try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
      except Exception as e:
        # print(e)
         print("Say that again please....")
         return "None"
      return query

if __name__=='__main__':
   wishme()
   while True:
      query = takecommand().lower()

      # Logic for executing tasks based on query.
      if 'wikipedia' in query:
         speak('Searching Wikipedia....')
         query = query.replace('wikipedia', "")
         results = wikipedia.summary(query, sentences=2)
         speak("According to wikipedia")
         print(results)
         speak(results)
        
      elif 'open youtube' in query:
         webbrowser.open('youtube.com')

      elif 'open google' in query:
         webbrowser.open('google.com')

      elif 'play music' in query:
         music_dir = "C:\\Users\\Hp\\Downloads\\Songs"   # Note : This songs file address is taken from my PC , you can copy and paste your own address
         songs = os.listdir(music_dir)                       # To fix the error use "\\" , so as interpreter can read the path of file.
         print(songs)
         os.startfile(os.path.join(music_dir, songs[1]))

      elif 'the time' in query:
         strTime = datetime.datetime.now().strftime('%H:%M:%S')
         speak(f"Mam, the time is {strTime}")

# Steps to execution of code :
# (1) For Time: Say ,Hey alexa what's the time
# (2) To open google or youtube : Say, Hey alexa open youtube / open google
# (3) To play music : Say, Hey alexa play music
# (4) To Gather information from Wikipedia :For example = Say ,Hey alexa Tell me about Virat Kohli from Wikepedia

                                                   
                                                           # THANK YOU
      
   
         
         

   
      


