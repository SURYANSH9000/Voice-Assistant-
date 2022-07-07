import datetime
# from itertools import count
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

eng = pyttsx3.init('sapi5')# To take voice
voices = eng.getProperty('voices')
eng.setProperty('voice',voices[0].id)

def speaking(audio):
    eng.say(audio)
    eng.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speaking("Good Morning ....Have a nice day")
    
    elif hour>=12 and hour<16:
        speaking("Good Afternoon")
    
    elif hour>=16 and hour<19:
        speaking("Good Evening")
    
    else:
        speaking("Good Night")
    
    speaking("Hello I am SG Assistant ! How may I Help you")

def takecommand():
    #takes input from speaking

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("ASG is listening!!!!!")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio,language='en-in')
        print("You Said",query)
    
    except Exception as e:        
        print("Please say it again")
        speaking("Please say it again")
        return "None"
    return query
    

if __name__ == "__main__":
    wishme()
    while True:        
        query = takecommand().lower()
        
        if 'wikipedia' in query:
            speaking("Going To Wikipedia")
            query = query.replace("wikipedia"," ")
            result = wikipedia.summary(query,sentences = 3)
            print(result)
            speaking("Wikipedia says")            
            speaking(result)
            0
        elif 'youtube' in query:
            speaking("Going to youtube")
            webbrowser.open("youtube.com")

        elif 'cricket score' in query:
            speaking("Showing cricket score")
            webbrowser.open("m.cricbuzz.com")

        elif 'google' in query:
            speaking("Going to google")
            webbrowser.open("https://www.google.com/")

        elif 'facebook' in query:
            speaking("Going to facebook")
            webbrowser.open("https://www.facebook.com/")
                    
        elif 'time' in query:
            speaking(datetime.datetime.now())
            print(datetime.datetime.now())
        
        elif 'vs code' in query:
            path = "C:\\Users\\Suryansh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
            speaking("opening vs code")

        elif 'gmail' in query:
            speaking("gping to gmail")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'who are you' in query:
            speaking("I am SG Assistant .... And I am created by Suryansh")
        
        elif 'exit' in query:
            speaking("Exiting .....Good Bye")
            print("Exiting .....Good Bye")
            exit()
        
        # elif 'camera' in query:

        


