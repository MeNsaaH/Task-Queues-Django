""" Worker implementation """

import redis

from simple_queue import SimpleQueue


class NoTaskException(Exception):
    """ when no task in the Queue """
    pass

def worker():
    """ Worker to execute task """
    r = redis.Redis()
    queue = SimpleQueue(r, 'sample')
    if queue.get_length() > 0:
        queue.dequeue()
    else:
        raise NoTaskException
