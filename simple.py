import speech_recognition as sr 
import pyttsx3
from langdetect import detect
from googletrans import Translator

record = sr.Recognizer()
translator = Translator(service_urls=['translate.google.com'])
tts = pyttsx3.init()

while True:
    with sr.Microphone() as source:
        print("Escutando...")

        record.adjust_for_ambient_noise(source)
        audio = record.listen(source)

    try:
        text = record.recognize_google(audio)
        input_language = detect(text)

        if input_language == "pt-br":
            translation = translator.translate(text, dest='en')
            print("Tradução: {translation.text}")

            tts.say(translation.text)
            tts.runAndWait()

        else:
            print("Linguagem desconhecida")
    except sr.UnknownValueError:
        print("Error Google")
    except sr.RequestError as e:
        print("Network Error Service")
