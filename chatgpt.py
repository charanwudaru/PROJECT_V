import speech_recognition as sr
import openai
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change voice index as needed

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Set your OpenAI API key here
api_key = "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"  # Replace with your actual API key

# Initialize the OpenAI API client
openai.api_key = api_key

# Initialize the speech recognizer
recognizer = sr.Recognizer()

def listen_for_voice():
    with sr.Microphone() as source:
        print("Listening for voice input...")
        audio = recognizer.listen(source)

    try:
        # Recognize the voice input using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand your voice.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150  # Adjust max_tokens for longer responses
        )
        return response.choices[0].message["content"]

    except Exception as e:
        print(f"Error generating response: {str(e)}")
        return "I encountered an error."

if __name__ == "__main__":
    while True:
        voice_input = listen_for_voice()

        if voice_input:
            response = generate_response(voice_input)
            print("ChatGPT:")
            print(response)
            speak(response[1:100])  # Speak the response
            with open("response.txt", "a") as file:
                file.write(response + "\n")  # Append the response to the file

