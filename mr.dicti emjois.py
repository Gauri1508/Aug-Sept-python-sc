def emojis(message):
    words=message.split(" ")
    emo={
        ":)":"☺️",
        ":(":"😔"
    }
    output = " "
    for word in words:
        output += emo.get(word, word) + " "
    return output


message = input(">")
print(emojis(message))
