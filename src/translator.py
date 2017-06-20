#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kurt
import os
import re

MAPPING = [
	['repeat', 'for i in int(%s):'],
	['say', 'print %s'],
	['end', '']
]

# get current working directory
path = os.getcwd()
path = path[:path.rfind('src')] + 'data/'

# load the scratch project
p = kurt.Project.load(path + 'hello_world_simple.sb2')

# show the blocks included
for scriptable in p.sprites + [p.stage]:
	for script in scriptable.scripts:
		s = script

#~ print s
#~ print

for b in s.blocks:
	sentences = b.stringify().split('\n')
	
#~ print sentences
#~ print

python_program = ""
tab_seq = "\t"
for s in sentences:
	aux = s.replace('    ', tab_seq).split(' ', 1)
	for m in MAPPING:
		if m[0] in aux[0]:
			if len(aux) > 1:
				python_program += tab_seq * aux[0].count(tab_seq) + m[1] % aux[1]
	python_program += "\n"

print python_program
