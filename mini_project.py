import speech_recognition as sr
from win32com import client
import wikipedia
import os
import webbrowser

b = client.Dispatch('SAPI.SpVoice')
def user_input():
    a=sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now!!!")
        audio=a.listen(source)
        text=a.recognize_google(audio)
    return text
def task(op):
    if 'open' in op:
        search=op.split()[1]
        print(search)
        webbrowser.open('https://www.'+search+'.com')

        b.speak('Opening'+search)

    elif 'search' in op:
        search = op.split()[1:]
        ans = ' '.join(search)
        print(ans)
        data = wikipedia.summary(ans)
        print(data)
        b.speak('Searching for'+ans)
        b.speak(data)
    elif 'start' in op:
        search = op.split()[1]
        os.system('Start '+search)
        b.speak('Starting '+search)

    elif 'map' in op:
        search = op.split()[1]
        webbrowser.open('https://www.google.be/maps/place/'+search+'/')
        b.speak('Showing you'+search+'map')



text=user_input()
task(text)