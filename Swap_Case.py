
def swap(sentence):
    res = ""
    for word in sentence:
        for letter in word:
            if letter.isupper():
                res = res + letter.lower()
            else:
                res = res + letter.upper()
    return res

sentence = input("----Enter the sentence to convert-------\n")
print("-----The sentence after conversion-----\n",swap(sentence))