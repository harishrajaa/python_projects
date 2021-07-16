import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speak("i love you ")

def date():
    date = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    speak("date is")
    speak(date)
    speak("month is")
    speak(month)
    speak("year is")
    speak(year)

#date()

def wishme():
    speak("hello genius") 
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("Good morning ")
    elif hour>=12 and hour<=18:
        speak("Good afternoon ")
    elif hour>=18 and hour<=24:
        speak("Good evening ")
    else:
        speak("good night harysh, sweet dreams..")
    speak("deza at your service, how can i help you..")
    
#wishme()




def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("time is")
    speak(Time)

#time()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio =r.listen(source)
    try:
        print('Recognizing....')
        query = r.recognize_google(audio,language='en=US')
        print(query)
        #speak(query )
    except Exception as e:
        print(e)
        speak("i cant understand, say it again please...")
        return "None"
    return query

#takeCommand()

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("harishrajaa06112001@gmail.com", "**** **** **** ****") #here comes your password
    server.sendmail("harishrajaa06112001@gmail.com", to, content)
    server.quit()

#fuction to take screenshot
def screenshot():
    import pyautogui
    pyautogui.screenshot(r"C:\Users\dhavena harish\Desktop\vs-code projects\python proj\ss.png")
    #img = pyautogui.screenshot()
    #img.save(r"C:\Users\dhavena harish\Desktop\vs-code projects\python proj\ss.png")

#to get the information about cpu and battery
def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+ usage)
def battery():
    batry = psutil.sensors_battery()
    speak("battery percent is")
    speak(batry.percent)

#function for randon jokes
def jokes():
    speak(pyjokes.get_joke())

if __name__=="__main__":
    wishme()
    while(True):
        query = takeCommand().lower()
        print(query)

        if "date" in query:
            date()
        elif "thank you" in query:
            speak("most welcome harish")
        elif "time" in query:
            time()
        elif "wish me" in query:
            wishme()
        elif "love me" in query:
            speak("i love you")
        elif "bad words" in query:
            speak("podaang gotha")
        elif "offline" in query:
            speak("getting offline. take care. see yo")
            quit()
        elif "wikipedia" in query:
            speak("wait a second, searching for results...")
            query = query.replace("wikipedia", " ")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)
        elif "send mail" in query:
            try:
                speak("what do you wanna say?")
                content = takeCommand()
                to = "harishrajaa.m.2019.cse@rajalakshmi.edu.in"
                sendmail(to,content)
                speak("Email sent successfully")
                #speak("you wrote")
                #speak(content)
            except Exception as e:
                speak(e)
                print(e)
                speak("there's a problem in sending your mail. try again later")
        #command for opening chrome
        elif "search in chrome" in query:                                       #problem in this lines of code
            speak("what should i search?")
            chromepath = "C:\Program Files (x86)\Google\Chrome\\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        #commands to login and shutdown----not yet tested
        elif "logout" in query:
            os.system("shutdown -l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1") 
        elif "restart" in query:
            os.system("shutdown /r /t 1")

        #play songs
        elif "play songs" in query:
            songs_dir = r"F:\MUSIQ"
            songs = os.listdir(songs_dir)
            join = os.path.join(songs_dir, songs[8])
            os.startfile(join)
        #store what i say to remember
        elif "remember that" in query:
            speak("wht the hell i should remember?")
            data = takeCommand()
            speak("you said me to remember that"+data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()
        #remember wht stored on the file
        elif "do you have something to remind me" in query:
            remember = open("data.txt", "r")
            speak("you said me to remember that"+remember.read())
        
        #screenshot command -------not working :( -----problem fixed ;)
        elif "screenshot" in query:
            screenshot()
            speak("screen shot is taken successfully")
        
        #cpu and battery usage
        elif "cpu" in query:
            cpu()
        elif "battery" in query:
            battery()
        #tells a joke
        elif "joke" in query:
            jokes()

        

