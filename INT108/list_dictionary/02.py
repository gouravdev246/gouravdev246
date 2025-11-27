#Given a list of words, count the frequency of each word using a dictionary.
# l = ["apple" , "banana" , "apple" , "grape" , "banana" , "apple"]
# n = int(input("Number of Words:"))
# words = []
# for i in range(n):
#     x = input("Word : ")
#     words.append(x)
# word_dict ={}
# for word in words:
#     if word not in word_dict:
#         word_dict[word] = 1
#     else:
#         word_dict[word] += 1
# print(word_dict)

from collections import Counter

n = int(input("Number of Words: "))
words = [input("Word: ") for _ in range(n)]
word_dict = Counter(words)
print(dict(word_dict))

