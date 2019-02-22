import abc

class AudioFile(metaclass = abc.ABCMeta):
	def __init__(self, fname):
		self.__fname = fname
	
	def getFileName(self):
		return self.__fname
	
	@abc.abstractmethod
	def load(self):
		pass
	
	@abc.abstractmethod
	def play(self):
		pass
	
class MP3(AudioFile):
	ext = ".mp3"
	def load(self):
		print("Loading",super().getFileName() + MP3.ext)
	
	def play(self):
		print("PLAYING",super().getFileName())
	
class WAV(AudioFile):
	ext = ".wav"
	def load(self):
		print("Loading",super().getFileName() + WAV.ext)
		
	def play(self):
		print("PLAYING",super().getFileName())
	

if __name__ == "__main__":
	a = MP3("radiohead")
	b = WAV("adele")
	
	lst = [a, b]
	for ob in lst:
		ob.load()
		ob.play()
	
	
	
	
