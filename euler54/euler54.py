import cards, pokerhand

def euler54():
	player1, player2, game = 0, 0, 0
	poker = open('poker.txt').read().split('\n')
	poker = poker[:1000]
	try:
		for line in poker:
			game +=1
			deal1, deal2 = line[:14].split(), line[15:].split()
			hand1, hand2 = [], []

			for card_str in deal1:
				hand1.append(cards.card.from_string(card_str))
			hand1 = pokerhand.hand(hand1)

			for card_str in deal2:
				hand2.append(cards.card.from_string(card_str))
			hand2 = pokerhand.hand(hand2)

			if hand1 > hand2:
				player1 += 1
				print "Player 1 wins!"
			else:
				player2 += 1
				print "Player 2 wins!"
		print "Player 1 wins", player1, "hands."
		print "Player 2 wins", player2, "hands."
	except ValueError, e:
		print "Error in game#", game, "\nProblem with line # ", game-1, "\n"
		print poker[game-1]
