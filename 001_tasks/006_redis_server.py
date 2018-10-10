# redis_queue_server.py

import multiprocessing

import redis

from simple_queue import SimpleQueue
from worker import NoTaskException, worker

PROCESSES = 4


def run():
    """ Executes worker on all queues"""
    num_tasks = SimpleQueue(redis.Redis(), 'sample').get_length()
    processes = []
    print(f'Running with {PROCESSES} processes!')
    while num_tasks > 0:
        try:
            for w in range(PROCESSES):
                p = multiprocessing.Process(target=worker)
                processes.append(p)
                p.start()
                num_tasks -= 1
                if num_tasks < 1:
                    break
            for p in processes:
                p.join()
        except NoTaskException:
            break


if __name__ == '__main__':
    run()
