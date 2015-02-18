#!/usr/bin/env python

"""MeaningfulCharacters.py: compute the meaningful characters ratio (MCR) 
(what proportion of the characters in the string)
are made up of actual words
e.g. "facebook" is face (4) and book(4) so the MCR is (4+4)/8"""

__author__      = "James Marquardt"
__copyright__   = "Copyright 2015, UWT"

import itertools, enchant

dictionary = enchant.Dict("en_US")

#split the string in all possible places
def break_down(text):
    words = text.split()
    ns = range(1, len(words))
    for n in ns:
        for idxs in itertools.combinations(ns, n):
            yield [' '.join(words[i:j]) for i, j in zip((0,) + idxs, idxs + (None,))]

#compute the maximum meaningful characters ratio
def meaningful_characters(domain):

	domain_length = float(len(domain))
	domain = ''.join([i for i in domain if not i.isdigit()])
	max_ratio = 0.0
	breakdowns = break_down(" ".join(domain))

	for words in breakdowns:

		char_count = 0

		for word in words:
			if len(word.strip().replace(" ","")) > 1 and dictionary.check(word.replace(" ","")):
				char_count += len(word.strip().replace(" ",""))

		temp_ratio = float(char_count) / domain_length

		if temp_ratio > max_ratio:
			max_ratio = temp_ratio

	return max_ratio