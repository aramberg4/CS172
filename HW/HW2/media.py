#File Name:   media.py
#Purpose:     File contains Media class and all child classes.
#Author:      Austin Ramberg
#User id: 	  afr38
#Date:        February 5, 2019

class Media:

    # initialization method 
    def __init__(self,
                mediaType,
                name,
                rating):
        self.__mediaType = mediaType
        self.__name = name
        self.__rating = rating

    # getters
    def getMediaType(self):
        return self.__mediaType

    def getName(self):
        return self.__name

    def getRating(self):
        return self.__rating
        
    # setters
    def setMediaType(self, newType):
        self.__mediaType = newType

    def setName(self, newName):
        self.__name = newName

    def setRating(self, newRating):
        self.__ans2 = newRating

    # overload __str__ method
    def __str__(self):
        return "Name: " + self.getName() + '\n' + "Type: " + self.getMediaType() + '\n' + "Rating: " + str(self.getRating()) + '\n' 

class Movie(Media):

    # initialization method 
    def __init__(self,
                name,
                rating,
                director,
                runTime):
        super().__init__('Movie', name, rating)
        self.__director = director
        self.__runTime = runTime

    # getters
    def getDirector(self):
        return self.__director

    def getRunTime(self):
        return self.__runTime

    # setters
    def setDirector(self, newDirector):
        self.__director = newDirector

    def setRunTime(self, newRunTime):
        self.__runTime = newRunTime

    # overload __str__ method
    def __str__(self):
        return "Name: " + self.getName() + '\n' + "Type: " + self.getMediaType() + '\n' + "Rating: " + str(self.getRating()) + '\n' + "Director: " + self.getDirector() + '\n' + "Run time: " + str(self.getRunTime()) + ' minutes' + '\n'

    # other methods
    def play(self):
        print(self.getName() + ', playing now' + '\n')

class Song(Media):

    # initialization method 
    def __init__(self,
                name,
                rating,
                artist,
                album):
        super().__init__('Song', name, rating)
        self.__artist = artist
        self.__album = album

    # getters
    def getArtist(self):
        return self.__artist

    def getAlbum(self):
        return self.__album

    # setters
    def setArtist(self, newArtist):
        self.__director = newArtist

    def setAlbum(self, newAlbum):
        self.__album = newAlbum

    # overload __str__ method
    def __str__(self):
        return "Name: " + self.getName() + '\n' + "Type: " + self.getMediaType() + '\n' + "Rating: " + str(self.getRating()) + '\n' + "Artist: " + self.getArtist() + '\n' + "Album: " + self.getAlbum() + '\n'

    # other methods
    def play(self):
        print(self.getName() + ' by ' + self.getArtist() + ', playing now'+ '\n')

class Picture(Media):

    # initialization method 
    def __init__(self,
                name,
                rating,
                resolution):
        super().__init__('Picture', name, rating)
        self.__resolution = resolution

    # getters
    def getResolution(self):
        return self.__resolution

    # setters
    def setResolution(self, newResolution):
        self.__resolution = newResolution

    # overload __str__ method
    def __str__(self):
        return "Name: " + self.getName() + '\n' + "Type: " + self.getMediaType() + '\n' + "Rating: " + str(self.getRating()) + '\n' + "Resolution: " + str(self.getResolution()) + ' dpi' + '\n'

    # other methods
    def show(self):
        print('Showing ' + self.getName() + '\n')

# for testing purposes
if __name__ == "__main__":
    myMedia = Media('Movie', 'Titanic', 7)
    print(myMedia)

    myMovie = Movie('The Breakfast Club', 10, 'John Hughes', 97)
    print(myMovie)
    myMovie.play()

    mySong = Song('A Day in the Life', 9, 'The Beatles', 'Sgt. Pepper\'s Lonely Hearts Club Band')
    print(mySong)
    mySong.play()

    myPicture = Picture('feelsBadMan.jpeg', 5, 800)
    print(myPicture)
    myPicture.show()
