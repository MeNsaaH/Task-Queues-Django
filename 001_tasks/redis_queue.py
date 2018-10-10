""" A redis like Queue implementation """

import pickle
import uuid


class SimpleQueue:
    """ Simple Queue for Task """
    def __init__(self, conn, name):
        self.conn = conn
        self.name = name

    def enqueue(self, func, *args):
        """ Add elements to Queue """
        task = SimpleTask(func, *args)
        serialized_task = pickle.dumps(task, protocol=pickle.HIGHEST_PROTOCOL)
        self.conn.lpush(self.name, serialized_task)
        return task.id

    def dequeue(self):
        """ Remove Elements from Queue """
        _, serialized_task = self.conn.brpop(self.name)
        task = pickle.loads(serialized_task)
        task.process_task
        return task

    def get_length(self):
        """ Return length of queue"""
        return self.conn.llen(self.name)


class SimpleTask:
    """ Task """
    def __init__(self, func, *args):
        self.id = str(uuid.uuid4)
        self.func = func
        self.args = args

    def process_task(self):
        """ Process task """
        self.func(*self.args)
