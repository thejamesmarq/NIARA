#!/usr/bin/env python

"""ExtractFeatures.py: extract an ngram frequency vector for all documents.
Replace all paths with paths of your data."""

__author__      = "James Marquardt"
__copyright__   = "Copyright 2015, UWT"

import csv,sys

#the "n" in n-grams
grams = 3

#------Getting possible grams-----#
all_grams = []

print "Gathering possible grams for DGA"

with open("DGA_Data", "rU") as infile1:

	for line in infile1:
		domain = line.split("\t")[0].split(".")[0]

		for g in range(1,grams+1):
			all_grams.extend([domain[i:i+g] for i in range(len(domain)-g+1)])

all_grams = list(set(all_grams))

header = []
header.append("domain")
header.append("class")
header.extend(all_grams)

#-----Make feature vectors-----#

print "Making feature vectors for DGA"

with open("DGA_Data", "rU") as infile1, open("DGA_Data_all_grams.csv", "wb") as outfile:

	writer = csv.writer(outfile)
	writer.writerow(header)

	for line in infile1:
		domain = line.split("\t")[0].split(".")[0].strip()
		label = line.split("\t")[1].strip()

		these_grams = []

		for g in range(grams,grams+1):
			these_grams.extend([domain[i:i+g] for i in range(len(domain)-g+1)])

		row = []
		row.extend([0] * len(all_grams))

		for gram in these_grams:
			if row[all_grams.index(gram)]==0:
				row[all_grams.index(gram)]=1

		row.insert(0, line.split("\t")[0])
		row.insert(0, label)

		#row.extend([line.split("\t")[0],label])

		writer.writerow(row)
