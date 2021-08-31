def translate(translation, msg):
    #creates list of strings from the message based on space
    words = msg.lower().split(' ')
    stringList = []

    for word in words:
        stringList.append(translation.get(word, word)) #adds the translation to the list

    return ' '.join(stringList)


