import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def listening():
    engine.say('I am K 1')
    engine.say('your assistant')
    engine.say('What can I do for you ?')
    engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        listening()
        with sr.Microphone() as source:
            print('listening...')
            voice = r.listen(source)
            command = r.recognize_google(voice)
            talk(command)
            print(command)

    except:
        pass
    return command


def run_jarvis(command_new):
    command = command_new
    if 'play' in command:
        print('playing...')
        talk('Playing')
        talk(command)

