#import needed modules
import string
import random
#create list of different characters
al=[]
for letter in string.ascii_letters:
    al.append(letter)
nu=[]
for num in string.digits:
    nu.append(num)
spec_char=[]
for spec in string.punctuation:
    spec_char.append(spec)
#combine all characters into one list
final_lst=[]
final_lst.extend(al)
final_lst.extend(nu)
final_lst.extend(spec_char)
#get user inputs
length=int(input("ENTER THE LENGTH OF THE PASSWORD:"))
if (length<10):
    print("you entered less than 10")
    length=int(input("ENTER THE LENGTH OF THE PASSWORD(more than 10 character):"))
character=input("ENTER THE CHARACTER MUST BE IN THE PASSWORD:")
#enter user input into list
character_lst=[]
for i in character:
    character_lst.append(i)
number=input("ENTER THE NUMBER MUST BE IN THE PASSWORD:")
#enter user input list
number_lst=[]
for i in number:
    number_lst.append(i)
special=input("ENTER THE SPECIAL CHARACTER MUST BE IN THE PASSWORD:")
#enter user input list
special_lst=[]
for i in special:
    special_lst.append(i)
#combine all user input into a one list
given_lst=character_lst+number_lst+special_lst
#generate password with user's inputs
password=given_lst[:]
#if generate password is less than required password's length
if (len(password)<length):
    c=length-len(password)
    a=random.choices(final_lst,k=c)
    password.extend(a)
#shuffle the password to ensure the password is unpredictable
    random.shuffle(password)
    b="".join(password)
    print("GENERATED PASSWORD:",b)
#if generate password is greater than required password's length
elif(len(password)>length):
    print("Your entered more than",length)
#if generate password is equal to required password's length
else:
    random.shuffle(password)
    b="".join(password)
    print("GENERATED PASSWORD:",b)


    