# MOVIE DATA MANAGEMENT PROJECT - SANA S


# Pre-existing Users Dictionary (Username, Password)


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

# Favourites 
favourites = [{}]


# User System

# Menu Option Functions
def displayall():
    for movie in movies:
        print(movie["title"])

def search(title):
    for i in range (len(movies)):
        if movies[i]["title"] == title:
            return i
    return -1

def searchmovie():
    searchMov = input("Please enter a movie you want to search up: ")
    index = search(searchMov)
    if index != -1:
        print("Title:",movies[index]["title"]) 
        print("Genre:",movies[index]["genre"]) 
        print("Director:",movies[index]["director"])
    else:
        print("Movie not found")  

def sorttitle(): # alphabetical order of genres 
    pass

def addfav():
    pass

def removefav():
    pass

def displayfav():
    pass

def add():
    newtitle = input("What is the title of this movie? ")
    newgenre = input("What is the genre for this movie? ")
    newdir = input("What is the director for this movie? ")
    print("Movie Added")
    newMovie = {
        "title": newtitle,
        "genre": newgenre,
        "director": newdir
    }
    movies.append(newMovie)

def remove():
    removemov = input("What is the name of the movie you would like to delete? ")
    index = search(removemov)
    if index != -1:
        del movies[index]
    else:
        print("Movie not found")

def exit():
    loop = False 
    print("\nBye!")

# Menu Options 
def getMenuSelection():
    # Menu Options
    print(f"\n********MAIN MENU********")
    print("1. Display movies")
    print("2. Search data")
    print("3. Sort by title")
    print("4. Add to favourite")
    print("5. Display favourites")
    print("6. Add new movie")
    print("7. Remove a movie")
    print("8. Exit")
    return input("\nChoose an option please: ").lower()

# Main Menu
loop = True
while loop:
    selection = getMenuSelection()

    if selection == "1" or selection == "display all data":
        displayall()
    elif selection == "2" or selection == "search data":
        searchmovie()
    elif selection == "3" or selection == "sort by title":
        sorttitle()
    elif selection == "4" or selection == "add to favourite":
        addfav()
    elif selection == "5" or selection == "remove from favourite":
        removefav()
    elif selection == "6" or selection == "remove from favourite":
        add()
    elif selection == "7" or selection == "remove from favourite":
        remove()
    elif selection == "8" or selection == "exit":
        exit()
    else: 
        print("Please choose an option. ")








