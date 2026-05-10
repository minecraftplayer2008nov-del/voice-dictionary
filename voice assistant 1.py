# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:18:49 2024

@author: singh
"""

import speech_recognition as sr

ArithmeticError
import pyttsx3
import wikipedia 
 

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            speak("please say clearly.")
            return ""
        except sr.RequestError:
            speak("say something; check your internet connection.")
            return ""

def fetch_answer(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.DisambiguationError as e:
        return f"Multiple results found for {query}. Please be more specific."
    except wikipedia.PageError:
        return f"No page found for {query}."
    except Exception as e:
        return "An error occurred while fetching the answer."

def main():
    speak("teri maki lund")
    while True:
        query = listen()
        if query.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye!")
            break
        answer = fetch_answer(query)
        speak(answer)

if __name__ == "__main__":
    main()
 
