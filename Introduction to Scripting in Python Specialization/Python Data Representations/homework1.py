def count_vowels(word):
    n = 0
    for x in range(0,len(word)):
        if word[x] == "a" or word[x] == "e" \
                or word[x] == "i" or word[x] == "o" \
                or word[x] == "u":
            n = n + 1
    return n

#print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
#print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))

def demystify(li_string):
    str = li_string.replace("l","a")
    str1 = str.replace("1","b")
    return str1


print(demystify("lll111l1l1l1111lll"))
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))

