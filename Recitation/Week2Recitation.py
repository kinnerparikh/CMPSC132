def translate(translation, msg):
    words = msg.lower().split(' ')
    stringList = []
    for word in words:
        stringList.append(translation.get(word, word))
    return ' '.join(stringList)