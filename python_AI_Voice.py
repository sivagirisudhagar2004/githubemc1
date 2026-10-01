import pyttsx3
from datetime import datetime

engine = pyttsx3.init()
def speak(text):
    print("AI bot: ",text)
    engine.say(text)
    engine.runAndWait()

print("AI bot: Hello! I am your AI assistant. How can I help you today?\nYou can ask me about the current time, date, or even ask me to tell you a joke. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ").lower()
    if user_input.lower() in ["exit", "quit", "bye"]:
        speak("Goodbye! Have a great day!")
        break
    elif "time" in user_input.lower():
        current_time = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}.")
    elif "hello" in user_input.lower() or "hi" in user_input.lower():
        speak("Hello! How can I assist you today?")
    elif "how are you" in user_input.lower():
        speak("I'm just a program, but I'm functioning as expected! How can I help you?")
    elif "help" in user_input.lower():
        speak("I can provide you with the current time, date, and even tell you a joke! You can also ask me to perform calculations. What would you like to do?")
    elif "who are you" in user_input.lower():
        speak("I am your AI assistant. How can I help you today?")
    elif "what can you do" in user_input.lower():
        speak("I can provide you with the current time, date, and even tell you a joke! You can also ask me to perform calculations. What would you like to do?")
    elif "thank you" in user_input.lower() or "thanks" in user_input.lower():
        speak("You're welcome! If you have any more questions or need assistance, feel free to ask.")
    elif "goodbye" in user_input.lower() or "bye" in user_input.lower():
        speak("Goodbye! Have a great day!")
        break
    elif "web development" in user_input.lower():
        speak("Web development is the work involved in developing a website for the Internet or an intranet. It can range from developing a simple single static page to complex web applications, electronic businesses, and social network services.")
    elif "how to become a python developer" in user_input.lower():
        speak("To become a Python developer, you should start by learning the basics of Python programming. Practice coding regularly, work on projects, and consider contributing to open-source projects. Additionally, learning web frameworks like Django or Flask can be beneficial.")
    elif "name" in user_input.lower():
        speak("I am your AI assistant. I don't have a personal name, but you can call me whatever you like!")
    elif "date" in user_input.lower():
        current_date = datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}.")
    elif "could you tell about the django" in user_input.lower():
        speak("Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.")
    elif "weather" in user_input.lower():
        speak("I'm sorry, I cannot provide real-time weather updates. Please check a reliable weather service for the latest information.")
    elif "news" in user_input.lower():
        speak("I'm sorry, I cannot provide real-time news updates. Please check a reliable news source for the latest information.")
    elif"python developer" in user_input.lower():
        speak("A Python developer is a programmer who uses the Python programming language to build software applications.")
    elif "python" in user_input.lower():
        speak("Python is a high-level, interpreted programming language known for its simplicity and readability.")
    elif "calculator" in user_input.lower():
        speak("Sure! Please enter a mathematical expression (e.g., 2 + 2):")
        expression = input("You: ")
        try:
            result = eval(expression)
            speak(f"The result of {expression} is {result}.")
        except:
            speak("I'm sorry, I couldn't calculate that. Please try again.")
    elif "joke" in user_input.lower():
        speak("Why don't scientists trust atoms? Because they make up everything!")

    else:
        speak("I'm sorry, I didn't understand that. Can you please rephrase?")