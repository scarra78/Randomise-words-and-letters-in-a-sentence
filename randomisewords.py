from random import shuffle
from collections import Counter
import random

ist = input("Enter a sentence: ") 
print(ist)


st = ist.split()  #turns string into a list 
count_each_word = Counter(st)
print(count_each_word) #counts how many times each word is used 
print(len(st)) #counts how many words in the list
shuffle(st) # shuffles the words in the list  
print (st)

st=["".join(random.sample(st ,len(st))) for st in st] #jumbles letters in the words in list 
print(st) 

# str=" ".join([str(elm) for elm in st])
# print(str)

#or

# str=" " # important note must keep a space between quotes or it will join all words 
# print (str .join(st))

#or 

str=" " .join(st) #turns list in to string by removing commas
print (str)