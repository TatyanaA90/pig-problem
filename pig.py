def pig_latin(sentence):
    # Write your solution here!
    words = sentence.split()
    new_words_list = []
    vowel = "a,e,i,o,u"

    for word in words:
        if word[0] in vowel:
            new_words_list.append(word)
        else:
            new_words = word[1:] + word[0] + "ay"
            new_words_list.append(new_words)

    return " ".join(new_words_list)

print(pig_latin("Hello"))


# Test cases
assert pig_latin("something") == "omethingsay"
assert pig_latin("awesome") == "awesome"
assert pig_latin("latin is a hard language") == "atinlay is a ardhay anguagelay"
assert pig_latin("y") == "yay"
assert pig_latin("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")