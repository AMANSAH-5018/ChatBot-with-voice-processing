from openai import OpenAI
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests


recogizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "f4c15cd0f4824f3aa5039f0218e67165"


def speak(text):
    engine.say(text)
    engine.runAndWait()


def aiProcess(command):

    # The program is totally correct and workable just need api_key to run this
    # Due to security and confidential reason I have revoked my api_key
    # Revoked my api_key so program doesn't give output, you can replace ypor api_key to see the output of this program

    client = OpenAI(
        api_key="please place your api key here",
    )
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant named jarvis skilled in general taska like Alexa and google cloud.",
            },
            {"role": "user", "content": command},
        ],
    )

    return completion.choices[0].message.content


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" "[1])
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}"
        )
        if r.status_code == 200:

            # parses json data
            data = r.json()

            # extract he articles
            articles = data.get("articles", [])
            for article in articles:
                speak(article["title"])

        else:
            output = aiProcess(c)
            speak(output)


if __name__ == "__main__":
    speak("Initializing jarvis.....")

    while True:
        # listen for the wake word "jarvis"
        # obtain audi from the microphone
        r = sr.Recognizer()

        print("Recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yaa")
            # listen for command

            with sr.Microphone() as source:
                print("jarvis active.....")
                audio = r.listen(source)
                command = r.recognize_google(audio)

                processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
