#!/usr/bin/env python

# takes in a single word with one or more letters replaced with '.' to signify
# 'any character', and returns all possible words matching the description.
#
# This can be done trivially with:
#  'cat words | grep '^sh.y$' => 'shay'

import sys

from collections import defaultdict


with open('/usr/share/dict/words', 'r') as f:
    words = { w.strip().lower() for w in f }

# create sets of words that contain the same letter
# in the ith position. i.e.:
#
#  (0,a) => {'a', 'aardvark', 'aardwolf', ...}
#  (1,a) => {'baa', 'baby', ...}
#   ...

letter_pos_map = defaultdict(set)

for word in words:
    for i, letter in enumerate(word):
        letter_pos_map[(letter, i)].add(word)

word_desc = sys.argv[1]
word_len = len(word_desc)
word_list = None

# for every letter provided, union the set at (letter, position) to
# generate the list of words that meet the constraint
for i, letter in enumerate(word_desc):
    if not letter == '.':
        possible_words = { i for i in letter_pos_map[(letter, i)] if len(i) == word_len }

        if not word_list:
            word_list = possible_words
        else:
            word_list.intersection_update(possible_words)

print word_list
