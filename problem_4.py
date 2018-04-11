'''Reverse a String
Write a reverse_string(string) function that reverses a string. For example: "bananas" -> "sananab".

It has one parameter:

string - the string to be reversed
Return value: a string - the reversed version of the string passed in.

Write some extra code to test this function and verify that it works properly.'''

    
'''this is the correct way to do this problem'''
    
    
    def reverse(string):
    string = "".join(reversed(string))
    print (string)
    return string

string = "bananas"
reverse(string)

'''not this way'''

def reverse(string):
string = "".join(reversed(string))
    return string
string = "bananas"
reverse(string)

string = input("bananas")
reverse_string(string)

def reverse_string(string):
    result =[]
    string = string.split()
    string.reverse()
    result = "".join(string)
    print (result)
string = ["bananas"]  
reverse_string(string)


result = []
    for letter in string:
        letter+= result
        result.reverse()
    print(result)
    
    
