'''Vowel Count
Write a vowel_count(string) function that counts the # of vowels for a given string. It has one parameter:

string - the string to be counted
It has one return value: a number representing the number of vowels in the string.

After you've written this function. Write some extra code to test this function and verify that it works properly.'''

def vowel_count(string):
    count = 0
    vowels = "aeiou"
    for letter in string:
        if letter in vowels:    
            count += 1
    print (count) 
    return (count)
    
string = "this is a test run from kris"        
vowel_count(string)
count_variable = vowel_count(string)