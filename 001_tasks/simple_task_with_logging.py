""" Task Queue implementation with Logging """

import logging
import multiprocessing
import os
import time

from simple_task_queue import add_tasks, run
from tasks import get_word_counts

PROCESSES = multiprocessing.cpu_count() - 1
NUMBER_OF_TASKS = 3


def process_tasks(task_queue):
    """ Execute tasks in task queue """
    logger = multiprocessing.get_logger()
    proc = os.getpid()
    while not task_queue.empty():
        try:
            food = task_queue.get()
            get_word_counts(food)
        except Exception as e:
            logger.error(e)
        logger.info(f'Process {proc} completed successfully')
    return True


if __name__ == '__main__':
    multiprocessing.log_to_stderr(logging.ERROR)
    run()
