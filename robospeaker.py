import pyttsx3

print("Welcome to Robot speaker")

while(True):
    name = input("Enter Your Name: ")
    if(name == "q"):
        break
    command = pyttsx3.init()
    command.setProperty('rate', 150)
    command.say(name)
    command.runAndWait()
