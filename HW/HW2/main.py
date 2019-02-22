#File Name:   main.py
#Purpose:     Program that simulates a media library.
#Author:      Austin Ramberg
#User id: 	  afr38
#Date:        February 5, 2019

from media import *

def initializeMedialibrary():
    mediaList = []

    # songs
    song1 = Song('A Day in the Life', 7, 'The Beatles', 'Sgt. Pepper\'s Lonely Hearts Club Band')
    mediaList.append(song1)

    song2 = Song('God Only Knows', 9, 'The Beach Boys', 'Pet Sounds')
    mediaList.append(song2)

    song3 = Song('Be My Baby', 10, 'The Ronettes', 'Single')
    mediaList.append(song3)

    song4 = Song('Go Your Own Way', 9, 'Fleetwood Mac', 'Rumours')
    mediaList.append(song4)

    # movies
    movie1 = Movie('The Breakfast Club', 9, 'John Hughes', 97)
    mediaList.append(movie1)

    movie2 = Movie('Back to the Future', 8, 'Robert Zemeckis', 116)
    mediaList.append(movie2)

    movie3 = Movie('Whiplash', 9, 'Damien Chazelle', 106)
    mediaList.append(movie3)

    movie4 = Movie('Apocalypse Now', 7, 'Francis Ford Coppola', 97)
    mediaList.append(movie4)

    # pictures
    pic1 = Picture('feelsBadMan.jpeg', 5, 800)
    mediaList.append(pic1)

    pic2 = Picture('MonaLisa.jpeg', 10, 1200)
    mediaList.append(pic2)

    pic3 = Picture('boof.png', 6, 200)
    mediaList.append(pic3)

    pic4 = Picture('homework.png', 9, 800)
    mediaList.append(pic4)

    return mediaList

# function to disply the main menu in the loop
def printMenu():
    print('\n')
    print('Menu:')
    print('1. Display all items in the Media library')
    print('2. Display only songs')
    print('3. Display only movies')
    print('4. Display only pictures')
    print('5. Play a Song')
    print('6. Play a Movie')
    print('7. Display a Picture')
    print('8. Quit the program')

# function to display all media in mediaList of type mediaType
def displayMedia(mediaType, mediaList):
    for item in mediaList:
        if(item.getMediaType() == mediaType):
            print(item)

# function to play/show the name of a medium of type mediaType in mediaList
def interactWithMedia(mediaType, mediaList):
    found = False
    # Name can really be anything, even a number, so I will just convert to a string
    name = str(input('Please enter the name of a song you would like to play: '))
    for item in mediaList:
        if(item.getMediaType() == mediaType and item.getName() == name):
            if(mediaType == 'Picture'):
                item.show()
            else:
                item.play()
            found = True
    if(found == False):
        print('Sorry, the ' + mediaType + ' you were looking for is not in the media library')

def main():
    mediaList = initializeMedialibrary()
    print('Welcome to the Media Library!')
    while True:
        printMenu()
        while True:
            try:
                userInput = float(input('Please press the button for the action you wish to perform: '))
                if userInput not in [1,2,3,4,5,6,7,8]:
                    print('Your input was a number, but not between 1 and 8. Please try again.')
                    continue
                break
            except:
                print('Error: your answer has to be a value between 1 and 8. Try again.')
        print('\n')
        if(userInput == 1):
            for item in mediaList:
                print(item)
        elif(userInput == 2):
            displayMedia('Song', mediaList)
        elif(userInput == 3):
            displayMedia('Movie', mediaList)
        elif(userInput == 4):
            displayMedia('Picture', mediaList)
        elif(userInput == 5):
            interactWithMedia('Song', mediaList)
        elif(userInput == 6):
            interactWithMedia('Movie', mediaList)
        elif(userInput == 7):
            interactWithMedia('Picture', mediaList)
        elif(userInput == 8):
            break

if __name__ == "__main__":
    main()