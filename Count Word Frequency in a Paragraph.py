para = input("enter a paragraph:")

para = para.lower()

words = para.split()

word_freq = {}
for word in words :
    if word in word_freq:
        word_freq[word]+=1
    else :
        word_freq[word] = 1
    pass

for word , count in word_freq.items() :
    print(word ,":",count)