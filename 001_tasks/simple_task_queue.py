# simple_task_queue.py

import multiprocessing
import time

from tasks import get_word_counts

PROCESSES = multiprocessing.cpu_count() - 1
NUMBER_OF_TASKS = 3


def process_tasks(task_queue):
    """ Execute tasks in task queue """
    while not task_queue.empty():
        food = task_queue.get()
        get_word_counts(food)
    return True


def add_tasks(task_queue, number_of_tasks):
    """ Add tasks to a task Queue """

    for num in range(number_of_tasks):
        task_queue.put('go.txt')
        task_queue.put('python.txt')
        task_queue.put('javascript.txt')
        task_queue.put('erlang.txt')
    return task_queue


def run():
    """ Initializer"""

    empty_task_queue = multiprocessing.Queue()
    full_task_queue = add_tasks(empty_task_queue, NUMBER_OF_TASKS)
    processes = []
    print(f'Running with {PROCESSES} processes!')
    start = time.time()
    for n in range(PROCESSES):
        # Create a new process with independent memory and resources
        p = multiprocessing.Process(
            target=process_tasks, args=(full_task_queue,)
        )
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    print(f'Time taken = {time.time() - start:.10f}')


if __name__ == '__main__':
    run()
