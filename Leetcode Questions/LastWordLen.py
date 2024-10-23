def LastWordLen(sentence):
    wordList = sentence.split()
    print(wordList)
    return len(wordList[-1])
    


sentence = "Hello World  nighttttt   "
print(LastWordLen(sentence))
    