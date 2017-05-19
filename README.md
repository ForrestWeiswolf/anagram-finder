#find_anagrams outputs a list of anagrams of a passed text, using words from a passed lexicon. Lines 1-5 create a lexicon from nltk corpuses for this purpose. To use a text file as a custom lexicon, replace lines 1-3 with 
	file = open('/path/to/file.txt', 'r')
	corpus = file.read().split()
	lexicon = set(w.lower() for w in corpus)
	print("Lexicon compiled")