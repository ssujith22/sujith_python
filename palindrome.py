'''
1.check the input string is palindrome or not

2.in the given paragraph
Next, lets create a redux store to hold our applications state.
in the src directory, create a new file called store.js.
inside this file, import the configurestore function from @reduxjs/toolkit and your todoslice reducer.
then use configurestore to create the redux store.

find the total no of vowels from the given paragraph
find the total no of consonants from the given paragraph witnout any punctuation
find the total number of words in the paragraph
'''

'''
my_string = "malayalam"
my_string = my_string.casefold()
rev_String = reversed(my_string)
if list(my_string) == list(rev_String):
    print ("string is palindrome")
else:
    print ("string is not a palindrome")

'''

String = raw_input("enter string:")
vowels = 0
for i in string:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i== 'u' or i=='A' or i=='E' or i=='I' or i=='O' or i== 'U'):
        vowels = vowels+1
print("No of vowels are: ")
print(vowels)
        

