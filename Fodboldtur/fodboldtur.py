# PROGRAMMERING OPGAVE 31/10/2023

import pickle

filename = 'betalinger.pk'
fodboldturinfo = {"Date": 6/11/2023, "Location": "London, England", "Audience Count": 123.456}
itemlist = ['Ticket', 'Holdtrøje', 'Halstørklæde', 'Kasket']
itemlistdict = {'Ticket': 359, 'Holdtrøje': 150, 'Halstørklæde': 95, 'Kasket': 85}
issuelist = ['Lag', 'bad website']


#  FUNKTION DEFINITIONER -------------------------------------------------------------------------------------------


#  funktionen på information (1)
def info():
    print(fodboldturinfo) #printer info af fodboldturen
    menu()

#  funktionen på prislisten (2)
def pricelist():
    print(itemlist)  # printer prislisten


#  funktionen på indbetalinger (3)
def payment():
    print(list(itemlistdict.keys()))  # printer en list over de items man kan købe
    item = input("Choose an item to add in cart..")  # giver brugeren muligheden for at vælge en item
    if item in list(itemlistdict.keys()):  # hvis item'et de har tastede på er gyldig,
        print(f"{itemlistdict[item]} kr.")  # viser det prisen af item'et



#  funktionen på dem der har betalt (4)
def leaderboard():
    sorted_dict = sorted(fodboldtur.items(), key=lambda x: x[1])
    for i in range(3):
        print(sorted_dict[i])


#  funktionen over programhjælp (5)
def help():
    print("Welcome to Fodboldtur support page.")
    issue = input("Please enter your issue..")
    if issue in issuelist:
        print("Okay, we will work on that issue.\n")
        menu()
    elif issue not in issuelist:
        print("Okay :D \n")
        menu()

#  funktionen på afslutning af programmet (6)
def quit():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    quit()
    print("PROGRAM QUITTED!")


def menu():
    print("Welcome to Fodboldtur")
    UserInput = input('[ Enter User ID ] ')
    if UserInput in fodboldtur.keys():
        running = True
        while running:
            print("Welcome back" + " " + UserInput)
            print("------------ MAIN MENU ----------")
            print("1: INFORMATION")
            print("2: PRICE LIST")
            print("3: PAYMENT")
            print("4: LEADERBOARD")
            print("5: HELP")
            print("6: QUIT PROGRAM")
            actionInput = input('Choose your action..')
            if actionInput == '1':
                info()
            elif actionInput == '2':
                pricelist()
                print(itemlist)
            elif actionInput == '3':
                payment()
            elif actionInput == '4':
                leaderboard()
            elif actionInput == '5':
                help()
            elif actionInput == '6':
                quit()
            else:
                print("User ID invalid.")
                break
        menu()

infile = open(filename, 'rb')
fodboldtur = pickle.load(infile)
infile.close()
menu()
