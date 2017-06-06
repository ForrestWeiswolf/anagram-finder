import nltk
from nltk.corpus import gutenberg
corpus = gutenberg.words('bible-kjv.txt') + gutenberg.words('blake-poems.txt')
lexicon = set(w.lower() for w in corpus)
print("Lexicon compiled")

import re

def find_anagrams(text, lexicon, limit):
	results = []
	text = re.sub('\W+', '', text).lower()
	stack = [("", text)]

	while len(stack) > 0:
		if len(results) >= limit:
			return results
		else:
			option = stack.pop(0)
			part_anagram = option[0]
			remaining = option[1]
			if len(remaining) == 0:
				results.append(part_anagram)
			else:
				for word in lexicon:
					try_text = remaining
					for l in word:
						if (try_text.find(l) != -1):
							try_text = try_text.replace(l, "", 1)
						else:
							break
					else:
						stack.append((" ".join([part_anagram, word]), try_text))

	return results