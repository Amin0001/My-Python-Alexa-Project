import pyjokes
import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import openai
command = "text"
openai.api_key = "Use you own API key"
model_engine = "text-davinci-003"


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                talk(command)
    except:
        pass
    return command
def run_alexa():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%m %p')
        talk("the current time is " + time)
        print(time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'are you there' in command:
        talk('yes boss')
    elif "joke" in command:
        word = pyjokes.get_joke()
        talk(word)
        print(word)
    elif "date" in command:
        talk('send me two thousand naira for transport')
    elif 'are you single' in command:
        talk("no i'm in love with wifi")
    elif 'who created you' in command:
        talk('i was created from different AI models and API by Aminu Lawal, and i will say he is a wonderful programmer')
    elif "what is" or "generate" or "write code" or "write a" in command:
        prompt = command
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = completion.choices[0].text
        print(response)
        talk(response)
    else:
        talk("say the command again")
while True:
    run_alexa()
