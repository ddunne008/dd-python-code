import random
import time


#The Agents list contains names of Agents in the system
Agents = ["Martha", "Sarah","Dean","Alex","Joseph","Dylan", "Carlos", "Amelia", "Eden"]
Stop_words = ["exit", "Exit", "Quit", "quit", "Bye", "bye", "Stop", "stop"]
Course_queries = ["what courses are available?", "What courses are available", "show me courses available"]
Courses_available = ["Marketing", "IT in Business", "Cyber Security", "Sport Science", "Sport Coaching", "Basket Weaving", "Project Management", "Civil Engineering"]

def Marketing(marketing):
    print("************************")
    print("Course Tittle: Bsc Hons")
    print("Course Duration: 3 Years")
    print("Placement Year Available: Yes")
    print("Course Talks: 9:00am - 10:30am")
    print("************************")

#This is the first part of the chatbot system which will display a welcome to the chatbot
print("****Welcome to the University of Poppleton Chatbot System!*****")
username = input("SYSTEM >>> What is your name: ")
if username == "":
    username = "Stranger"
print("SYSTEM >>> Hello", username,", Good to meet you, give me one moment whilst you are connecting to an agent")

#This slows down the process to give the system a realistic feel
time.sleep(3.5)

#This assigns a random agent name from the Agents list
agent = random.choice(Agents)
terminal = print("Hello", username,", Agent", agent,"is connected")
print(agent,">>>", "Hey there,", username,",Nice to meet you, What can I help you with?")


def main_screen(terminal):
    terminal = input(">>> ")
    if terminal in Stop_words:
        print(agent,">>> Enjoy the rest of your day!")
        quit()

if terminal in Course_queries:
    print(agent,">>> The courses that are available this year are: ", Courses_available)

else:
    print(agent,">>> Im sorry I dont understand what your looking for, Maybe re-type the question again or in more detail and I can help more")


main_screen()





