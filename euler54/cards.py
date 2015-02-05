import random

class card:
	values = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
		  'Jack', 'Queen', 'King', 'Ace']
	suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

	def __init__(self, value, suit):
		self.suit_value = suit[0]
		self.value_value = value[0]
		self.value = value[1]
		self.suit = suit[1]

	def __str__(self):
		return self.value + " of " + self.suit

	def __cmp__(self, other):
		if self.value_value == other.value_value:
			return self.suit_value - other.suit_value
		else: return self.value_value - other.value_value

	@classmethod
	def from_string(self, string):
		strdict = {
				'2':0,    '9':7,
				'3':1,    'T':8,
				'4':2,    'J':9,
				'5':3,    'Q':10,
				'6':4,    'K':11,
				'7':5,    'A':12,
				'8':6,    'S':3,
				'D':1,    'C':0,
                                'H':2
			}
		value, suit = strdict[string[0]], strdict[string[1]]
		return card((value, self.values[value]), (suit, self.suits[suit]))
		

class cards:

	def __init__(self):
		global card
		v, s = list(enumerate(card.values)), list(enumerate(card.suits))
		self.ordered = [card(value, suit) for value in v for suit in s]
#		self.ordered.extend([("Black Joker", int.inf, "Red Joker"])
		self.deck = [c for c in self.ordered]
		random.shuffle(self.deck) 


	def newDeck(self):
		self.deck = [card for card in self.ordered]
		random.shuffle(self.deck)
	
	def shuffle(self):
		random.shuffle(self.deck)

	def next(self):
		if not self.deck:
			print "Reshuffling..."
			self.newDeck()
		return self.deck.pop()


def dice(sides):
	while True: yield random.randrange(1, sides+1)

