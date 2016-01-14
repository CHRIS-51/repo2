#!/usr/bin/env python
# read pairs - form triplets
# implements hort: g0<g1
import sys
import string

dict={}
for line in sys.stdin: 
	str1=line.strip()
	(g0,g1) = str.split(str1)
	if (g0 > g1):
		g2=g0
		g0=g1
		g1=g2
	if g0 not in dict:
		dict[g0] = set()
	dict[g0].add(g1)

for gene in dict:
	for partner in dict[gene]:
		if partner in dict:
			ovr = dict[gene].intersection(dict[partner])
			if len(ovr):
				for j in ovr:
					print(gene,partner,j)
