#!/usr/bin/env python

FILENAME='day2.txt'

def cnt_occurences(s):
  counters = {}
  for c in s:
    counters[c] = counters.get(c, 0) + 1
  return counters


def all_but_one_letter_match(a, b):
  differences = 0
  identical = ''
  for i, cursor in enumerate(a):
    if b[i] != cursor:
      differences += 1
    else:
      identical += cursor
  if differences == 1:
    return identical
  return False


def part2():
  singletons = []
  pairs = []
  for s in open(FILENAME).readlines():
    print '%s in [%d]' % (s.strip(), len(singletons))
    singletons.append(s)
    for b in singletons:
      a = all_but_one_letter_match(s, b)
      if a:
        print a


def part1():
  cnt_twins = 0
  cnt_triplets = 0
  for s in open(FILENAME).readlines():
    counters = cnt_occurences(s)
    if 2 in counters.values():
      cnt_twins += 1
    if 3 in counters.values():
      cnt_triplets += 1
  print '%d * %d = %d' % (cnt_twins, cnt_triplets, cnt_twins * cnt_triplets)


part2()
