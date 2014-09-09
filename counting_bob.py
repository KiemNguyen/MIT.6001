#Assume s is a string of lower case characters.

#Write a program that prints the number of times the string 'bob' occurs in s.
#For example, if s = 'azcbobobegghakl', then your program should print

#Number of times bob occurs is: 2

s = str(raw_input("Enter a string: " ))

def repeat_words(string):
    count = 0
    for i in range(len(s)):
        if s[i:].startswith('bob'):
            count = count + 1
    return count
print("Number of times bob occurs is: " + str(repeat_words(s)))
