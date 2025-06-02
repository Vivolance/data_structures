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


def scheduler(tasks: list[tuple[datetime, timedelta]]) -> datetime:
    """
    Takes in a list of tasks (start_time, duration) and returns the datetime when all tasks will be finished at the soonest

    Key Concepts:
    1. Use a min heap to identify which is the earliest start time of each task
    2. Always prioritise choosing tasks that can be started first
    """

    # arrange the tasks into a heap
    heapq.heapify(tasks)

    # create a start time for all tasks
    curr_time: datetime = datetime(2025, 1, 1, 0, 0, 0)

    while tasks:
        curr_task: tuple[datetime, timedelta] = heapq.heappop(tasks)
        curr_time: datetime = max(curr_time, curr_task[0])
        curr_time += curr_task[1]

    return curr_time


if __name__ == "__main__":
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

    earliest_complete: datetime = scheduler(tasks)
    print(earliest_complete)
