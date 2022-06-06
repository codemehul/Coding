#This is Python Automation Project which takes your basic voice inputs and show the results.
#Python modules used in this project are: smtplib, datetime, wikipedia, pyttsx3, speech_recognition, webbrowser, os
#Module speech_recognition is giving some py_audio module errors which i am not able to correct, if you can please contribute.

import smtplib
import datetime
from time import strftime
import wikipedia
import pyttsx3
import speech_recognition as sr 
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def takecommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
         print("Recognizing your voice...")
         query = r.recognize_google(audio, language='en-in')
         print(f"You Said :{query}\n")
    except Exception as e:
        print("Please can you say it once again..")
        return "None"
    return query

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Please let me know your query.")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendEmail(to, connect):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('','') # email and password from which email is sent
    server.sendmail('',to,connect) # email mentioned above
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if 'open wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia...")
            print(results)
            speak(results)
        
        if 'open notepad' in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
        
        elif 'open paint' in query:
            npath = "C:\\Windows\\System32\\mspaint.exe"
            os.startfile(npath)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'tell me the time ' in query:
            strtime = datetime.datetime.now(),strftime("%H:%M:%S")
            speak(f"Time is{strtime}")
        
        elif 'send email' in query:
            try:
                speak("What is the content for email?")
                content = takecommand()
                speak("What is the email id?")
                to = takecommand()
                sendEmail(to,content)
                speak("Email sent successfully :) ")
            except Exception as e:
                print(e)
                speak("I am unable to send the email... Please check and address the error mentioned")
