import time
import random


print("                        _      ___  _           _ _               ")
print("                       (_)    / _ \| |         | | |              ")
print("  _ __ ___   __ _  __ _ _  __| (_) | |__   __ _| | |  _ __  _   _ ")
print(" | '_ ` _ \ / _` |/ _` | |/ __> _ <| '_ \ / _` | | | | '_ \| | | |")
print(" | | | | | | (_| | (_| | | (_| (_) | |_) | (_| | | |_| |_) | |_| |")
print(" |_| |_| |_|\__,_|\__, |_|\___\___/|_.__/ \__,_|_|_(_) .__/ \__, |")
print("                   __/ |                             | |     __/ |")
print("                  |___/                              |_|    |___/")

input("Ask the Magic 8 Ball something: ")

def shake():
    
    for x in range(1):
        select = random.randint(1,20)

    time.sleep(1)
    print ("\n - S..H..A..K..I..N..G..!!! - \n")
    time.sleep(1)
    print (" - S..H..A..K..I..N..G..!!! - \n")
    time.sleep(2)
    print (" - S..H..A..K..I..N..G..!!! - \n")
    time.sleep(1)
    if (select == 1):
        print("It is certain!")
    elif (select == 2):
        print("It is decidedly so")
    elif (select == 3):
        print("Without a doubt")
    elif (select == 4):
        print("Yes - definitely")
    elif (select == 5):
        print("You may rely on it")
    elif (select == 6):
        print("As I see it, yes")
    elif (select == 7):
        print("Most likely")
    elif (select == 8):
        print("Outlook good")
    elif (select == 9):
        print("Yes")
    elif (select == 10):
        print("Sings point to yes")
    elif (select == 11):
        print("Reply hazy, try again")
    elif (select == 12):
        print("Ask again later")
    elif (select == 13):
        print("Better not tell you now")
    elif (select == 14):
        print("Cannot predict now")
    elif (select == 15):
        print("Concentrate and ask again")
    elif (select == 16):
        print("Dont count on it")
    elif (select == 17):
        print("My reply is no")
    elif (select == 18):
        print("My sources say no")
    elif (select == 19):
        print("Outlook not so good")
    elif (select == 20):
        print("Very Doubtful")
    else :
        print("Error!")
  
  
    userSelection = input("\nPress -1- to ask a new question, -2- to shake again, -3- to quit:")
    if (userSelection == "1"):
        input("Ask the Magic 8 Ball something: ")
        shake()
    elif (userSelection == "2"):
        shake()
    elif (userSelection == "3"):
        exit()
    else :
        print ("You didn't select 1, 2, or 3, Good bye!")
        exit()


shake()
  