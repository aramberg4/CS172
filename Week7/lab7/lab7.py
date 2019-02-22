from room import Room
from maze import Maze

def main():
	my_rooms = []
	my_rooms.append(Room("This room is the entrance."))
	my_rooms.append(Room("This room has a table. Maybe a dinning room?"))
	my_rooms.append(Room("This room is the exit. Good Job."))
	#room 0 is south of room 1
	my_rooms[0].setNorth(my_rooms[1])
	my_rooms[1].setSouth(my_rooms[0])
	#Room 2 is east of room 1
	my_rooms[1].setEast(my_rooms[2])
	my_rooms[2].setWest(my_rooms[1])
		
	#Make a maze!
	#Set the start and exit rooms.
	my_maze = Maze(my_rooms[0],my_rooms[2])
	#Create an interface for the player.	
	while True:
		#Print a description of the room.
		print(my_maze.getCurrent())
		#Next, ask the player what direction to move.
		while True: 
			try:
				userInput = input('Enter direction to move (north, west, east, south, restart): ')
				if userInput not in ['north','west','east','south','restart']:
					print('Direction invalid, try again.')
					continue
				break
			except:
				print('Error: your answer has to be a valid direction')
		#Either move into the next room, or stay in the same place if the path is blocked.
		if(userInput == 'north'):
			if(my_maze.moveNorth()):
				print('You went north')
				if(my_maze.atExit()):
					print('You found the exit!')
					break
			else:
				print('There is no door in this direction, try again.')
		elif(userInput == 'west'):
			if(my_maze.moveWest()):
				print('You went west')
				if(my_maze.atExit()):
					print('You found the exit!')
					break
			else:
				print('There is no door in this direction, try again.')
		elif(userInput == 'east'):
			if(my_maze.moveEast()):
				print('You went east')
				if(my_maze.atExit()):
					print('You found the exit!')
					break
			else:
				print('There is no door in this direction, try again.')
		elif(userInput == 'south'):
			if(my_maze.moveSouth()):
				print('You went south')
				if(my_maze.atExit()):
					print('You found the exit!')
					break
			else:
				print('There is no door in this direction, try again.')
		elif(userInput == 'restart'):
			my_maze.reset()

if __name__ == "__main__":
	main()