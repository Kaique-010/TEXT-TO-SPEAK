import pyttsx3


engine = pyttsx3.init()


voices = engine.getProperty('voices')


for index, voice in enumerate(voices):
    print(f"Voz {index}: {voice.name} - Idioma: {voice.languages}")

engine.setProperty('voice', voices[0].id) 

engine.say('Olá, como você está?')
engine.say('Hoje temos que vos apresentar a nossa nova ferramenta o text to speak')


engine.runAndWait()


