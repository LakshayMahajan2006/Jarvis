import pyttsx3
import datetime 
import wikipedia
import webbrowser
import speech_recognition as sr
import os
import random
import smtplib
import psutil


engine = pyttsx3.init('sapi5') # this will have the speak API by Microsoft
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices',voices[0].id)
# This id is for the voices available in my pc.
print(voices[0].id)

#This function enables to speaks what ever you wish
def speak(audio):
    print(audio)
    engine.say(audio) # This will speak
    engine.runAndWait() 


# This will wish according to the time like afternoon, morning , evening.
def wishMe():
    hour = int(datetime.datetime.now().hour) 

    if (hour>=0 and hour<12):
        speak('good morning')

    elif (hour>=12 and hour<18):
        speak('good afternoon')

    else: 
         speak('good evening') 

    speak("HI I your Voice Assistant! How may I help you?")    

'''
This function take in the command 
Microphone i/p  and returns String output
'''    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognining...")    
        query = r.recognize_google(audio,language = 'en-in')
        print("User said ",query)

    except Exception:
        #print(e)   
        print("Say that again please") 
        return "None"   
    return query   


    '''
    This is to sent the email
'''      
def sendEmail(to,content):
    server = smtplib.SMTP('smtb gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('prernaverma200214@gmail.com','nptelcourse')
    server.sendmail('prernaverma200214@gmail.com',to,content)
    server.close()

'''
This function is for battery percentage of the laptop
'''
def battery():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = int(battery.percent)
    if(percent>75):
        speak(f"I am fine and is {percent} percent charged")
    else:
        plugged = "Plugged In" if plugged else "Not Plugged In"
        if plugged == "Plugged In":
            speak("I was not okay but now I am Plugged In")
        else:
            speak(f"I am not Okay as I am {percent} percent charged")    
        


if __name__ == "__main__":
    speak("HI Prerna")
    wishMe()

    while True:
        query = takeCommand().lower()

        '''
        Logic for executing commands based on query
        '''
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences =3)
            speak("According to wikipedia")
            speak(result)

        elif 'open youtube' in query:
            speak("Opening Youtube...")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("google.com") 

        elif 'play music' in query:
            speak("Playing Music...")
            music_dir = "D:\\Music"       
            somg = os.listdir(music_dir)
            print(somg)
            os.startfile(os.path.join(music_dir , somg[random.randint(0,len(somg))]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S %p")
            speak(f"Time is {strTime}") 

        elif 'open code' in query:
            code_path = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'send email' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "prernaverma200214@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry not able to send this email at this moment")

        elif 'how are you' in query:
            battery()

        elif 'quit' in query:
            speak("Quitting...")
            exit()
    speak("Nice speaking with you! Bye")
