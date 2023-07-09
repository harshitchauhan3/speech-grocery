import pyttsx3                      # Text to speech to use sapi
import speech_recognition as sr
import datetime
import os                      

engine = pyttsx3.init('sapi5')             #init function to get an engine instance for speech synthesis
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
            speak("Good Morning !")

    elif hour>= 12 and hour<18:
            speak("Good Afternoon !")

    else:
            speak("Good Evening !")

    asname =("Colexa")
    speak("I am your Assistant")
    speak(asname)

def username():
    speak("What should i call you ?")
    uname = takeCommand()
    speak("Welcome ")
    speak(uname)
    print("Welcome ", uname)
    
    speak("I am here to make a grocery list for you. You can add, reomve and update items on your grocery list")

def takeCommand():
	
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.record(source, duration =5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Sorry, I am unable to Recognize your voice.")
        return "None"
    
    return query

class item():
    # __init__ is known as the constructor
    def __init__(self, id_number, name, price, quantity):
        self.id_number = id_number
        self.name = name
        self.price = price
        self.quantity = quantity
	
class fruit(item):
    def __init__(self, id_number, name, price, quantity, fresh):
        self.fresh = fresh
        # invoking the __init__ of the parent class
        item.__init__(self, id_number, name, price, quantity)

class veges(item):
    def __init__(self, id_number, name, price, quantity, organic):
        self.organic = organic
        # invoking the __init__ of the parent class
        item.__init__(self, id_number, name, price, quantity)

market=[]
market.append(fruit(1,"apple", 200, 1.00, True))
market.append(fruit(2,"mango", 250, 1.00, True))
market.append(fruit(3,"banana", 120, 1.00, True))
market.append(fruit(4,"watermelon", 300, 1.00, True))
market.append(fruit(5,"oranges", 150, 1.00, True))
market.append(fruit(6,"grapes", 100, 1.00, True))
market.append(fruit(7,"papaya", 200, 1.00, True))
market.append(fruit(8,"dragon fruit", 500, 1.00, True))
market.append(fruit(9,"musk melon", 250, 1.00, True))

list=[]

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    # This Function will clean any command before execution of this python file
    clear()
    greet()
    username()

    while True:
      
        query = takeCommand().lower()

        if "add" in query:
            query=query.replace("add"," ")
            flag=0
            for obj in market:
                if obj.name in list:
                    print(obj.name)
                    print(obj.name + " already exists in list with quantity " + str(obj.quantity) +" kilgorams")
                    speak(obj.name + "already exists in list with quantity " + str(obj.quantity) +" kilgorams")
                    print("Try saying update if you wish to change quantity")
                    speak("Try saying update if you wish to change quantity")
                    flag=1
                else:
                    if obj.name in query:
                        list.append(obj)
                        speak("Please specify the quantity in kilograms")
                        t=0
                        while (t==0):
                            com=takeCommand()
                            if (com!="" or com!="None"):
                                obj.quantity=int(com)
                                print("Added "+ obj.name +" with quantity "+str(obj.quantity)+"kilograms")
                                speak("Added "+ obj.name +"with quantity "+str(obj.quantity)+"kilograms")
                                t=1
                                flag=1
                            else:
                                speak("Please try speaking again")
            if (flag==0):
                print("Could not find item in market")
                speak("Could not find item in market")

        elif "remove" in query:
            query=query.replace("remove"," ")
            flag=0
            if (len(list)>0):
                for obj in list:
                    if obj.name in query:
                        flag=1
                        print("Deleting " + obj.name + " from list")
                        speak("Deleting" + obj.name + " from list")
                        list.remove(obj)
                        speak("Removed successfully")
                if (flag==0):
                    speak("Item not found in list")
            else:
                print("The list is empty. Kindly try adding items")
                speak("The list is empty. Kindly try adding items")

        elif "update" in query:
            query=query.replace("update", " ")
            flag=0
            if (len(list)>0):
                for obj in list:
                    if obj.name in query:
                        speak("Please enter updated value of " + obj.name)
                        t=0
                        while (t==0):
                            com=takeCommand()
                            if (com!="" or com!="None"):
                                obj.quantity=int(com)
                                t=1
                                flag=1
                                print("Updated "+ obj.name +" to quantity "+str(obj.quantity)+"kilograms")
                                speak("Updated "+ obj.name +"to quantity "+str(obj.quantity)+"kilograms")
                            else:
                                speak("Please try speaking again")
                if (flag==0):
                    speak("Item not found in list")
            else:
                print("The list is empty")
                speak("The list is empty")

        elif "finalize" in query:
            speak("finalizing list in note")
            file = open('note.txt', 'w')
            file.write("\n")
            total=0
            for obj in list:
                sub_total=obj.price*obj.quantity
                file.write(f"{obj.name :>12}{obj.price :>12}{obj.quantity :>12}{sub_total :>12}")
                total+=sub_total
            file.write("Total amount to be paid = " + str(total))

        elif "show note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            file.close()
            
        elif query == 'none':
            continue
        
        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query:
            ex_exit = 'Thank you for using colexa. Have a great day.'
            speak(ex_exit)
            exit()
