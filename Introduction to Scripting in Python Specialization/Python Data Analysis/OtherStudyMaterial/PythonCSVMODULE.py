"""
Using the csv module.
"""

import csv

def parse(csvfilename,separator,quote):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a list of lists.
    """
    table = []
    with open(csvfilename, "r") as csvfile:
        csvreader = csv.reader(csvfile,
                               delimiter=separator,
                               quotechar=quote)
        for row in csvreader:
            table.append(row)

    list1 = table[0]
    print(list1)

parse("hightemp.csv", ',', '"')


def print_table(table):
    """
    Print out table, which must be a list
    of lists, in a nicely formatted way.
    """
    for row in table:
        # Header column left justified
        print("{:<19}".format(row[0]), end='')
        # Remaining columns right justified
        for col in row[1:]:
            print("{:>4}".format(col), end='')
        print("", end='\n')

#table = parse("hightemp.csv")
#print_table(table)

#print("")
#print("")

#table2 = parse("hightemp2.csv")
#print_table(table2)