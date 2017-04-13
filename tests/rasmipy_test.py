import csv
from os import path

from rasmipy import rasmify


DATA_FILE = path.abspath(path.join(path.dirname(__file__), 'quran_text_rasm.csv'))


def yield_test_data():
    with open(DATA_FILE, mode="r") as csv_data:
        csv_reader = csv.reader(csv_data, delimiter='\t')
        for row in csv_reader:
            if len(row) < 6:
                continue
            yield row[4].strip(), row[5].strip()
    raise StopIteration


def test_rasmify():
    for input, output in yield_test_data():
        assert rasmify(input) == output
