import random

# Announcing room arrival
def msg(room):
	if room['msg'] == '': # There is no custom message
		return 'You have entered the ' + room['name'] + '.\n'
	else:
		return room['msg']

# Direction choice relating to tuple
def get_choice(room,dir):
	if dir.upper() == 'N':
		choice = 0
	elif dir.upper() == 'E':
		choice = 1
	elif dir.upper() == 'S':
		choice = 2
	elif dir.upper() == 'W':
		choice = 3
	else:
		return -1

	if room['directions'][choice] == 0:
		return 4
	else:
		return choice

# Main function
def game():
	dirs = (0,0,0,0) #default position

	# Room list
	entrance = {'name':'Entrance Way','directions':dirs,'msg':''}
	livingroom = {'name':'Livingroom','directions':dirs,'msg':''}
	hallway = {'name':'Hallway','directions':dirs,'msg':''}
	kitchen = {'name':'Kitchen','directions':dirs,'msg':''}
	diningroom = {'name':'Diningroom','directions':dirs,'msg':''}
	family_room = {'name':'Family Room','directions':dirs,'msg':''}

	# Directions are tuples: Rooms to the (N,E,S,W), 0's are walls
	entrance['directions'] = (kitchen,livingroom,0,0)
	livingroom['directions'] = (diningroom,0,0,entrance)
	hallway['directions'] = (0,kitchen,0,family_room)
	kitchen['directions'] = (0,diningroom,entrance,hallway)
	diningroom['directions'] = (0,0,livingroom,kitchen)
	family_room['directions'] = (0,hallway,0,0)

	# Rooms where the diamond crown might be in
	rooms = [livingroom,hallway,kitchen,diningroom,family_room]
	room_with_crown = random.choice(rooms)
	crown_stolen = False
	# Starting point
	room = entrance

	# NEED TO CREATE THE UNLOCK CODE SEQUENCE USING RANDINT()
	print('Door unlocked! You sneak inside the museum, now to find the diamond crown!')

	while True:
		if crown_stolen and room['name'] == 'Entrance Way':
			print('You\'ve successfully found your way back to the entrance, nice work!\n' + 
					'You sneak out the door and work your way back to the hdieout.\n')
			play_again = input('Press any key to play again, otherise type \'Q\' to quit the game. ')
			if play_again.upper() != 'Q':
				game()
			else:
				break;
		elif not crown_stolen and room['name'] == room_with_crown['name']:
			crown_stolen = True
			print(msg(room) + 'You\'ve found the diamond crown!\n' +
					'As you slip the crown off the display, an alarm goes off - ' +
					'Time to get out of here!')
		else:
			print(msg(room))
			room['msg'] = 'You are back in the ' + room['name']


		stuck = True
		while stuck:
			dir = input('Which direction do you want to go: N, E, S, or W? ')
			choice = get_choice(room,dir)
			if choice == -1:
				print('Please enter only: N, E, S, or W.')
			elif choice == 4:
				print('There\'s a wall that way, try a different route.')
			else:
				room = room['directions'][choice]
				stuck = False


game()