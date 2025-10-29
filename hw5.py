# # # #program that takes list of integers and prints the numbers and count that appears more than 1

def moreThanOnce (inputList):
    countDone = []
    for i in range (len(inputList)):
        if ( inputList.count(inputList[i]) > 1 and inputList[i] not in countDone ):          #checking if multiple time appeared and already counted or not

            print (f"{inputList[i]} is appeared { inputList.count(inputList[i])} times in the list)" )
            countDone.append(inputList[i])


numberList=[1,5,4,7,8,7,4,8,9,5]
moreThanOnce(numberList)            



# # #show common number on 2 list and unique numbers in both lists 
list1 = [1,2,3,4]
list2 = [5,6,3,4]

common = []

for i in list1:
    if i in list2 and i not in common:
        common.append(i)

unique1 = []
unique2 = []
for i in list1:
   if i not in list2:
       unique1.append(i)        

for i in list2:
   if i not in list1:
       unique2.append(i)        

print ("common in both lists are: ", common)
print ("unique to list1 : ", unique1)
print ("unique to list2 : ", unique2)


# # #counting number of vowel in a string

def countingVowel (text):
    text = text.lower()
    count = 0
    vowels = ["a","e","i","o","u"]
    for char in text:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            count += 1

    return count        

userText = input("enter your text: ")
totalVowel = countingVowel(userText)
print (f"total number of vowel in the text is: {totalVowel}")


# # #sorting the elements of a list of tuples (str,int) based on their integer value

listedTuple= [("john",85),("jane",93),("david",37),("cena",34)]

(listedTuple.sort(key=lambda item: item[1]) )     # found this technique on online
print (listedTuple, "\nascending order based on integer value")
 

(listedTuple.sort(key=lambda item: item[1], reverse=True) )
print (listedTuple, "\ndescending order based on integer value") 


# # showcase the odd, even number of a list

listOddEven = [1,2,3,4,5,6,7,8,9,10]
for i in listOddEven:
    if i % 2 == 0:
        print (f"{i} is even number")
    else:
        print (f"{i} is odd number")


##merging 2 dictionary by adding values for common keys & keeping unique keys as it is

dictionary1 ={ 'a':100, 'b':200, 'c':300 }
dictionary2 ={ 'a':300, 'b':200, 'd':400, 'e':500 }
newDictionary = {}

for i in dictionary1:
    if i in dictionary2:
        newDictionary[i] = dictionary1[i] + dictionary2[i]

    else:
        newDictionary[i] = dictionary1[i]

for i in dictionary2:
       if i not in newDictionary:
            newDictionary[i] = dictionary2[i]
           

print (newDictionary)