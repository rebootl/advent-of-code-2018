#!/usr/bin/python
#
import re

with open('day4-input.txt', 'r') as f:
    entries = list(f)

# exampleraw = '''[1518-11-01 00:00] Guard #10 begins shift
# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up
# [1518-11-01 00:30] falls asleep
# [1518-11-01 00:55] wakes up
# [1518-11-01 23:58] Guard #99 begins shift
# [1518-11-02 00:40] falls asleep
# [1518-11-02 00:50] wakes up
# [1518-11-03 00:05] Guard #10 begins shift
# [1518-11-03 00:24] falls asleep
# [1518-11-03 00:29] wakes up
# [1518-11-04 00:02] Guard #99 begins shift
# [1518-11-04 00:36] falls asleep
# [1518-11-04 00:46] wakes up
# [1518-11-05 00:03] Guard #99 begins shift
# [1518-11-05 00:45] falls asleep
# [1518-11-05 00:55] wakes up'''
# entries = exampleraw.splitlines()
# result: 240

entries.sort()
#print(rawlist)
#for l in entries:
#    print(l.rstrip("\n"))

#class Guard:
#    def __init__(self, id):
#        self.id = id
#        self.sleep_min = 0

guards = {}
guards_minutes = {}

for l in entries:
    l1, l2 = l.split("]")
    if l2.strip().startswith("Guard"):
        curr_id = re.search('([0-9]+)', l2)[0]
        #print(curr_id)
    elif l2.strip().startswith("falls"):
        sleep_start = int(l1.split(":")[1])
        #print(sleep_start)
    elif l2.strip().startswith("wakes"):
        sleep_end = int(l1.split(":")[1])
        sleep_time = sleep_end - sleep_start
        if curr_id in guards.keys():
            guards[curr_id] += sleep_time
        else:
            guards[curr_id] = sleep_time
        for m in range(sleep_start, sleep_end):
            if (curr_id, m) in guards_minutes.keys():
                guards_minutes[(curr_id, m)] += 1
            else:
                guards_minutes[(curr_id, m)] = 1

bigval = 0
for k, v in guards.items():
    if v > bigval:
        guard_id = k
        bigval = v

bigval = 0
for k, v in guards_minutes.items():
    if v > bigval and k[0] == guard_id:
        most_mins = k
        bigval = v

print(int(guard_id) * most_mins[1])

bigval = 0
for k, v in guards_minutes.items():
    #print(k, v)
    if v > bigval:
        most_freq = k
        bigval = v

print(int(most_freq[0]) * most_freq[1])
