#!/usr/bin/python3
def multiple_returns(sentence):
    new_sentence = ()
    if len(sentence) == 0:
        new_sentence = 0, "None"
    else:
        new_sentence = len(sentence), sentence[0]
    return new_sentence
