# Finding Patterns of Text Without Regular Expressions
#
def phoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


# # 452-464-4444
#
# text = str(input("Enter phone number"))
# print("is "+text+" phone number")
# print(phoneNumber(text))


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    #  [i:i+12] it is called slice notation. It allows you to cut out a bit of an array,
    #  you can treat string a bit like array in python.
    # in your example when i=0, message[i:i+12] will be message[0:12] this will get the
    # 0th character of the string upto but not including the 12, so will get output "Call me at 4"
    chunk = message[i:i + 12]
    if phoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
