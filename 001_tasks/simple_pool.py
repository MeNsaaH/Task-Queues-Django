""" simple Pool to execute task in Queue"""
import multiprocessing

# The Queue class, also from the multiprocessing library, is a basic FIFO
# (first in, first out) data structure. It’s similar to the queue.Queue class,
# but designed for interprocess communication.
# We used `put` to enqueue an item to the queue and `get` to dequeue an item.

def run():
    """ Execute a simple Queue with multi processing Library"""

    foods = [
        'eba',
        'amala',
        'tuwo',
        'akpu',
    ]
    queue = multiprocessing.Queue()

    print('Enqueuing...')
    for food in foods:
        print(food)
        queue.put(food)

    print('\nDequeuing...')
    while not queue.empty():
        print(queue.get())


if __name__ == '__main__':
    run()
