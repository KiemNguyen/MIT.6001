import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    listOfLetters = string.ascii_lowercase
    result = []
    
    for char in listOfLetters:
        if char not in lettersGuessed:
            result += char
    #Conver list to String
    result = ''.join(result)
    return result
