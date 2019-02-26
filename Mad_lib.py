story = '''
{} was a very skilled {}, but {} always dreamed of doing {} for a living.
Everyone would make fun of {} for their {} {}...
Which made it very hard for their {} dreams.
Till one day, {} ran into {} and complimented {} on their {} {}.
"Wow, thanks {}! I've always thought that my {} was actually {}, but {} coninced me otherwise."
"Hey {}, how about we go get some {} and eat it in the {}!"
'''

def main():
	name = []
	name.append(input("Enter a name: "))
	name.append(input("and another one: "))
	name.append(input("ok, one more name: "))

	adjective = []
	adjective.append(input("Enter an adjective: "))
	adjective.append(input("another adjective: "))
	adjective.append(input("and a 3rd: "))

	hobby = input("Enter a hobby: ")
	food = input("Enter a food: ")
	location = input("Enter a location: ")
	profession = input("Enter a profession: ")
	body_part = input("And lastly, a body part: ")

	mad_lib = story.format(name[0],
							profession,
							name[0],
							hobby,
							name[0],
							adjective[0],
							body_part,
							hobby,
							name[1],
							name[0],
							name[0],
							adjective[0],
							body_part,
							name[1],
							body_part,
							adjective[1],
							name[2],
							name[1],
							food,
							location
							)

	print(mad_lib)

	input("Hit any key to exit.")

main()