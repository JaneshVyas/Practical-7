# ID-20CS102   Name-Janesh Vyas

# Lapindrome is defined as a string which when split in the middle, gives two
# halves having the same characters and same frequency of each character. If there
# are odd number of characters in the string, we ignore the middle character and
# check for lapindrome. For example gaga is a lapindrome, since the two halves ga
# and ga have the same characters with same frequency. Also, abccab, rotor and
# xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome.
# The two halves contain the same characters but their frequencies do not match.
# Your task is simple. Given a string, you need to tell if it is a lapindrome.
# Input:
# 6
# gaga
# abcde
# rotor
# xyzxy
# abbaab
# ababc
# Output:
# YES
# NO
# YES
# YES
# NO
# NO

# check all words if word has even length divide word and sort it if all letters have same frequency
# print yes else no and if the word have odd length discard the center letter and divide rest of word 
# in two parts if both parts have same frequency of all letters print yes else print no

total_words = int(input())
for i in range(total_words):
    word = input()
    word_length = len(word)
    if word_length%2 == 0:
        first = word[:word_length//2]
        second = word[word_length//2:]
    else:
        first = word[:word_length//2]
        second = word[(word_length//2)+1:]
    if sorted(first) == sorted(second):
        print("YES")
    else:
        print("NO")
