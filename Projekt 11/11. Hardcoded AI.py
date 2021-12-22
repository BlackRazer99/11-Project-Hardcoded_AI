#AI Hardcoded

from Data.text_example import read_all

#read_all()

#this many People are in France in General
number_france = 0
def read_france_all():
    with open("Data/comparison.txt","r") as f:
        file =  f.read().splitlines()

    global number_france
    start = 0
    number = 0
    for data in file:
        if data == "France: 1" or data == "France: 2":
            if data.count("1") == 1 or data.count("2") == 1:
                number = number + 1
    number_france = number
    print("This many People come from France", number_france)
    

#this many peopöe have the numbers 1 and 2 in France
number_france_1 = 0
def read_france_number1():
    with open("Data/comparison.txt","r") as f:
        file =  f.read().splitlines()

    global number_france_1
    start = 0
    number = 0
    for data in file:
        if data == "France: 1":
            if data.count("1") == 1:
                number = number + 1
    number_france_1 = number
    print("This many People come from France and District 1:", number_france_1)

number_france_2 = 0
def read_france_number2():
    with open("Data/comparison.txt","r") as f:
        file =  f.read().splitlines()

    global number_france_2
    start = 0
    number = 0
    for data in file:
        if data == "France: 2":
            if data.count("2") == 1:
                number = number + 1
    number_france_2 = number
    print("This many People come from France and District 2:", number_france_2)


#this many people live in germany in General
number_germany = 0
def read_germany_all():
    with open("Data/comparison.txt","r") as f:
        file =  f.read().splitlines()
    
    global number_germany
    start = 0
    number = 0
    for data in file:
        if data == "Germany: 1" or data == "Germany: 2":
            if data.count("1") == 1 or data.count("2") == 1:
                number = number + 1
    number_germany = number
    print("This many People come from Germany", number_germany)

#this many people live in Germany 1 and 2
number_germany_1 = 0
def read_germany_number1():
    with open("Data/comparison.txt","r") as f:
        file =  f.read().splitlines()

    global number_germany_1
    start = 0
    number = 0
    for data in file:
        if data == "Germany: 1":
            if data.count("1") == 1:
                number = number + 1
    number_germany_1 = number
    print("This many People come from Germany and District 1:", number_germany_1)

number_germany_2 = 0
def read_germany_number2():
    with open("Data/comparison.txt","r") as f:
        file =  f.read().splitlines()

    global number_germany_2
    start = 0
    number = 0
    for data in file:
        if data == "Germany: 2":
            if data.count("2") == 1:
                number = number + 1
    number_germany_2 = number
    print("This many People come from Germany and District 2:", number_germany_2)

#make the "A.I" compare these 
def compare():
    if number_france == number_germany:
        print("France and Germany have the same amount of People")
    elif number_france > number_germany:
        print("France has more people than Germany")
    elif number_france < number_germany:
        print("France has less people than Germany")
    else:
        print("Somethings Wrong")


compare()
