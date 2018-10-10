""" Task to be executed """

import collections
import json
import os
import sys
import time
import uuid

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIRECTORY = os.path.join(BASE_DIR, 'data')
OUTPUT_DIRECTORY = os.path.join(BASE_DIR, 'output')

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


if __name__ == '__main__':
    get_word_counts(sys.argv[1])
