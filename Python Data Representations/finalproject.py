"""
This is my final project
Dimon Yin

Mark: 100% achieved!!!
"""

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    if len(line1) == len(line2):
        for letter in range(0,len(line1)):
            if line1[letter] != line2[letter]:
                return letter

        return -1

    elif len(line1) > len(line2):
        for letter in range(0,len(line2)):
            if line2[letter] != line1[letter]:
                return letter

        return len(line2)

    elif len(line1) < len(line2):
        for letter in range(0, len(line1)):
            if line1[letter] != line2[letter]:
                return letter

        return len(line1)


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    for letter in range(0, len(line1)):
        if line1[letter] == "\n" or line1[letter] == "\r":
            return ""
    for letter in range(0, len(line2)):
        if line2[letter] == "\n" or line2[letter] == "\r":
            return ""

    if len(line1) == len(line2):
        if idx > len(line1) or idx < 0:
            return ""

    elif len(line1) > len(line2):
        if idx > len(line2) or idx < 0:
            return ""
    elif len(line1) < len(line2):
        if idx > len(line1) or idx < 0:
            return ""

    string = "=" * idx + "^"

    return line1 + "\n" + string + "\n" + line2 + "\n"

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """

    if len(lines1) == len(lines2):
        for lis in range(0, len(lines1)):
            if singleline_diff(lines1[lis], lines2[lis]) == -1:
                pass
            else:
                return lis, singleline_diff(lines1[lis], lines2[lis])
        return -1,-1

    if len(lines1) > len(lines2):
        for lis in range(0, len(lines2)):
            if singleline_diff(lines1[lis], lines2[lis]) == -1:
                pass
            else:
                return lis, singleline_diff(lines1[lis], lines2[lis])
        return len(lines2), 0

    if len(lines1) < len(lines2):
        for lis in range(0, len(lines1)):
            if singleline_diff(lines1[lis], lines2[lis]) == -1:
                pass
            else:
                return lis, singleline_diff(lines1[lis], lines2[lis])
        return len(lines1), 0

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    file = open(filename)
    list1 = list()
    for line in file:
        line = line.strip('\n')
        list1.append(line)

    return list1

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    filelist1 = get_file_lines(filename1)
    filelist2 = get_file_lines(filename2)
    diff = multiline_diff(filelist1, filelist2)

    if diff == (-1, -1):
        return "No differences\n"
    else:
        if len(filelist1) == 0 and len(filelist2) != 0:
            line1 = ""
            line2 = filelist2[diff[0]]
            idx1 = singleline_diff(line1, line2)
            diff1 = singleline_diff_format(line1, line2, idx1)
            linenum = str(diff[0])
            finalanswer = "Line " + linenum + ":" + "\n" + diff1
            return finalanswer
        elif len(filelist2) == 0 and len(filelist1) != 0:
            line2 = ""
            line1 = filelist1[diff[0]]
            idx1 = singleline_diff(line1, line2)
            diff1 = singleline_diff_format(line1, line2, idx1)
            linenum = str(diff[0])
            finalanswer = "Line " + linenum + ":" + "\n" + diff1
            return finalanswer
        else:
            line1 = filelist1[diff[0]]
            line2 = filelist2[diff[0]]
            idx1 = singleline_diff(line1, line2)
            diff1 = singleline_diff_format(line1, line2, idx1)
            linenum = str(diff[0])
            finalanswer = "Line " + linenum + ":" + "\n" + diff1
            return finalanswer