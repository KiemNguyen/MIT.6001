def laceString(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    
    # Find the remainder
    if len(s1) > len(s2):
        (s1, remainder) = (s1[0:len(s2)], s1[len(s2):])
    elif len(s2) > len(s1):
        (s2, remainder) = (s2[0:len(s1)], s2[len(s1):] )
    else:
        remainder = ''
    
    # Loop over 2 strings with same lenght, lace the character and add remainder     
    char = []
    for i in range(len(s1)):
        char.append(s1[i])
        char.append(s2[i])
    result = ''.join(char) + remainder
    return result
    
print(laceString('abcd', 'efghi'))
