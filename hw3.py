# function to clean an inpt text as:
# rmv spcl char
# rep bad==> negative
# good ==> positive
#  then print



def cleanerBoy (user_text):
    user_text= user_text.lower()
    a= user_text.replace("bad","negative")
    b= a.replace("good","positive")
    special_character = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in special_character:
        b= b.replace(char, "")
       
    b = b.replace("\n", " ")
    print("modified one is:",b)
 


from_user = input("enter any line/statement (including bad, good, special char):")
cleanerBoy(from_user)



# make a function that will take two numbers and print the result of their sum, subtraction, multiplication and division

def arithmetic(first, second):
    sum = first + second
    sub= first - second
    multiply= first * second
    divide= first / second

    print ("Sum:", sum, " Subtraction:", sub, " Multiplication:", multiply, " Division:", divide)

num1= float(input("enter first number:"))
num2= float(input("enter second number:(dont give zero)"))
arithmetic(num1, num2)



# . make a function that will take a text and retrun list of word from the text. the text may contain punctuation,  special characters and newlines

def text_to_word(text):
    special_character = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in special_character:
        text= text.replace(char, "")

    word = text.split()
    print("words list:", word)


user_text = input("enter text with punctuation, special characters and newlines:")
text_to_word(user_text)



