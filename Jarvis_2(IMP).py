import speech_recognition as sr
import webbrowser
import pyttsx3
import sounddevice as sd
import numpy as np

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def record_audio(duration=2, fs=16000):
    print("Listening...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    return sr.AudioData(audio.tobytes(), fs, 2)

# def processCommand(command):
#     print("Command:", command)
#     speak(f"You said {command}")
def processCommand(command):
    if "open google" in command.lower():
        webbrowser.open("http://google.com")
    elif "open facebook" in command.lower():
        webbrowser.open("http://facebook.com")
    elif "open youtube" in command.lower():
        webbrowser.open("http://youtube.com")
    elif "open linkedin" in command.lower():
        webbrowser.open("http://linkedin.com")
    else:
        speak("Command not recognized")
if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        try:
            print("Waiting for wake word...")
            audio = record_audio(duration=3)
            word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes")
                print("Jarvis active...")
                audio = record_audio(duration=3)
                command = recognizer.recognize_google(audio)
                processCommand(command)

        # except Exception as e:
        #     print("Error:", e)
        
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("API error:", e)
        except Exception as e:
            print("Other error:", e)
