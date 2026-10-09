# to count  the sentence and no of words .


def count_sentence(s):
    list1 = list(s)
    no_of_sentence = 0
    no_of_words = 1
    for i in list1 :
        if i == "." or i == "!" or i == "?" :
            no_of_sentence += 1
        if i == " ":
            no_of_words += 1
    return no_of_sentence,no_of_words

print(count_sentence("Hello World! Welcome to the placement test. Are you ready?"))
    