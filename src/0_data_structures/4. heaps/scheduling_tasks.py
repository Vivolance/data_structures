"""
Given a list of task with its specific start time and duration, determine
the best schedule to finish all tasks as fast as possible.

Example input:

tasks: list[tuple] = [
        (datetime(year=2024, month=1, day=1,hour=0, minute=0, second=0), timedelta(hour=1)),
        (datetime(year=2024, month=1, day=1,hour=1, minute=0, second=0), timedelta(hour=3)),
        (datetime(year=2024, month=1, day=1,hour=3, minute=0, second=0), timedelta(hour=2)),
    ]

return datetime after all tasks finished

Example output:
datetime(year=2024, month=10, day=1, hour=6, minute=0, second=0)
"""
import heapq
from datetime import timedelta, datetime


tasks: list[tuple[datetime, timedelta]] = [
    (
        datetime(2025, 1, 1, 0, 0, 0),
        timedelta(hours=1)
    ),
    (
        datetime(2025, 1, 1, 1, 0, 0),
        timedelta(hours=3)
    ),
    (
        datetime(2025, 1, 1, 3, 0, 0),
        timedelta(hours=2)
    ),
]

# arrange the tasks into a heap
heapq.heapify(tasks)

# create a start time for all tasks
curr_time: datetime = datetime(2025, 1, 1, 0, 0, 0)

while tasks:
    curr_task: tuple[datetime, timedelta] = heapq.heappop(tasks)
    curr_time: datetime = max(curr_time, curr_task[0])
    curr_time += curr_task[1]

print(curr_time)
