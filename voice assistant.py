import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user input
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't understand.")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""

# Say "Hello sir"
speak("Hello Samir sir I am your assistant")

# Listen for response
ste="l"
while ste.lower()=="l":
    response = listen()
    if response.lower()=="hello":
        break
if response.lower() == "hello":
    speak("How may I help you?")
    query = listen()

    if query:
        # Perform Google search
        search_url = "https://www.google.com/search?q=" + query.replace(" ", "+")
        webbrowser.open(search_url)
        speak("opening the google chrome")
        speak("Here are the search results for " + query)
        
        # Ask if there's anything else the user wants
        speak("Anything else, Samir sir?")
        next_query = listen()
        
        while next_query.lower() != "no":
            if next_query.lower() == "yes brother":
                speak("What else can I search for you?")
                query = listen()
                
                if query:
                    # Perform Google search
                    search_url = "https://www.google.com/search?q=" + query.replace(" ", "+")
                    print(query.replace(" ", "+"))
                    webbrowser.open(search_url)
                    speak("opening Google sir")
                    speak("Here are the search results for " + query)
                    
                    # Ask if there's anything else the user wants
                    speak("Anything else, sir?")
                    next_query = listen()
                else:
                    speak("Sorry, I didn't catch that. Anything else, sir?")
                    next_query = listen()
            else:
                speak("Sorry, I didn't catch that. Anything else, sir?")
                next_query = listen()
        
        speak("Goodbye sir, have a nice day!")
