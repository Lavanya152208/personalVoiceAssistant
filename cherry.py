import speech_recognition as sr
import pyttsx3
import datetime as dt
import wikipedia as wiki

listener = sr.Recognizer()
speaker = pyttsx3.init()

# RATE
rate = speaker.getProperty('rate')   # getting details of current speaking rate
print(rate)                          # printing current voice rate
speaker.setProperty('rate', 150)     # setting up new voice rate

def speak(text):

    speaker.say('yes boss ' + text)
    speaker.runAndWait()

def speak_ex(text):
    speaker.say(text)
    speaker.runAndWait()

name = 'cherry'

speak_ex('I am Your ' + name + ', Tell me boss')

def takeCommand():
    command = ''
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if name in command:
                command = command.replace(name + '', '')
    except:
        print("check your microphone")
    return command

while True:
    user_command = takeCommand()
    if 'close' in user_command:
        print('see you next time')
        speak('see you next time')
        break

    elif 'time' in user_command:
        time = dt.datetime.now().strftime("%I:%M:%p")
        print(time)
        speak(time)

    elif 'play' in user_command:
        try:
            import pywhatkit as pk
            user_command = user_command.replace('play ', '')
            print('playing ' + user_command)
            speak('playing ' + user_command)
            pk.playonyt(user_command)
            break
        except:
            speak_ex("Unable to connect to YouTube. Please check your internet connection.")

    elif 'search for' in user_command or 'google' in user_command:
        try:
            import pywhatkit as pk
            user_command = user_command.replace('search for', '')
            user_command = user_command.replace('google', '')
            speak('searching for ' + user_command)
            pk.search(user_command)
        except:
            speak_ex("Search failed. Please check your internet connection.")

    elif 'who is' in user_command:
        try:
            user_command = user_command.replace('who is', '')
            info = wiki.summary(user_command, 2)
            print(info)
            speak(info)
        except:
            speak_ex("Sorry, I couldn't find any information.")

    elif 'who are you' in user_command:
        speak_ex('I am Your ' + name + ', Tell me boss')

    else:
        speak_ex('please say that again')
