#!/usr/bin/env python

import re

FILENAME = 'input.txt'
claims = {}

def part1(claims):
  print len([claim for coord, claim in claims.iteritems() if len(claim) > 1])

def part2(claims):
  non_overlaps = set()
  overlaps = set()
  for coord, claim in claims.iteritems():
    if len(claim) == 1:
      non_overlaps.add(claim[0])
    else:
      overlaps.update(claim)
  print non_overlaps - overlaps


def main():
  for s in open(FILENAME).readlines():
    claim_id, left, top, width, height = re.split(r'[\sx\,\:\@]+', s.strip())
    print '%s %s %s %s %s' % (claim_id, top, left, width, height)
    for x in range(0, int(width)):
      for y in range(0, int(height)):
        coords = str(int(left) + 1 + x) + ' - ' + str(int(top) + 1 + y)
        if coords not in claims:
          claims[coords] = [claim_id]
        else:
          claims[coords].append(claim_id)
#  part1(claims)
  part2(claims)

main()