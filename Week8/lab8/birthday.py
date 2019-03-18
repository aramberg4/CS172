class Birthday():
	def __init__(self, month, day, year):
		self.__day = day
		self.__month = month
		self.__year  = year

	#getters
	def getDay(self):
		return self.__day

	def getMonth(self):
		return self.__month

	def getYear(self):
		return self.__year

	# overrides
	def __str__(self):
		return str(self.getMonth()) + '/' + str(self.getDay()) + '/' + str(self.getYear())

	def __hash__(self):
		return (int(self.getDay())+int(self.getMonth())+int(self.getYear()))%12

	def __eq__(self, other):
		return(self.getDay() == other.getDay() and self.getMonth() == other.getMonth() and self.getYear() == other.getYear())

if __name__ == "__main__":
	b1 = Birthday(9, 8, 1996)
	b2 = Birthday(3, 25, 1952)
	b3 = Birthday(9, 8, 1996)

	print('b1: ', b1)
	print('b1 hash: ', str(hash(b1)))

	print('b2: ', b2)
	print('b2 hash: ', str(hash(b2)))

	print(b1 == b2)
	print(b1 == b3)
