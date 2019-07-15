from functools import reduce as fold

#adding numbers to give a total
total = fold(lambda item, running_total: item + running_total,[1,2,3,4,5])
print(total)

def join_strings(listofwords):# joining list of words
    return fold(lambda item, running_total: item  +  running_total,listofwords)
words = ["Johnson ","is ", "great"]
joinwords = join_strings(words)
print(joinwords)