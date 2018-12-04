#!/usr/bin/env python

import re
FILENAME = 'input.txt'
data = {}


def main():
  entries = sorted([s for s in open(FILENAME).readlines()])
  sleep_time = None
  wakeup_time = None
  guard = None
  for entry in entries:
    timestamp = re.search(r'(\d+\-\d+\-\d+)\s(\d+)\:(\d+)\](.*)', entry)
    date, hour, minute, action = timestamp.groups()
    guard_match = re.search(r'Guard\s\#(\d+)', action)
    wakeup_match = re.search(r'wakes', action)
    asleep_match = re.search(r'asleep', action)
    if guard_match:
      guard = guard_match.groups()[0]
      if guard not in data:
        data[guard] = {}
      print 'Guard %s' % guard
      wakeup_time = int(hour)*60 + int(minute)
    elif wakeup_match:
      wakeup_time = int(hour)*60 + int(minute)
      for i in range(asleep_time, wakeup_time):
        if i < 60:
          data[guard][i] = data[guard].get(i, 0) + 1
    elif asleep_match:
      asleep_time = int(hour)*24 + int(minute)
  print data
  record = 0
  champion = ''
  for guard, sleep_minutes in data.iteritems():
    if sum(sleep_minutes.values()) > record:
      record = sum(sleep_minutes.values())
      champion = guard
    print '%s: %d - %d' % (guard, sum(sleep_minutes.values()), 0)
  best_minute = max(data[champion], key=data[champion].get)
  print 'Champion: %s - total minutes slept: %d - best_minute: %d - solution: %d' % (champion, record, best_minute, int(champion) * best_minute)





main()