import speech_recognition as sr
import pyttsx3
import musiclib
import webbrowser
import requests

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def openbrowser(c):
    try:
        if 'open google' in c.lower():
            webbrowser.open('https://google.com')
        elif c.lower().startswith("play"):
            parts = c.lower().split(" ")
            if len(parts) > 1:
                song = parts[1]
                link = musiclib.music.get(song)
                if link:
                    webbrowser.open(link)
                else:
                    speak("Song not found.")
            else:
                speak("Please specify a song to play.")
        elif 'news' in c.lower():
            response =requests.get("https://newsapi.org/v2/everything?q=tesla&from=2024-07-27&sortBy=publishedAt&apiKey=c38bf69149e0456d8de76b8b006b9545")
            data=response.json()
            # print(data)
            titles = [article['title'] for article in data['articles']]

            # Print the titles
            for title in titles:
                speak(title)

    except Exception as e:
        speak(f"An error occurred: {e}")

def main():
    speak("Initializing Jarvis....")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
                print("Recognizing...")
            word = r.recognize_google(audio).lower()
            if word == 'jarvis':
                speak('Yes Boss')
                print('Jarvis Active')
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source, timeout=3, phrase_time_limit=3)
                    print("Recognizing...")
                    word = r.recognize_google(audio).lower()
                    print(word)
                    openbrowser(word)
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Sorry, there was an error with the request; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()























# # import speech_recognition as sr
# import webbrowser
# # import pyttsx3

# # # r=sr.Recognizer()
# # engine=pyttsx3.init()

# # def speak(text):
# #     # with sr.Microphone() as S:
# #     #     print("Listioning")
# #     #     audio = r.listen(S)
# #     engine.say(text)
# #     engine.runAndWait()

# # # if __name__ == "__main__":
# # #     speak("I will speak this text")
# # if __name__ == "__main__":
# #     speak("Initializing Jarvis....")
# #     while True:
# #         # Listen for the wake word "Jarvis"
# #         # obtain audio from the microphone
# #         r = sr.Recognizer()
# #         # with sr.Microphone() as source:
# #         #     print("Listening...")
# #         #     audio = r.listen(source)
# #         #     print("recognizing...")
# #         # try:
# #         print("recognizing...")
# #         try:
# #             with sr.Microphone() as source:
# #                 print("Listening...")
# #                 audio = r.listen(source, timeout=1, phrase_time_limit=3)
            
# #                 word = r.recognize_google(audio)
# #             if(word.lower() == "jarvis"):
# #                 word = word.replace('jarvis', 'Yes Boss')
# #                 speak(word)
# #             else:
# #                 speak(word)
# #         except Exception as e:
# #             print("Error; ".format(e))









# import speech_recognition as sr
# import pyttsx3
# import musiclib

# r = sr.Recognizer()
# engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def openbrowser(c):
#     try:
#         if 'open google' in c.lower():
#             webbrowser.open('https://google.com')
#         elif c.lower().startswith("play"):
#             parts = c.lower().split(" ")
#             if len(parts) > 1:
#                 song = parts[1]
#                 link = musiclib.music[song]
#                 if link:
#                     webbrowser.open(link)
#                 else:
#                     speak("Song not found.")
#             else:
#                 speak("Please specify a song to play.")
#     except Exception as e:
#         speak(f"An error occurred: {e}")

# # def openbrowser(c):
# #     try:
# #         if 'open google' in c.lower():
# #             webbrowser.open('https://google.com')
# #         elif c.lower().startswith("play"):
# #             song = c.lower().split(" ")[1]
# #             link = musiclib.get(song)
# #             if link:
# #                 webbrowser.open(link)
# #             else:
# #                 speak("Song not found.")
# #     except Exception as e:
# #         print(f"An error occurred: {e}")

# # def openbrower(c):
# #     if 'open google' in c.lower():
# #         webbrowser.open('https://google.com')
# #     elif c.lower().startswith("play"):
# #         song = c.lower().split(" ")[1]
# #         link = musiclib.music[song]
# #         webbrowser.open(link)
#     # 'play' in c:
#     #     d= musiclib.music[0]
#     #     webbrowser.open(d)

# def main():
#     speak("Initializing Jarvis....")
#     while True:
#         try:
#             with sr.Microphone() as source:
#                 print("Listening...")
#                 audio = r.listen(source, timeout=3, phrase_time_limit=3)  # Adjusted timeout and phrase_time_limit
#                 print("Recognizing...")
#             word = r.recognize_google(audio)
#             word =word.lower()
#             if word.lower() == 'jarvis':
#                 speak('Yes Boss')
#                 print('Jarvis Active')
#                 with sr.Microphone() as source:
#                     print("Listening...")
#                     audio = r.listen(source, timeout=3, phrase_time_limit=3)  # Adjusted timeout and phrase_time_limit
#                     print("Recognizing...")
#                     word = r.recognize_google(audio)
#                     word =word.lower()
#                     print(word)
#                     openbrowser(word)
#                 # print(f"You said: {word}")
#                 # openbrowser(word)
#                 # Check if the word starts with "jarvis"
#                 # if word.lower() =='Jarvis':
#                 #     response = word.replace('Jarvis', 'yes boss')  # Remove 'jarvis' from the recognized text
#                 #     # response = "Yes Boss, " +response
#                 #     # if response else "Yes Boss"
#                 #     speak(response)
#                 # else:
#                 #     speak(word)

#         except sr.UnknownValueError:
#             print("Sorry, I did not understand that.")
#         except sr.RequestError as e:
#             print(f"Sorry, there was an error with the request; {e}")
#         except Exception as e:
#             print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     main()
