import random
import time
import datetime

Agents = ["Martha", "Sarah","Dean","Alex","Joseph","Dylan", "Carlos", "Amelia", "Eden"] #This contains a list of Agents in the system
Stop_words = ["exit", "Exit", "Quit", "quit", "Bye", "bye", "Stop", "stop"] #This is a list of stop words which will terminate the program
Course_queries = ["what courses are available?", "What courses are available", "show me courses available"] #This is a list of keywords about course queries
Courses_available = ["Marketing", "IT in Business", "Cyber Security", "Sport Science", "Sport Coaching", "Basket Weaving", "Project Management", "Civil Engineering"] #This is a list of courses that are available
Campus_Cafe_Words = ["campus cafe", "Campus Cafe", "Poppies", "poppies", "is there a cafe on campus", "Is there a cafe on campus", "is there a cafe on campus?"]

def marketing_course():
    print(agent,">>> Here is the details about the Marketing Course we offer")
    print("************************")
    print("Course Tittle: Bsc Hons")
    print("Course Duration: 3 Years")
    print("Placement Year Available: Yes")
    print("Course Talks: 9:00am - 10:30am")
    print("************************")

def it_business_course():
    print(agent,">>> Here is the details about the IT in Business Course we offer")
    print("************************")
    print("Course Tittle: Bsc Hons")
    print("Course Duration: 3 Years")
    print("Placement Year Available: No")
    print("Course Talks: 14:00pm - 15:30pm")
    print("************************")

def cyber_security_course():
    print(agent,">>> Here is the details about the Cyber Security Course we offer")
    print("************************")
    print("Course Tittle: BEng Hons")
    print("Course Duration: 3 Years")
    print("Placement Year Available: Yes")
    print("Course Talks: 11:00am - 12:30pm")
    print("************************")

def sport_science_course():
    print(agent,">>> Here is the details about the Sport Science Course we offer")
    print("************************")
    print("Course Tittle: Bsc Hons")
    print("Course Duration: 3 Years")
    print("Placement Year Available: No")
    print("Course Talks: 12:30pm - 14:00pm")
    print("************************")

def sport_coaching_course():
    print(agent,">>> Here is the details about the Sport Coaching Course we offer")
    print("************************")
    print("Course Tittle: Bsc Hons")
    print("Course Duration: 3 Years")
    print("Placement Year Available: Yes")
    print("Course Talks: 09:00am - 10:30am")
    print("************************")

def basket_weaving_course():
    print(agent,">>> Here is the details about the Basket Weaving Course we offer")
    print("************************")
    print("Course Tittle: Bsc Hons")
    print("Course Duration: 2 Years")
    print("Placement Year Available: No")
    print("Course Talks: 11:00am - 12:30pm")
    print("************************")

def project_management_course():
    print(agent,">>> Here is the details about the Project Management Course we offer")
    print("************************")
    print("Course Tittle: BEng Hons")
    print("Course Duration: 3 Years")
    print("Placement Year Available: Yes")
    print("Course Talks: 13:45pm - 15:15pm")
    print("************************")

def civil_engineering_course():
    print(agent,">>> Here is the details about the Civil Engineering Course we offer")
    print("************************")
    print("Course Tittle: BEng Hons")
    print("Course Duration: 3 Years")
    print("Placement Year Available: Yes")
    print("Course Talks: 10:00am - 11:30am")
    print("************************")

def campus_cafe_info():
    print(agent,">>> The Campus Cafe, also known as poppies, serves a variety of coffe, tea and homemade smoothies. We are a big believer in recycling and doing our part for mother nature, We are open Monday - Saturday, 8am - 16:30pm everyday")
#This is the first part of the chatbot system which will display a welcome to the chatbot
print("****Welcome to the University of Poppleton Chatbot System!*****")
print("Current Time:", datetime.datetime.now())
username = input("SYSTEM >>> What is your name: ")
if username == "":
    username = "Stranger"
print("SYSTEM >>> Hello", username,", Good to meet you, give me one moment whilst you are connecting to an agent")

#This slows down the process to give the system a realistic feel
time.sleep(3.5)


agent = random.choice(Agents) #This assigns a random agent name from the Agents list
terminal = print("SYSTEM >>> Hello", username, ", Agent", agent, "is connected")
print(agent,">>>", "Hey there,", username,",Nice to meet you! What can I help you with?")


def main_screen(terminal): #This is the first screen the user will see
    terminal = input(">>> ")
    if terminal in Stop_words:
        print(agent,">>> Enjoy the rest of your day!")
        quit() #This code will stop the program when the user enters an exit word from the Stop_Words list
    if terminal == "":
        if username == "Stranger":
            print(agent,">>> Although I asked before, Im sure it would be better if I address you as your real name?")
            username = input(agent," >>> What is your name?: ")
        else:
            return main_screen(terminal)
    if terminal in Campus_Cafe_Words:
        campus_cafe_info()
        return main_screen(terminal)
    if terminal in Course_queries:
        print(agent,">>> Yes, The courses that are available this year are: ", Courses_available, "If you want more Information about a course type in the course tittle")
        if terminal in Courses_available:
            if terminal == "Marketing":
                marketing_course()
                return main_screen(terminal)
            if terminal == "IT in Business":
                it_business_course()
                return main_screen(terminal)
            if terminal == "Cyber Security":
                cyber_security_course()
                return main_screen(terminal)
            if terminal == "Sport Science":
                sport_science_course()
                return main_screen(terminal)
            if terminal == "Basket Weaving":
                basket_weaving_course()
                return main_screen(terminal)
            if terminal == "Project Management":
                project_management_course()
                return main_screen(terminal)
            if terminal == "Civil Engineering":
                civil_engineering_course()
                return main_screen(terminal)
        else:
            print(agent,">>> Im sorry I dont understand what your looking for, Maybe re-type the question again or in more detail and I can help more")
            return main_screen(terminal)

main_screen(terminal)





