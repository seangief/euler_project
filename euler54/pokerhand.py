import collections

class hand:
	def __init__(self, cards):
		self.cards = cards
		self.ranking, self.high_ranking_card, self.high_hand_card = self.get_ranking()

	def get_ranking(self):
		hand = sorted(self.cards)
		values = [card.value_value for card in hand]
		suits = [card.suit_value for card in hand]

		# check for a flush
		flush = not suits or [suits[0]] * len(suits) == suits

		# check for a straight
		diffs = []
		for i in xrange(1, len(values)):
			diffs.append(values[i]-values[i-1])
		straight = [1] * len(diffs) == diffs

		sorted_hand = collections.Counter(values)

		# find the largest and second largest group
		prime_group, second_group = (0,0), (0,0)
		for key, value in sorted_hand.iteritems():
			if value > prime_group[1] or (value == prime_group[1] and key > prime_group[0]):
				second_group = prime_group
				prime_group = (key, value)
			elif value > second_group[1] or (value == second_group[1] and key > second_group[0]):
				second_group = (key, value)

		#get the highest card in the hand
		high_hand_card = max(values)

		# find the rank and find the highest card in it
		ranking = 0
		high_ranking_card = high_hand_card
		if straight and flush:  # Straight flush
			if high_hand_card == 12: # Royal flush
				rankinging = 9
			else: ranking = 8
		elif prime_group[1] == 4: # four of a kind
			high_ranking_card = prime_group[0]
			ranking = 7
		elif prime_group[1] == 3: # three of a kind
			high_ranking_card = prime_group[0]
			if second_group[1] == 2: # full house
				ranking = 6
			else: ranking = 3
		elif prime_group[1] == 2:
			if second_group[1] == 2: # two pair
				high_ranking_card == max(prime_group[0], second_group[0])
				ranking = 2
			else:
				high_ranking_card = prime_group[0]
				ranking = 1
		elif flush: # Flush
			ranking = 5
		elif straight: # Straight
			ranking = 4

		return ranking, high_ranking_card, high_hand_card


	def __cmp__(self, other):
		if self.ranking == other.ranking:
			if self.high_ranking_card == other.high_ranking_card:
				return self.high_hand_card - other.high_hand_card
			return self.high_ranking_card - other.high_ranking_card
		return self.ranking - other.ranking

