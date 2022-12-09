# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path 


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(filter_bank_list):
    desired_file_name = input("File name for your qualifying loans: ")
    csvpath = Path(f"{desired_file_name}.csv")
    header = ["Lender" , "Max Loan Amount" ,"Max LTV" , "Max DTI" , "Min Credit Score" , "Interest Rate"]
    with open(csvpath, "w", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)           # write a header
        for row in filter_bank_list:         # write a list of filtered bank data
            csvwriter.writerow(row) 