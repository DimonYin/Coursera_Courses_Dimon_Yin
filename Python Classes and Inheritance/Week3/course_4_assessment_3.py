# The function mySum is supposed to return the sum of a list of numbers (and 0 if that list is empty),
# but it has one or more errors in it. Use this space to write test cases to determine what errors there are.
# You will be using this information to answer the next set of multiple choice questions.

import test

test.testEqual(mySum([1,2]), 3)
test.testEqual(mySum([]), 0)

# test-4-1: Which of the following cases fail for the mySum function?
# A. an empty list
# B. a list with one item
# C. a list with more than one item

# Answer: A and C

# test-4-2: Are there any other cases, that we can determine based on the
# current structure of the function, that also fail for the mySum function?
# A. Yes
# B. No

# Answer: B

import test


#testing class constructor (__init__ method)
p = Student("Dimon", 4)
test.testEqual(p.name, "Dimon")
test.testEqual(p.years_UM, 4)
test.testEqual(p.knowledge, 0)

test.testEqual(p.study(), 0)
test.testEqual(p.getKnowledge(), 1)
test.testEqual(p.knowledge, 1)
test.testEqual(p.year_at_umich(), 4)


# test-4-3: Which of the following cases fail for the Student class?
# A. the method study does not return None
# B. the optional integer in the constructor is not optional
# C. the attributes/instance variables are not correctly assigned in the constructor
# D. the method study does not increase self.knowledge
# E. the method year_at_umich does not return the value of self.years_UM

# Answer: C and D

# test-4-4: Are there any other cases, that we can determine based on the current structure of the
# class, that also fail for the Student class?
# A. Yes
# B. No

# Answer: A
