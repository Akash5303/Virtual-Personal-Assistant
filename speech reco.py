import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser as wb
import os
from urllib.request import urlopen
engine = pyttsx3.init()
wolframalpha_app_id = 'app123'
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    def time_():
        Time=datetime.datetime.now().strftime("%H:%M:%S") #24 Hour Time
        speak("the current time is")
        speak(Time)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
def wishme_():

    #Greating
    
    speak("Hello mahak agarwal mam  !")

    hour = datetime.datetime.now().hour

    if 4 <= hour <= 12:
        speak("Good Morning mam!")
    elif 12 <= hour <=16:
        speak("Good afternoon mam!")
    elif 16 <= hour <=23:
        speak("Good evening mam!")
    else:
        speak("good night mam!")

    speak("I  am  Chotu and  HOW can help you ")

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio,language='en-US')
        print(query)

    except Exception as e:
        print(e)
        speak("Say That Again Please.....")
        return "None"
    
    return query
if __name__ == "__main__":
    
    wishme_()

    while True:
        query = TakeCommand().lower()

        #All commmand will be start in lower case in query
        #for easy recognition

        if 'whats time now' in query:  # tell us time when we ask
            time_()
        elif 'todays date' in query: # tell us date when we ask 
            date_()
        
        elif 'how are you' in query: 
            speak("Thankyou for Asking   I am fine mam!  I hope you are also fine ")
            print("I am fine sir")
        elif 'where are you' in query:
            speak("I live in cloud and only in your coumputer ")
            print("I am in your computer harddisk")
        
        elif 'who are you' in query:
            speak("i  am  Chotu  a virtiual assistant of mahak mam! ")
            print("I am  Chotu  a virtiual assistant look like alexa mam!")
        elif 'who is your developer' in query:
            speak('mahak aggarwal ')
            print("mahak mam")
        
        elif 'search in chrome' in query:
            speak("what whould I search")
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe  %s'
            # chromepath is location of installation of chrome in your computer 

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com') #only open .com website extension

        elif 'open youtube' in query:
            speak('What should I search ?')
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe  %s'
            search_Term = TakeCommand().lower()
            speak('Here we go to youtube')
            wb.get(chromepath).open_new_tab('https://www.youtube.com/results?search_query= '+search_Term)

        elif 'open google' in query:
            speak('what should I search ?')
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe  %s'
            search_Term = TakeCommand().lower()
            speak('Searching.....')
            wb.get(chromepath).open_new_tab('https://www.google.com/search?q='+search_Term)

        
        elif 'open excel' in query:
            speak("opening ms excel.......")
            excel = r'C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE'
            os.startfile(excel)

        
        
        elif 'open chrome' in query:
            speak("opening GOOgle chrome.......")
            chrome = r'C:/Program Files/Google/Chrome/Application/chrome.exe'
            os.startfile(chrome)

        elif 'open powerpoint' in query:
            speak("opening ms powerpoint.......")
            powerpoint = r'C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE'
            os.startfile(powerpoint)


        elif 'open word' in query:
            speak("opening ms word.......")
            word = r'C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE'
            os.startfile(word)

        elif 'thank you' in query:
            speak("your welcome mam!")

        else:
            speak("donot say thanks , its my work and your welcome mam!")
            