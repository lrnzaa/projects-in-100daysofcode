def reverse(s):
    temp = ""
    for i in s:
        temp = i + temp

    return temp

def check(s):
    w2 = reverse(s)

    if s == w2:
        return True
    else:
        return False

print("Palindrome")
print("----------")
string = input("Enter your words here: ")

print("Checking...")

result = check(string)

if result == True:
    print(string + " is a palindrome.")
else:
    print(string + " is not a palindrome.")