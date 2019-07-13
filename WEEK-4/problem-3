def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    newHand = hand.copy()
    for i in word:
        newHand[i] = newHand.get(i, 0) - 1
        if newHand[i] == -1:
            return False
        
    if word not in wordList:
        return False
    
    return all(i in hand for i in word)
