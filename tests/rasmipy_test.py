import unittest
from rasmipy import rasmify
import csv
import os

class RasmipyTestCase(unittest.TestCase):
    def test_rasmipy(self):

        # Read sample data
        sample_data = self.read_sample_data()

        # Iterate over all words
        for word in sample_data:

            # Get original arabic word with vocalization etc
            original_arab = word[4].strip()

            # Get target rasmified word without vocalization etc
            target_rasm = word[5].strip()


            self.assertEqual(target_rasm, rasmify(original_arab))



    def read_sample_data(self):

        """
        Read the sample data into an array
        :return: list 
        """

        # Set path to sample data file
        csv_file = os.path.join(os.getcwd(), "data/quran_text_rasm.csv")

        # Open file
        with open(csv_file, mode="r") as csv_data:

            # Parse file to csv reader data
            csv_reader = csv.reader(csv_data)

            # Parse data into a list
            sample_list = [x[0].split("\t") for x in list(csv_reader)]

            # Return data
            return sample_list

if __name__ == '__main__':
    unittest.main()
