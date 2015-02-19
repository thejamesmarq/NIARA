#extracts the highest ranked ngrams

import csv

grams = ["8y2","m3e","5or","3ez","zn5","qb1","ezn","jia","sfc","rhs","hsf","5o","b1","ez","fc","cj","ia","hs","ax","2","F95","e-","q-i","q-h","q-o","q-a","q-e","PQU","n","s","q","e","i"]

header = ["url"] + grams

features = []
with open("/Users/jamarq_laptop/NIARA/DGA_Data","rb") as infile, open("/Users/jamarq_laptop/NIARA/DGA_top45","wb") as outfile:
	writer = csv.writer(outfile)
	writer.writerow(header)

	for line in infile:

		url = line.split("\t")[0]

		gram_feats = [0]*len(grams)

		for i in range(0,len(grams)):
			if grams[i] in url:
				gram_feats[i] = 1
		row = [url] + gram_feats
		writer.writerow(row)




