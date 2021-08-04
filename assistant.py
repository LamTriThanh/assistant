import pyttsx3
import datetime
#import webbrowser as wb 
import os 

n = pyttsx3.init()
voice=n.getProperty('voices')
n.setProperty('voice', voice[1].id)




def noi(audio):
    print("Cmon :" + audio) 
    n.say(audio)
    n.runAndWait()


time=datetime.datetime.now().strftime("%I:%M:%p")


def wc():
    hour=datetime.datetime.now().hour
    if hour >=6 and hour<=12:
        noi("good moring sir")
    elif hour >=12 and hour<=18:
        noi("good afternoon sir")
    elif hour >=18 and hour<=24:
        noi("good night sir")
    noi("what do you want ")

def username():

    username_file = open("name.txt", "w")

    username_file.write(input("input your name down here : \n"))

    username_file.close()

def read_name():
    with open(r"C:\Users\user0\Desktop\assittent\name.txt") as f :
        ai_re = f.readline() 

        print(noi(ai_re))



def main():
    while True:
        tin = input("cmon listen :")
#----------------------------------------------
        if  "hi" in tin:
            rb = "hi tin"
            print(noi(rb))
#----------------------------------------------
        elif "thoat".upper() in tin :
            break
#----------------------------------------------
        elif "what is your name" in tin:
            rb = "my name is Cmon"
            print(noi(rb))
#----------------------------------------------
        elif "time" in tin:
            rb = ("now is "+ time)
            print(noi(rb))
#----------------------------------------------
        elif "pygame" in tin:
            os.system('click_circle.py')
            rb = "open now"
            print(noi(rb))
#----------------------------------------------
        elif "save my name" in tin:
            rieng = username()
            print(rieng)
            print(noi("your name was save!"))
#----------------------------------------------
        elif "save my name" in tin:
            print(noi("your name is "))
            read =  read_name()
            print(read)

#----------------------------------------------
        else:
            rb = "erro"
            print(noi(rb))
            continue

#----------------------------------------------


if __name__  =="__main__":
    main()
#     read_name()
#    wc()