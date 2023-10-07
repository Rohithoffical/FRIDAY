import pyttsx3
import speech_recognition as sr
import datetime
import os
import subprocess
import webbrowser as wb
import pyautogui
import wikipedia
import pyjokes
from time import sleep
import pywhatkit

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
voicespeed = 160
engine.setProperty('rate', voicespeed)
chrome_path = '"C:/Program Files/Google/Chrome/Application/chrome.exe" %s'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-us')
    except Exception as e:
        print(e)
        print("Please tell me again")
        query = "none"
    return query


def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)
    print(time)


def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    #print(date:month:year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)


def wishme():
    print("welcome back sir")
    speak("welcome back sir")

    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        print("Good morning")
        speak("Good morning")
    elif hour > 12 and hour < 16:
        print("Good afternoon")
        speak("Good afternoon")
    elif hour >= 16 and hour < 20:
        print("Good evening")
        speak("Good evening")
    else:
        print("Good night")
        speak("Good night")

    print("how can i help u?")
    speak("how can i help u?")


if __name__ == "__main__":
    wishme()

    # wishme()
    while True:
        query = takecommand().lower()
        print(query)

        if "time" in query:
            time()

        if "date" in query:
            date()

        # Open chrome/Website
        elif "open chrome" in query:
            open_chrome()

        # Wikipedia search
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
            print(result)

        elif 'play' in query:
            playQuery = query.replace('play','')
            speak("Playing" + playQuery)
            pywhatkit.playonyt(playQuery)

        # Chrome search
        elif "search" in query:
            speak("what should i search?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # location
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")


        # Launch applications
        elif "open notepad" in query:  # if open notepad in statement
            speak("opening notepad")  # speak
            location = "C:/WINDOWS/system32/notepad.exe"  # location
            notepad = subprocess.Popen(location)  # location of a software you want tot opem

        elif 'type' in query:
            speak("Please tell me what should i write")
            while True:
                typeQuery = takeCommand()
                if typeQuery == "exit typing":
                    speak("Done sir")
                    break
                else:
                    pyautogui.write(typeQuery)

        elif "close notepad" in query:
            speak("closing notepad")
            notepad.terminate()

        elif 'open firefox' in query:
            speak("Opening firefox ")
            print("Opening firefox ")
            os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

        elif 'open opera' in query:
            speak("Opening opera ")
            print("Opening opera ")
            os.startfile("C:\\Users\\rohit\\AppData\\Local\\Programs\\Opera GX\\launcher.exe")

        elif 'open brave' in query:
            speak("Opening brave")
            print("Opening brave")
            os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")

        elif 'open telegram' in query:
            speak("Opening telegram")
            print("Opening telegram")
            os.startfile("C:\\Users\\rohit\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")


        # Random jokes
        elif 'joke' in query:
            Joke = pyjokes.get_joke()
            print(Joke)
            speak(Joke)

        # Logout / Shutdown / Restart
        elif "logout" in query:
            speak('logging out in 5 second')
            sleep(5)
            os.system("shutdown - l")

        elif "shutdown" in query:
            speak('shutting down in 5 second')
            sleep(5)
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            speak('initiating restart in 5 second')
            sleep(5)
            os.system("shutdown /r /t 1")


        elif "hidden menu" in query:
            # Win+X: Open the hidden menu
            pyautogui.hotkey('winleft', 'x')

        elif "task manager" in query:
            # Ctrl+Shift+Esc: Open the Task Manager
            pyautogui.hotkey('ctrl', 'shift', 'esc')

        elif "task view" in query:
            # Win+Tab: Open the Task view
            pyautogui.hotkey('winleft', 'tab')

        elif "take screenshot" in query:
            # win+perscr
            pyautogui.hotkey('winleft', 'prtscr')
            speak("done")

            # Take screenshot save in Given location
            
        elif "take screenshot" in query:
            img = pyautogui.screenshot()
            img.save("D:/screenshot_1.png")  # file mane and location
            speak("Done")
            

        elif "snip" in query:
            pyautogui.hotkey('winleft', 'shift', 's')

        elif "close this app" in query:
            # alt + f4: close this app
            pyautogui.hotkey('alt', 'f4')

        elif "setting" in query:
            # win+i = open setting
            pyautogui.hotkey('winleft', 'i')

        elif "new virtual desktop" in query:
            # Win+Ctrl+D: Add a new virtual desktop
            pyautogui.hotkey('winleft', 'ctrl', 'd')

        elif "stop" in query:
            print("bye sir come back as soon as possible")
            speak("bye sir come back as soon as possible")
            break
