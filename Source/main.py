Context = str()
ReversedContext = str()

Context = input("Please Enter Your Text : ")

ReversedContext = Context[::-1]

if (Context == ReversedContext):
    print("Your Text Is A Palindrome")
else:
    print("Your Text Is Not A Palindrome")