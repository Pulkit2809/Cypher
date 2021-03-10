# pip install pyttsx3
import webbrowser as wb
import json
import requests
import wolframalpha
from urllib.request import urlopen
import datetime
import getpass
import os
import psutil
import pyautogui
import pyjokes
import pyttsx3
import random
import smtplib
import time
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init()

name = getpass.getuser()
wolframalpha_appID = 'AXYWP9-Y8T27X7WXY'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time_():
    time = datetime.datetime.now().strftime("%H:%M:%S")  # for 24-hour clock
    speak('the current time is')
    speak(time)


def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak('the current date is')
    speak(date)
    speak(month)
    speak(year)


def wishme(name):
    speak("Welcome" + ',' + name)
    time_()
    date_()

    hour = datetime.datetime.now().hour

    if 6 <= hour < 12:
        speak('Good Morning Boss!')
    elif 12 <= hour < 18:
        speak('Good Afternoon Boss!')
    elif 18 <= hour < 20:
        speak('Good Evening Boss')
    else:
        speak('Have a great Night Boss!')

    speak('CYPHER at your service today. How may I help you?')


def TakeCommand():
    inp = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Yes Boss, I'm Listening.")
        inp.adjust_for_ambient_noise(mic, duration=2)
        # inp.pause_threshold = 2
        speech = inp.listen(mic)

    try:
        print("Identifying")
        query = inp.recognize_google(speech)
        print(query)

    except Exception as E:
        print(E)
        print("Sorry, I didn't get you. Please say again.")
        return None
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # for this function to work, security on gmail account should be low

    server.login('AlphaXK9@gmail.com', 'gamingchannel09')
    server.sendmail('pulkitagarwal2899@gmail.com', to, content)
    server.close()


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU Usage is at ' + usage)

    battery = str(psutil.sensors_battery())
    speak('Battery is at')
    speak(battery)


def joke():
    speak(pyjokes.get_joke())


def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/pulki/OneDrive/Pictures')


if __name__ == '__main__':

    # query = TakeCommand().lower()
    # if 'initiate cypher' in query:

    wishme(name)

    while True:
        query = TakeCommand().lower()  # all commands are stored in lower case for easy recognition
        if 'time' in query:
            time_()
        if 'date' in query:
            date_()
        elif 'wikipedia' in query:
            speak('Searching')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=4)
            speak('According to Wikipedia')
            print(result)
            speak(result)
        elif 'send mail' in query:
            try:
                speak('what should i say?')
                content = TakeCommand()
                speak('Who should I send it to?')
                receiver = input("enter receiver email address : ")
                to = receiver
                sendEmail(to, content)
                speak(content)
                speak('email sent')
            except Exception as E:
                print(E)
                speak('Unable to send email')

        elif 'search in chrome' in query:
            speak('which site should i search?')
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            # location of chrome installation

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')  # only open websites with .com domain

        elif 'search youtube' in query:
            speak('which video should i search?')
            search_Term = TakeCommand().lower()
            speak('Launching Youtube right away Boss.')
            wb.open('https://www.youtube.com/results?search_query=' + search_Term)

        elif 'search google' in query:
            speak('what should i search?')
            search_Term = TakeCommand().lower()
            speak('Launching Google right away Boss.')
            wb.open('https://www.google.com/search?q=' + search_Term)

        elif 'usage' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'offline' in query:
            speak('Going Offline Boss.')
            quit()

        elif 'open chrome' in query:
            speak('Launching Chrome')
            path = r'C:/Program Files/Google/Chrome/Application/chrome.exe'
            os.startfile(path)

        elif 'write a note' in query:
            speak('What should i note?')
            notes = TakeCommand()
            file = open('notes.txt', 'w')
            speak('Boss, should I include Date and Time?')
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime('%H:%M:%S')
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                # strDate = datetime.datetime
                speak('Noted down Boss')
            else:
                file.write(notes)

        elif 'show note' in query:
            speak('Showing Notes Boss')
            file = open('notes.txt', 'r')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query:
            speak('Taking a screenshot')
            screenshot()

        elif 'play music' in query:
            video = 'C:/SONGS'
            # audio1 = 'C:/NOKIA/Received'
            # songs_dir = ''
            # songs = ()
            # speak('what should i play? audio or video')
            # speak('which song should i play?')
            # ans = (TakeCommand().lower())
            # while ans != 'audio' and ans != 'video':
            # speak("No song found. Please Try again.")
            # ans = (TakeCommand().lower())

            # if 'audio' in ans:
            # songs_dir = audio1
            # songs = os.listdir(songs_dir)
            # print(songs)

            # elif 'video' in ans:
            songs_dir = video
            ans = ''
            no = 0
            songs = os.listdir(songs_dir)
            print(songs)

            speak('Which song do you want to listen?')
            speak('select a number')
            # rand = (TakeCommand().lower())

            # while 'number' not in rand and rand != 'random':
            # speak("No song found. Please Try again.")
            # rand = (TakeCommand().lower())
            # if 'number' in rand:
            #    rand = int(rand.replace("number ", ""))
            #    os.startfile(os.path.join(songs_dir, songs[rand]))
            #    continue

            # elif 'random' in rand:
            #    rand = random.randint(1, 219)
            #    os.startfile(os.path.join(songs_dir, songs[rand]))
            #    continue
            while ('number' not in ans and ans != 'random' and ans != 'you choose'):
                speak("I couldn't get you. Please try again")
                ans = TakeCommand().lower()

            if 'number' in ans:
                no = int(ans.replace('number', ''))

            if 'random' or 'choose yourself' in ans:
                no = random.randint(1, 100)

            os.startfile(os.path.join(songs_dir, songs[no]))

        elif 'remember that' in query:
            speak('What do you want me to remember?')
            memory = TakeCommand()
            speak('You have asked me to remember that ' + memory)
            remember = open('memory.txt', 'w')
            remember.write(memory)
            remember.close()

        elif 'do you remember' in query:
            remember = open('memory.txt', 'r')
            speak('You asked me to remember that ' + remember.read())

        elif 'news' in query:
            try:
                jsonObj = urlopen(
                    "http://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=5b81e34cc51349ffa6d28a864594ccf1")
                data = json.load(jsonObj)
                i = 1
                speak("Here are the top articles")
                print("====Top Articles====" + '\n')
                for items in data['articles']:
                    print(str(i) + '.' + items['title'] + '\n')
                    print(items['description'] + '\n')
                    speak(items['title'])
                    i += 1
            except Exception as E:
                print(str(E))


        elif 'where is' in query:
            query = query.replace("where is", '')
            location = query
            speak("You asked me to locate " + location)
            wb.open_new_tab("https://www.google.com/maps/place/" + location)

        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_appID)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print('The Answer is ' + answer)
            speak('The Answer is ' + answer)

        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_appID)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                speak('No results found.')

        elif 'stop listening' in query:
            speak('For how long should i stop listening?')
            ans = int(TakeCommand())
            time.sleep(ans)
            print(ans)
            speak('I am back online')

        elif 'log out' in query:
            os.system("shutdown -l")

        elif 'restart' in query:
            os.system("shutdown /r /t 10")

        elif 'shut down' in query:
            os.system("shutdown /l /t 10")
