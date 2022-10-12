# MOVIE DATA MANAGEMENT PROJECT - SANA S

import json

# DICTIONARIES
# Users Dictionary (Username, Password)
foundUser = 0

# Movie Dictionary (Title, Genre, Director)
movies = [{
    "title": "The Conjuring",
    "genre": "Horror",
    "director": "James Wan"
    },
{
    "title": "Insidious",
    "genre": "Horror",
    "director": "James Wan"
    },
{
    "title": "Heathers",
    "genre": "Drama",
    "director": "Michael Lehmann"
    },
{
    "title": "Murder on the Orient Express",
    "genre": "Mystery",
    "director": "Kenneth Branagh"
}]

# Favourites (Title, Genre, Director)
favourites = [ ]

file = open("users.txt", "r")
user_from_file = file.read()
file.close()

users = json.loads(user_from_file)
print(users)

# FUNCTIONS
# Login 
foundUser = 0
def login():
    print("\n*****LOGIN MENU*****")
    user = input("Username: ")
    foundUser = findUP("username", user)
    if foundUser != -1:
        passw = input("Password: ")
        foundPass = findUP("password", passw)
        if foundPass != -1:
            mainMenu()
        else:
            print("Wrong Password!")
            login()
    else:
        print("No account found. Please register.")
        requestInfo()
        mainMenu()


# Random Functions to Help
def bubbleSort(anArray, item):
    for i in range(len(anArray)):
        for nums in range(0, len(anArray) - i - 1):
            if anArray[nums][item] > anArray[nums + 1][item]:
                temp = anArray[nums]
                anArray[nums] = anArray[nums + 1]
                anArray[nums + 1] = temp

def search(anArray, title):
    for i in range (len(anArray)):
        if anArray[i]["title"] == title:
            return i
    return -1

# Menu Option Functions
def displayall():
    for movie in movies:
        print(movie["title"])

def searchmovie():
    searchMov = input("Please enter a movie you want to search up: ")
    index = search(movies, searchMov)
    if index != -1:
        print("Title:",movies[index]["title"]) 
        print("Genre:",movies[index]["genre"]) 
        print("Director:",movies[index]["director"])
    else:
        print("Movie not found")  

def sortgenre(): 
    bubbleSort(movies, "genre")
    for movie in movies:
        print(movie["genre"], ":", movie["title"])

def add():
    newtitle = input("What is the title of this movie? ")
    searching = search(movies, newtitle)
    if searching == -1:
        newgenre = input("What is the genre for this movie? ")
        newdir = input("What is the director for this movie? ")
        print("Movie Added")
        newMovie = {
            "title": newtitle,
            "genre": newgenre,
            "director": newdir
        }
        movies.append(newMovie)
    else: 
        print("Movie already in the list.")

def remove():
    removemov = input("What is the name of the movie you would like to delete? ")
    index = search(movies, removemov)
    if index != -1:
        movies.pop(index)
        print("Movie deleted.")
    else:
        print("Movie not found")

def addfav():
    favMovie = input("What movie would you like to add to your favourites? ")
    movie = search(movies, favMovie)
    alrMovie = search(users[foundUser]["faves"], favMovie)
    if movie != -1 and alrMovie == 1:
        users[foundUser]["faves"].append(movies[movie])
        print("Movie added")

        users_json = json.dumps(users)
        file = open("users.txt", "w")
        file.write(users_json)
        file.close()
    else:
        print("Movie can not be added to the list. Check if it is already in favourites or if it is not in your general movies list.")


def removefav():
    remfavMovie = input("What movie would you like to remove from your favourites? ")
    index = search(users[foundUser]["faves"], remfavMovie)
    if index != -1:
        users[foundUser]["faves"].pop(index)

        users_json = json.dumps(users)
        file = open("users.txt", "w")
        file.write(users_json)
        file.close()

        print("Movie removed")
    else:
        print("Movie not in list.")


def displayfav():
    print("\nFAVOURITES:")
    for favourite in users[foundUser]["faves"]:
        print("\nTitle: ", favourite["title"], "\nGenre: ", favourite["genre"], "\nDirector: ", favourite["director"])

def exit():
    users_json = json.dumps(users)
    file = open("users.txt", "w")
    file.write(users_json)
    file.close()

    login()

# Menu Options 
def getMenuSelection():
    # Menu Options
    print(f"\n********MAIN MENU********")
    print("1. Display movies")
    print("2. Search data")
    print("3. Sort by genre")
    print("4. Add to favourite")
    print("5. Remove from favourites")
    print("6. Display favourites")
    print("7. Add new movie")
    print("8. Remove a movie")
    print("9. Logout")

    return input("\nChoose an option please: ").lower()

# Main Menu
def mainMenu(): 
    loop = True
    while loop:
        selection = getMenuSelection()

        if selection == "1" or selection == "display all data":
            displayall()
        elif selection == "2" or selection == "search data":
            searchmovie()
        elif selection == "3" or selection == "sort by genre":
            sortgenre()
        elif selection == "4" or selection == "add to favourites":
            addfav()
        elif selection == "5" or selection == "remove from favourites":
            removefav()
        elif selection == "6" or selection == "display favourites":
            displayfav()
        elif selection == "7" or selection == "add new movie":
            add()
        elif selection == "8" or selection == "remove a movie":
            remove()
        elif selection == "9" or selection == "logout":
            exit()
            loop = False
        else: 
            print("Please choose an option. ")


# Function to Register or Login
def requestInfo():
    username = input("What would you like your username to be? ")
    password = input("What would you like your password to be? ")
    users.append(newUser(username,password))

def newUser(username, password):
    return {
        "username": username,
        "password": password,
        "faves": [ ]
    }

def findUP(uorp, item): # find username and password
    for i in range(len(users)):
        if users[i][uorp] == item:
            return i
    return -1

# Register or Login User
rorl = input("Would you like to register or login? ")
if rorl == "login":
    login()
elif rorl == "register":
    requestInfo()
    print("Great! Go ahead and login now.")
    login()


# Things to do 
# add,addfav - already existing