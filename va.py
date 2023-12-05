# What is pyttsx3?
#   A python library that will help us to convert text to speech. In short, it is a text-to-speech library.
#   It works offline, and it is compatible with Python 2 as well as Python 3.
import pyttsx3 #pip install pyttsx3

import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

# What is sapi5?
#   Microsoft developed speech API.
#   Helps in synthesis and recognition of voice.
# What Is VoiceId?
#   Voice id helps us to select different voices.
#   voice[0].id = Male voice 
#   voice[1].id = Female voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your Assistant Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer() #Class to recognize voice command
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)

    # Error checking 
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
# What is smtplib?
    # Simple Mail Transfer Protocol (SMTP) is a protocol that allows us to send emails and route emails between mail servers. An instance method called sendmail is present in the SMTP module. This instance method allows us to send an email.  It takes 3 parameters:
        # The sender: Email address of the sender.
        # The receiver: T Email of the receiver.
        # The message: A string message which needs to be sent to one or more than one recipient
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ayodhya911@gmail.com', 'your-password')
    server.sendmail('ayodhya911@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "") #replace "wikipedia" with blank
            results = wikipedia.summary(query, sentences=2) #return 2 sentences from wikipedia
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        #pip install PyAudio (to play music)
        elif 'play music' in query:
            music_dir = "C:\\Users\\Sai Arya\\Downloads\\animal-ranbir-kapoor-entry-bgm-ranbir-kapoor-rashmika-m-anil-k-bobby-d-sandeep-vang-128-ytshorts.savetube.me.mp3"
            # songs = os.listdir(music_dir)
            # print(songs)    
            os.startfile(os.path.join(music_dir))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Sai Arya\\AppData\R\oaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codePath)

        elif 'email to arya' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ayodhya911@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend arya. I am not able to send this email")    
