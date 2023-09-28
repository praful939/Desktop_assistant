import pyttsx3 as tts #pip install pyttsx3 
import pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import yagmail
import pywhatkit as kit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate",185)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir . Please tell me how may i help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("Say that again please......")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results) 
       

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            hvg = 'C:\\Users\\prafu\Music\\music_dir'   
            songs = os.listdir(hvg)
            print(songs)    
            os.startfile(os.path.join(hvg, songs[0])) 
             
       


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "enter your PATH of vs code"
            os.startfile(codePath) 
        elif 'play video' in query:
            In = input("search for youtube vid:  ") 
            v = tts.init() 
            kit.playonyt(In)
            print("Playing" + In + "On youtube")
            v.say("Playing" + In + "On youtube") 
            v.runAndWait()

        elif 'email to me' in query:
            try: 
                rec = 'receiver_mail' 
                speak("What should I say?")
                info = takeCommand()
                sender =yagmail.SMTP('sender_mail')
                sender.send(to=rec,subject='dgyf ygdea0',contents=info)    
                
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send this email")    
