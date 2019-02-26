import random

def draw_card(card_num):
	card_dealt = random.randint(1,card_num)
	return card_dealt

def main():
	card_num = 10
	drawing = True
	total_player = 0
	chips = 1000

	# 1st card dealt
	card_dealt = draw_card(card_num)
	total_player = card_dealt
	print("1st card: ",card_dealt)

	# 2nd card dealt
	card_dealt = draw_card(card_num)
	total_player += card_dealt
	print("2nd card: ",card_dealt)
	print("Your total: ",total_player)

	# Dealer's card showing
	card_dealt	= draw_card(card_num)
	total_dealer = card_dealt
	print("\nDealer is showing a: ",card_dealt)

	# Player hitting or staying
	while int(total_player) < 21:
		draw_again = input("\nHit or Stay? H=hit. S=stay.  ")
		if draw_again.lower() == "h":
			card_dealt = draw_card(card_num)
			total_player += card_dealt
			print("You drew a ", card_dealt,". Your total is: ",total_player)
		elif draw_again.lower() == "s":
			break
		else:
			print("Be sure to select one of the two available options:")
	
	if int(total_player) == 21:
		print("\nCongrats!!!\nYou just got BLACKJACK!!!\n")
	# Dealer reveals 2nd card & hits or stays
	elif int(total_player) < 21:
		card_dealt = draw_card(card_num)
		total_dealer += card_dealt
		print("\nDealer flips a:",card_dealt,"   Dealer's total is: ",total_dealer)
		input("Hit any key to continue")
		while int(total_dealer) <= 17:
			card_dealt = draw_card(card_num)
			total_dealer += card_dealt
			print("\nDealer drew a:",card_dealt,"    Dealer's total is: ",total_dealer)
			input("Hit any key to continue")
		else:
			if int(total_dealer) > 21:
				print("\nThe dealer busted! You win!")
			else:
				print("\nThe dealer stays at",total_dealer)
				input("Hit any key to continue")


	# Result print
	if total_dealer > total_player and int(total_dealer) <= 21:
		print("\nThe dealer beat your",total_player," with their ",total_dealer)
	elif total_dealer == total_player:
		print("\nWell isn't this boring, you both tied...")
	elif total_player > total_dealer and int(total_player) > 21:
		print("\nOuch... You busted!")
	else:
		print("\nYou beat the dealer's ",total_dealer,"with your ",total_player)


restart = input("\nWant to play again? ENTER=play again. Q=quit.  ")
while restart.lower() != "q":
	main()
else:
	print("Goodbye")



main()

