""" Worker to Execute Redis Queue"""

import redis

from simple_queue import SimpleQueue


def worker():
    """ Worker to execute task """
    r = redis.Redis()
    queue = SimpleQueue(r, 'sample')
    if queue.get_length() > 0:
        queue.dequeue()
    else:
        print('No tasks in the queue')


if __name__ == '__main__':
    worker()
