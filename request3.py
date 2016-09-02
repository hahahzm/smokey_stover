import sys
import copy

def answer(document, searchTerms):
    # your code here
    # small inpu data
    # figure out all snippet first

    doc = document.split()

    dictionary = {}
    for word in searchTerms:
        dictionary[word] = 0
    for word in doc:
        if word in dictionary:
            dictionary[word] += 1

    start = 0
    end = len(doc)

    dictionary2 = copy.deepcopy(dictionary)

    for word in doc:
        if word in dictionary:
            if dictionary[word] > 1:
                dictionary[word] -= 1
                start += 1
            else:
                break
        else:
            start += 1

    for word in doc[::-1]:
        if word in dictionary:
            if dictionary[word] > 1:
                dictionary[word] -= 1
                end -= 1
            else:
                break
        else:
            end -= 1

    print start, end

    start2 = start
    end2 = end

    start = 0
    end = len(doc)

    dictionary = dictionary2

    for word in doc:
        if word in dictionary:
            if dictionary[word] > 1:
                dictionary[word] -= 1
                start += 1
            else:
                break
        else:
            start += 1

    for word in doc[::-1]:
        if word in dictionary:
            if dictionary[word] > 1:
                dictionary[word] -= 1
                end -= 1
            else:
                break
        else:
            end -= 1

    print start, end

    if ((end2 - start2) < (end - start)):
        end = end2
        start = start2


    result = ""
    for i in range(start, end):
        result = result + str(doc[i])
        if (i != (end - 1)):
            result = result + " "
    return result



#doc = raw_input(str("Paste doc here: "))
#terms = raw_input("Search Terms: ").split()
doc = "the thing the only thing"
terms = "the thing".split()
print answer(doc, terms)
