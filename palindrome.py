def isPalindrome(foo):
    foo = foo.lower().replace(' ', '')
    return foo == foo[::-1]

foo = input("Enter a string for Palindrome check: ")
foo_pal = isPalindrome(foo)

if foo_pal:
    print("True")
else:
    print("False")
    