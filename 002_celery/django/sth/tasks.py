""" Celery task """

from __future__ import absolute_import, unicode_literals

import collections
import json
import os
import time
import uuid

from celery import chain, chord, group, shared_task
from django.conf import settings

from demo.celery import app

DATA_DIRECTORY = os.path.join(settings.BASE_DIR, 'data')
OUTPUT_DIRECTORY = os.path.join(settings.BASE_DIR, 'output')

# Use `shared_task` when declaring a django tasks
# The tasks you write will probably live in reusable apps, and reusable apps cannot
# depend on the project itself, so you also cannot import your app instance directly.
# The @shared_task decorator lets you create tasks without having any concrete app instance:
# To call our task you can use the `delay()` method
# Calling a task returns an AsyncResult instance.
# This can be used to check the state of the task,
# wait for the task to finish, or get its return value
# (or if the task failed, to get the exception and traceback)..


@shared_task
def some_task():
    """ Some task """
    get_word_counts('python.txt')
    get_word_counts('go.txt')
    get_word_counts('erlang.txt')
    get_word_counts('javascript.txt')
    return "Task Done"


def save_file(filename, data):
    """ saves a text file with filename and populate with data """
    random_str = uuid.uuid4().hex
    # Create Output Directory if not exists
    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
    outfile = os.path.join(OUTPUT_DIRECTORY, f'{filename}_{random_str}.txt')
    with open(outfile, 'w') as outfile:
        outfile.write(data)


def get_word_counts(filename):
    """ get count of words in filename and saves most common"""

    wordcount = collections.Counter()
    # get counts
    with open(os.path.join(DATA_DIRECTORY, filename), 'r') as f:
        for line in f:
            wordcount.update(line.split())
    # save file
    save_file(filename, json.dumps(dict(wordcount.most_common(20))))
    # simulate long-running task
    time.sleep(2)
    proc = os.getpid()
    print(f'Processed {filename} with process id: {proc}')


# CANVAS WORKFLOWS

# Some Tasks to Do
@app.task
def add(x, y):
    return x + y


@app.task
def subtract(x, y):
    return x - y


@app.task
def mul(x, y):
    return x * y


@app.task
def div(x, y):
    return x / y

@app.task
def xsum(numbers):
    return sum(numbers)


# Chain Tasks
# Tasks can be linked together so that after one task returns the other is called
# The return value of one tasks is used as first parameter of the other
# The return value can be gotten using the `.get()` method of a task
@shared_task
def run_chain_tasks():
    # tasks are chained using Signatures of the task `task.s(params)`
    return chain(add.s(3, 8) | subtract.s(8) | div.s(2) | mul.s(7))

    # It can also be more conveniently
    # return (add.s(3, 8) | subtract.s(8) | div.s(2) | mul.s(7))().get


# Group Tasks
# A group calls a list of tasks in parallel, and it returns a special result instance
# that lets you inspect the results as a group, and retrieve the return values in order.

@shared_task
def run_group_task():
    return group(add.s(i, i) for i in range(10))()

@shared_task
def partial_group():
    return group(add.s(i) for i in range(10))


# Chords
# Chords are groups with callbacks

@shared_task
def run_chord_tasks():
    chord((add.s(i, i) for i in range(10)), xsum.s())()
