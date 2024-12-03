import random
import time
#The Agents list contains a list of names who are representing as Agents within the Chatbot system
Agents = ["Martha", "Sarah","Dean","Alex","Joseph","Dylan", "Carlos", "Amelia", "Eden"]

def Close_program(exit):
    if terminal == ["exit", "Exit", "Quit", "quit", "Bye", "bye", "Stop", "stop"]:
        quit()



#This is the first part of the chatbot system which will display a welcome to the chatbot
print("****Welcome to the University of Poppleton Chatbot System!*****")
username = input("What is your name: ")
print("Hello", username,", Good to meet you, give me one moment whilst you are connecting to an agent")

#This slows down the process to give the system a realistic feel
time.sleep(5)

#This assigns a random agent name from the Agents list
agent = random.choice(Agents)
terminal = print("Hello", username,", Agent", agent,"is connected")
print(agent,">>>", "Hey there,", username,",Nice to meet you, What can I help you with?")

terminal = input(">>> ")



