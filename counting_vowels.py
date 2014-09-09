#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

s = str(raw_input("Enter a string: " ));
def vowels(string):
    count = 0
    for i in range (len(s)):
        if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or \
           string[i] == 'u':
           count = count + 1
    return count
print("Number of vowels: " + str(vowels(s)))
