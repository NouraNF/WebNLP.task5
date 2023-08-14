import speech_recognition as sr

# Create a recognizer instance
r = sr.Recognizer()

# Open a microphone stream
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Use the recognizer to recognize speech
try:
    text = r.recognize_google(audio)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Sorry, I could not understand your speech")
except sr.RequestError as e:
    print("Error occurred: {0}".format(e))