import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Hii Gaurav I am katrina kaif your personal assistance how can i help you ")
            talk("Hii Gaurav I am katrina kaif your personal assistance how can i help you ")
            voice = listener.listen(source)
            commands = listener.recognize_google(voice)
            commands = commands.lower()
            if 'katrina' in commands:
                print(commands)
                commands = commands.replace('katrina', '')
            else:
                take_command()
            return commands
    except:
        pass


def run_alexa():
    command = take_command()
    print(command)
    if 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('gaurav current time is' + time)
        print('gaurav current time is' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        print('playing' + song)
        pywhatkit.playonyt(song)
    elif 'search' in command:
        searches = command.replace('search', '')
        talk('searching for' + searches + 'on google')
        print('searching for' + searches + 'on google')
        pywhatkit.search(searches)
    elif 'who is' in command:
        wiki = command.replace('who is', '')
        info = wikipedia.summary(wiki, 1)
        print(wiki)
        talk(info)
    elif 'whatsapp message' in command:
        talk('tell me a whatsapp number')
        whatsappno = take_command()
        print(whatsappno)
        talk("tell me a message")
        msg = take_command()
        print(msg)
        pywhatkit.sendwhatmsg("+91" + whatsappno, msg, 15, 00)
        talk("message send successfully")
    elif 'who programmed you' in command:
        print("Gaurav Lokhande programmed me")
        talk("Gaurav Lokhande programmed me")
    elif 'are you single' in command:
        print('I like you but you are my best friend and i am in a relationship with your broadband name Jio Telecom')
        talk('I like you but you are my best friend and i am in a relationship with your broadband name Jio Telecom')
    elif 'joke' in command:
        jokes = pyjokes.get_jokes()
        talk(jokes)
        print(jokes)
    else:
        talk("please say it again")


while True:
    run_alexa()
