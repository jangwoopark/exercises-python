#!/bin/python3
from heapq import *

orders = []
queue = []
wait_times = []
time_elapsed = 0
n = int(input().strip())
for i in range(n):
    time_entered, time_to_complete = map(int, input().strip().split(' '))
    heappush(orders, (time_entered, time_to_complete))

while orders or queue:
    # load the queue
    while orders and orders[0][0] <= time_elapsed:
        entered, duration = heappop(orders)
        heappush(queue, (duration, entered))

    # still nothing in the queue, pull the next order
    if not queue:
        entered, duration = heappop(orders)
        time_elapsed = entered
        heappush(queue, (duration, entered))

    # evaluate the priority queue
    cook_duration, cook_entered_time = heappop(queue)
    wait_time = time_elapsed - cook_entered_time
    time_elapsed += cook_duration
    wait_time += cook_duration
    wait_times.append(wait_time)

print(int(sum(wait_times)/n))
