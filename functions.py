import re
import random

def remove_non_letters(x):
    y = re.sub("[^' 'a-zA-Z]+", "", x)          #removing all elements which are not letters or spaces

    return y

def words_to_shuff(x):

    words_to_shuffle = []

    for i in x:                                 #this loop is responsible for proper selection of words that should be shuffled
        count = 0                               #the requirement: the smallest number of unique elements (letters) between first and last letter in
        unique = []                             #the word should be equal to 2. It automaticly rejects 1, 2, and 3-letter words and  words
        for j in range(len(i)):                 #like 'biiiig' which obviously would look exactly the same after shuffling
            if j != 0 and j != (len(i)-1):
                if i[j] not in unique:
                    count += 1
                    unique.append(i[j])
        if count > 1:
            words_to_shuffle.append(i)

    return words_to_shuffle

def word_to_replace(x):                         #auxilary function checking if word has to be replaced
    count = 0                                   #by word from shuffled_words
    unique = []
    for j in range(len(x)):
        if j != 0 and j != (len(x) - 1):
            if x[j] not in unique:
                count += 1
                unique.append(x[j])
    if count > 1:
        return True
    else:
        return False

def shuffler(x):
    shuffled_words = []

    temp_array = []

    for i in range(len(x)):                     #this algorithm just create temporary arrays: first one with
        temp1 = x[i][0]                         #the first letter, last with the last and middle part. It is done
        temp2 = x[i][len(x[i]) - 1]             #to simplify the process of shuffling itself. It happens inside only
        temp3 = []                              #with the middle part of the word. Then everything is joined back.
        for l in range(1, len(x[i]) - 1):
            temp3.append([x[i][l]])
        str3 = ''.join(sum(temp3, []))          # joining firstly 1-element lists (letters) inside and then joining the whole list
        while True:
            str4 = ''.join(random.sample(str3, len(str3)))
            if str4 != str3:
                temp_array.append(str4)
                break
        shuffled_words.append(''.join([temp1, temp_array[i], temp2]))

    return shuffled_words


def word_swap(x,y):                             #swapping principle - swaps proper words from the
    j = 0                                       #initial array with all shuffled words
    for i in range(len(x)):
        if word_to_replace(x[i]) is True:
            x[i] = y[j]
            j += 1
    return x



