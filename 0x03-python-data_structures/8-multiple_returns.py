#!/usr/bin/python3
def multiple_returns(sentence):
    # If the sentence is empty, return None for the first character
    if not sentence:
        return (0, None)

    # Otherwise, return the length of the sentence and its first character
    return (len(sentence), sentence[0])
