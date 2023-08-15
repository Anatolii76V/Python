import csv
import random


class CSVGenerator:
    def generate_csv(self, filename, rows):
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for _ in range(rows):
                row = [random.random() for _ in range(3)]
                csv_writer.writerow(row)
