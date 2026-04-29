#Stop gninnipS My sdroW!

def spin_words(sentence):
    s = sentence.split()
    string = []
    for i in s :
        if len(i) >= 5 :
            string.append(i[::-1])
        else :
            string.append(i)
    
    return " ".join(string)



d = spin_words("This is a test")
print(d)


