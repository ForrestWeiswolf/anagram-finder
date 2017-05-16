#import nltk

def find_anagrams(text, lexicon):
	results = []

	for word in lexicon:
		try_text = text
		for l in word:
			if (try_text.find(l) != -1):
				try_text = try_text.replace(l, "", 1)
			else:
				break
		else:
			if len(try_text) == 0:
				results = [word]
			else:
				rest_anagrams = find_anagrams(try_text, lexicon)
				for rest_anagram in rest_anagrams:
					results.append(word + " " + rest_anagram)
	
	return results

lexicon = ["i", "me", "us", "we", "you", "are", "am", "is", "was", "be", "this", "these", "that", "those"]
print(find_anagrams("matthias", lexicon))