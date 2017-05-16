#import nltk

def find_anagrams(text, lexicon):
	results = ""#[]

	for word in lexicon:
		try_text = text
		for l in word:
			if (try_text.find(l) != -1):
				try_text = try_text.replace(l, "", 1)
			else:
				break
		else:
			#for rest_option in find_anagrams(try_text, lexicon):
			#	results.append(word + " " + rest_option)
			results = word + " " + find_anagrams(try_text, lexicon)

	return results