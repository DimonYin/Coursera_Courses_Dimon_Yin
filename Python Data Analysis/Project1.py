"""
This is my week 3 project
Dimon Yin
"""
import csv

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      A list of strings corresponding to the field names in
      the given CSV file.
    """
    table = []
    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile,
                               delimiter=separator,
                               quotechar=quote)
        for row in csvreader:
            table.append(row)

    list1 = table[0]
    return list1

def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    table = []
    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile,
                               delimiter=separator,
                               quotechar=quote)
        for row in csvreader:
            table.append(row)

    dic1 = {}
    dic2 =[]

    lis = read_csv_fieldnames(filename, separator, quote)
    # 1 2 3 4

    for row in range(1,len(table)):
        for con in range(0,len(table[row])):
            for num in range(0, len(lis)):
                if num == con:
                    dic1[lis[num]] = table[row][con]
        dic2.append(dic1)
        dic1 = {}

    return dic2

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}
    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   delimiter=separator,
                                   quotechar=quote)
        for row in csvreader:
            table[row[keyfield]] = row
    return table

def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    newtable = []
    newtable1 =[]

    for row in table:
        for name in fieldnames:
            newtable.append(row[name])
        newtable1.append(newtable)
        newtable = []

    with open(filename, "w", newline='') as filename:
        csvwriter = csv.writer(filename,
                               delimiter=separator,
                               quotechar=quote,
                               quoting=csv.QUOTE_NONNUMERIC)
        csvwriter.writerow(fieldnames)

    for dic in newtable1:
        csvwriter.writerow(dic)

    filename.close()