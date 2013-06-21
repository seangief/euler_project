#open and clean cipher
f = open("cipher1.txt")
cipher = f.read().split(',')
f.close()
cipher[len(cipher)-1] = cipher[len(cipher)-1].strip()
for i in range(len(cipher)):
	cipher[i] = int(cipher[i])

def decode(cipher):
	#'a'=97, 'z'=122
	answer = []
	keys = [(a, b, c) for a in range (97,123) for b in range(97,123) for c in range(97,123)]
	for key in keys:
		str_list, i, maxi = [], 0, len(cipher)
		while i < maxi:
			str_list.append(chr(key[0]^cipher[i]))
			i+=1
			if (i+1 < len(cipher)):
				str_list.append(chr(key[1]^cipher[i]))
				i+=1
			if (i+2 < len(cipher)):
				str_list.append(chr(key[2]^cipher[i]))
				i+=1
		answer.append(''.join(str_list))
	return answer

'''
The passage is from the bible:
"(The Gospel of John, chapter 1) 1 In the beginning the Word already existed. He was with God, and he was God. 2 He was in the beginning with God. 3 He created everything there is. Nothing exists that he didn't make. 4 Life itself was in him, and this life gives light to everyone. 5 The light shines through the darkness, and the darkness can never extinguish it. 6 God sent John the Baptist 7 to tell everyone about the light so that everyone might believe because of his testimony. 8 John himself was not the light; he was only a witness to the light. 9 The one who is the true light, who gives light to everyone, was going to come into the world. 10 But although the world was made through him, the world didn't recognize him when he came. 11 Even in his own land and among his own people, he was not accepted. 12 But to all who believed him and accepted him, he gave the right to become children of God. 13 They are reborn! This is not a physical birth resulting from human passion or plan, this rebirth comes from God.14 So the Word became human and lived here on earth among us. He was full of unfailing love and faithfulness. And we have seen his glory, the glory of the only Son of the Fatheq."
#But wait... "Fatheq"? must be a typo, like an off by one. Add one to the sum...

#candid = [s for s in ans if "Gospel" in s]
# sum([ord(a) for a in candid[0]])+1
