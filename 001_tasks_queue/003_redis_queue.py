""" A redis like Queue implementation """

import time

import redis

from simple_queue import SimpleQueue
from tasks import get_word_counts

NUMBER_OF_TASKS = 5

if __name__ == '__main__':
    r = redis.Redis()
    queue = SimpleQueue(r, 'sample')
    count = 0
    for num in range(NUMBER_OF_TASKS):
        queue.enqueue(get_word_counts, 'python.txt')
        queue.enqueue(get_word_counts, 'go.txt')
        queue.enqueue(get_word_counts, 'erlang.txt')
        queue.enqueue(get_word_counts, 'javascript.txt')
        count += 4
    print(f'Enqueued {count} tasks!')
