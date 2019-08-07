def count_letters(word_list):
    """ See question description """

    ALPHABET = "abcdefghijklmnopqrstuvwxyz"


    letter_count = {}
    for letter in ALPHABET:
        letter_count[letter] = 0

    for word in word_list:
        for letter in word:
            res = ALPHABET.find(letter)
            if res != -1:
                    letter_count[letter] = letter_count[letter] + 1

    max_num = 0
    for dic in letter_count:
        if letter_count[dic] > max_num:
            max_num = letter_count[dic]

    for dic in letter_count:
        if letter_count[dic] == max_num:
            Letter = dic

    for key, value in letter_count.items():
        print(key,value)


    return Letter, max_num

monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"

monty_words = monty_quote.split(" ")

print(count_letters(monty_quote))