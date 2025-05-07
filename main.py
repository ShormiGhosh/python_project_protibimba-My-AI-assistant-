import requests
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recog=sr.Recognizer()
engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 
engine.setProperty('rate', 150) 
API_KEY = "f82000820df5039630eed32e464d93d6"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
def get_weather(city):
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"  
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]
            weather_info = f"The current temperature in {city} is {temp} degrees Celsius with {description}. The humidity is {humidity} percent."
            return weather_info
        else:
            return f"Sorry, I couldn't fetch the weather for {city}. Please check the city name."
    except Exception as e:
        return f"An error occurred while fetching the weather: {str(e)}"


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram")
    elif "open twitter" in c.lower():
        webbrowser.open("https://www.twitter.com")
        speak("Opening Twitter")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")
        speak("Opening WhatsApp")
    elif "open codeforces" in c.lower():
        webbrowser.open("https://codeforces.com")
        speak("Opening Codeforces")
    elif c.lower().startswith("play"):
        song = c.lower().split("play")[-1].strip()
        if song in musicLibrary.playMusic:
            link = musicLibrary.playMusic[song]
            webbrowser.open(link)
            speak("Playing " + song)
        else:
            speak("Sorry, I couldn't find the song " + song)
    elif "weather" in c.lower():
        speak("Which city's weather would you like to know?")
        with sr.Microphone() as source:
            audio = recog.listen(source)
            city = recog.recognize_google(audio)
            speak(f"Fetching weather for {city}")
            weather_info = get_weather(city)
            speak(weather_info)
    else:
        speak("Sorry, I didn't understand that command.")
        
def speak(text):
    engine.say(text)
    engine.runAndWait()
if __name__ == "__main__":
    speak("Hello, I am Protibimba. How can I assist you today?")
while True:
    r=sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio=r.listen(source, timeout=4, phrase_time_limit=2)
        word=r.recognize_google(audio)
        print("You said: ",word)
        if "pratibimb" in word.lower():
            speak("Yeah")
            with sr.Microphone() as source:
                print("Protibimba active...")
                audio=r.listen(source)
                command=r.recognize_google(audio)

                processCommand(command)
            
    except Exception as e:
        print("Error: ", str(e))
        continue

