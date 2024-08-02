
escape_codes = """
\n = new line feed
\r = Carriage Return
\t = Tab
\' = Literal single quote
\" = Literal double quote
\\ = Literal backslash
"""
print(escape_codes)

print ("new line  \n feed (new line)")
print ("new line  \r feed")
print ("new line  \t feed")
print ("good morning \'s'")
print ("good morning \"s")
print ("good morning \\s")

message = 'good \'s';
print("\n",message)

#string slicing \indexing
message = "Learning python for data engineering"

print ("\nstring  from the 9th postion: ",message[9:])
print ("string till 9th postion: ",message[:9])
print ("String from the 9th position till 15th position: ",message[9:15])

print ("\nLast 5 character from the string: ",message[-5:])
print ("From 5th position to len-3 postion: ",message[5:-3])
print ("Till len-3 postion: ",message[:-3])
print ("Length of string: ",len(message))
print ("Reversal of string: ",message[::-1])
print ("Last 5 character from the string: ",message[-1::])

print ("\nno of 'in' in the message: ",message.count("in"))
print ("Upper case message",message.upper())
print ("Find position of 'in' in the message: ",message.find("in"))
print ("Find position of 'in' in the message from position 9: ",message.find("in",9))
print ("Find position of 'in' in the message from position 29 till 35: ",message.find("in",29,35))
print ("Split the message: ",message.split())
print ("Split the message: ",message.split("in"))
