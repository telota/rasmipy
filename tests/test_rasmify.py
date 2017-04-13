import csv
from os import path
import unicodedata

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
        try:
            assert rasmify(input) == output
        except AssertionError:
            processed = ':'.join(unicodedata.name(x) for x in rasmify(input))
            expected = ':'.join((unicodedata.name(x) for x in output))
            assert processed == expected
