"""
Example code to read and parse a CSV file.
"""

def parse(csvfilename):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a list of lists.
    """
    table = []
    table1 = []
    with open(csvfilename, "r") as csvfile:
        for line in csvfile:
            line = line.rstrip()
            columns = line.split(',')
            table.append(columns)

    for i in range(0,len(table)):
        for j in range(0, len(table[i])):
            if i == 0:
                table1.append(table[i][j])
    print(table1)
    #return table

parse("hightemp.csv")


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