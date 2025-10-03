import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
import webbrowser
import time

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

# Speak function
def speak(text):
    print(f"Bot: {text}")
    engine.say(text)
    engine.runAndWait()

# Listen function
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio)
            print("You:", query)
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please repeat.")
            return ""
        except sr.RequestError:
            speak("Network error. Please check your connection.")
            return ""

# Respond function
def respond(command):
    if 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The current time is {current_time}")
        
    elif 'date' in command:
        today = datetime.datetime.now().strftime('%B %d, %Y')
        speak(f"Today's date is {today}")
        
    elif 'wikipedia' in command:
        speak("Sure! What should I search on Wikipedia?")
        topic = listen()
        if topic:
            try:
                result = wikipedia.summary(topic, sentences=2)
                speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f"Multiple results found. Can you be more specific?")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any page for that topic.")
                
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        speak(joke)
        
    elif 'open google' in command:
        speak("Opening Google...")
        webbrowser.open("https://www.google.com")
        
    elif 'open youtube' in command:
        speak("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")
        
    elif 'hello' in command or 'hi' in command:
        speak("Hello! How are you today?")
        
    elif 'calculate' in command:
        speak("What should I calculate?")
        expr = listen()
        try:
            result = eval(expr)
            speak(f"The result is {result}")
        except:
            speak("Sorry, I couldn't calculate that.")
            
    elif 'bye' in command or 'exit' in command:
        speak("Goodbye! Have a great day!")
        exit()
        
    else:
        speak("Sorry, I don't understand that yet.")

# Start assistant
speak("Hi! I am your voice assistant. How can I help you today?")

while True:
    user_input = listen()
    if user_input:
        respond(user_input)
        time.sleep(1)