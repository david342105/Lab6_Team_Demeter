import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import requests
from bs4 import BeautifulSoup
import random

b = "Spartan: "
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# Set English voice
for voice in voices:
    if 'English' in voice.name:
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greetings():
    h = int(datetime.datetime.now().hour)
    if 8 < h < 12:
        print(b, 'Good Morning. My name is Spartan. Version 1.00')
        speak('Good morning. My name is Spartan. Version 1.00')
    elif 12 <= h < 17:
        print(b, "Good afternoon. My name is Spartan. Version 1.00")
        speak('Good afternoon. My name is Spartan. Version 1.00')
    else:
        print(b, 'Good evening! My name is Spartan. Version 1.00')
        speak('Good evening. My name is Spartan. Version 1.00')
    print(b, 'How can I help you, EE104?')
    speak('How can I help you, EE104?')

motiv = "Sometimes later becomes never. Do it now. EE104, I believe you, you have made me."
need_list = ['EE104, what can I do for you?', 'Do you want something else?', 'EE104, give me questions or tasks',
             'I want to take time with you, do you want to know something else?', 'EE104, what is on your mind?',
             'I can not think like you-humans, but can give answer your all questions',
             "Let's discover this world! What do you want to learn today?"]
sorry_list = ['EE104, I am sorry I dont know the answer', 'I dont have an idea about it, EE104', 'Sorry, EE104! try again']
bye_list = ['Good bye, EE104. I will miss you', 'See you EE104', 'Bye, dont forget I will always be here']
comic_list = ['It is not a joke, EE104. I was serious', 'Do you think that it is a joke? Be nice!']
greet_list = ['Hi EE104', 'Hi my dear']

def weather_Spartan(city):
    try:
        city = city.replace('weather', '')
        url = "https://www.google.com/search?q=" + "weather" + city
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')
        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
        data = str.split('\n')
        time_val = data[0]
        sky = data[1]
        listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
        strd = listdiv[5].text
        pos = strd.find('Wind')
        other_data = strd[pos:]

        print("At ", city)
        print("Temperature is", temp)
        print("Time: ", time_val)
        print("Sky Description: ", sky)
        print(other_data)
    except Exception as e:
        print(b, f"Error: {e}")
        sorry = random.choice(sorry_list)
        print(b, sorry)
        speak(sorry)

def takeCommand():
    while True:
        print(" ")
        query = input("EE104: ").lower()

        if 'who is' in query:
            try:
                query = query.replace('who is', '')
                result = wikipedia.summary(query, sentences=2)
                print(b, result)
                speak(result)
                need = random.choice(need_list)
                print(b, need)
                speak(need)
            except Exception as e:
                print(b, f"Error: {e}")
                sorry = random.choice(sorry_list)
                print(b, sorry)
                speak(sorry)

        elif 'what is' in query:
            try:
                query = query.replace('what is', '')
                result = wikipedia.summary(query, sentences=2)
                print(b, result)
                speak(result)
                need = random.choice(need_list)
                print(b, need)
                speak(need)
            except Exception as e:
                print(b, f"Error: {e}")
                sorry = random.choice(sorry_list)
                print(b, sorry)
                speak(sorry)

        elif 'weather' in query:
            weather_Spartan(query)
            need = random.choice(need_list)
            print(b, need)
            speak(need)

        elif 'play' in query:
            query = query.replace('play', '')
            url = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(url)
            time.sleep(2)
            speak('There are a lot of music, select one.')
            time.sleep(3)
            need = random.choice(need_list)
            print(b, need)
            speak(need)

        elif 'open' in query:
            try:
                website = query.split('open')[1].strip()
                url_dict = {
                    'github': 'https://github.com/',
                    'youtube': 'https://www.youtube.com/',
                    'google': 'https://www.google.com/',
                    'facebook': 'https://www.facebook.com/',
                    'sjsu': 'https://www.sjsu.edu/'
                }
                if website in url_dict:
                    webbrowser.open(url_dict[website])
                    print(b, f"Opening {website}...")
                    speak(f"Opening {website}")
                else:
                    print(b, "Sorry, I don't know this website.")
                    speak("Sorry, I don't know this website.")
                need = random.choice(need_list)
                print(b, need)
                speak(need)
            except Exception as e:
                print(b, f"Error: {e}")
                sorry = random.choice(sorry_list)
                print(b, sorry)
                speak(sorry)

        elif 'what time is it' in query:
            now = datetime.datetime.now().strftime('%H:%M:%S')
            print(b, f"The current time is {now}")
            speak(f"The current time is {now}")
            need = random.choice(need_list)
            print(b, need)
            speak(need)

        elif 'motivate' in query:
            print(b, motiv)
            speak(motiv)

        elif 'quote' in query:
            quote_list = [
                "The best way to predict the future is to invent it. — Alan Kay",
                "Life is 10% what happens to us and 90% how we react to it. — Charles Swindoll",
                "Your time is limited, don't waste it living someone else's life. — Steve Jobs",
                "The only way to do great work is to love what you do. — Steve Jobs",
                "Success is not final, failure is not fatal: It is the courage to continue that counts. — Winston Churchill"
            ]
            quote = random.choice(quote_list)
            print(b, quote)
            speak(quote)

        elif 'help' in query:
            help_text = """
Here are the commands you can use:
- who is [person]: Search Wikipedia information.
- what is [topic]: Search Wikipedia topic.
- weather [city]: Check the weather in a city.
- play [music]: Search music on YouTube.
- open [website]: Open GitHub, YouTube, Google, Facebook, or SJSU.
- what time is it: Tell the current time.
- motivate: Give a motivational quote.
- quote: Give a random inspirational quote.
- hello: Greeting from Spartan.
- bye / exit: Exit the program.
- haha: Funny reply.
- facebook: Open Facebook friend requests.
- shutdown laptop: Shutdown your computer (⚠️ Be careful!)
"""
            print(b, help_text)
            speak("Here are the commands you can use. Please read the terminal window.")

        elif 'hello' in query:
            greet = random.choice(greet_list)
            print(b, greet)
            speak(greet)

        elif 'haha' in query:
            comic = random.choice(comic_list)
            print(b, comic)
            speak(comic)

        elif 'facebook' in query:
            url2 = 'https://www.facebook.com/friends/requests/?fcref=jwl'
            webbrowser.open(url2)

        elif 'shutdown laptop' in query:
            os.system("shutdown /s /t 1")

        elif query == 'exit' or query == 'bye':
            bye = random.choice(bye_list)
            print(b, bye)
            speak(bye)
            break

        else:
            sorry = random.choice(sorry_list)
            print(b, sorry)
            speak(sorry)

time.sleep(2)
print('Initializing...')
time.sleep(2)
print('Spartan is preparing...')
time.sleep(2)
print('Environment is building...')
time.sleep(2)
greetings()
takeCommand()

