#!/usr/bin/python3
def multiple_returns(sentence):
    en = len(sentence)
    ch = sentence[0]
    if sentence is None:
        return ((0, None))
    else:
        return ((en, ch))
