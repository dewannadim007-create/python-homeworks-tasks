#1
# hw-1 colorspace conversion is a common process in image processing. suppose you are given a color image (RGB) write a python function 
# that convert the image to grayscale (BW) hints: RGB image has 3 channels but grayscale image has only one. 
# Formula: Grayscale= 0.299R + 0.587G + 0.114B

print("Problem 1: RGB to Grayscale Conversion")
rgb = [[[60, 57, 88], 
        [73, 10, 70], 
        [90, 69, 60]], 
            
        [[80, 40, 45],
        [124,170,36],
        [15, 35, 90]],

        [[0, 23, 120],
        [67, 150, 5],
        [135,78,199]]
        ]

def convertToGray (rgbList):
    grayscaleList = []
    for element in rgbList:
        for rgbValue in element:
            new = int(0.299 * rgbValue[0] + 0.587 * rgbValue[1] + 0.114 * rgbValue[2])
            grayscaleList.append(new)

    return grayscaleList 

print (convertToGray(rgb))

#2
#Number Guessing Game
#Create a python function where the user has to guess a secret number within 5 tries.

print("Problem 2: Number Guessing")
import random
hiddenNum = random.randint(0,100)

print ("a hidden number has been  (from 0 to 100), you have 5 attempt left to guess the right one.")
chance = 5
atempt = 0
answer = False

while (chance > atempt):
    try:
        guess = int(input(f"this is your attempt number {atempt + 1 }: "))
    except ValueError:
        print("enter only integer")
        continue
    
    if (guess == hiddenNum):
            print(f"congratulation!!!!!! the number was indeed {hiddenNum}.")
            answer = True
            break
    else:
            print("try again!")
            atempt += 1
            


    if ( answer == False and chance <= atempt): 
      print(f"Sorry no chances left. The number was {hiddenNum}")
#3
#Flattened
# You are given a 2D list; make a python function that will return a 1D list preserving the elements' position.
# The child lists should have the same length; if not, raise a proper error.

print("Problem 3: 2d to 1d Conversion")
twoDList = [[10,30,80],
            [60,70,30],
            [30,41,87],
            [66,85,23],
            [24,86,32]]

def convertToOneD (twoD):
     oneDList=[]
     for element in twoD:
          index = len (element)
          for i in range (index):
            oneDList.append(element[i])
          
     return oneDList      

print (f"from 2d to 1d :: {convertToOneD(twoDList)}")   


#4
#You are given a 2D list; return a 2D list where the first child list contains the average of each row and 
# the second list contains the average of each column
print("Problem 4: Average of Rows and Columns")

twoDList2 = [[10,30,30],
            [50,20,30],
            [30,1,27],
            [6,45,23],
            [24,66,72]]

def avgOfRow(twoD):
     avgRowList = []
     for element in twoD:
          count = len (element)
          sum = 0
          for i in range (count):
            sum += element[i]
            avg = round (sum / count, 4)
          avgRowList.append(avg)
     return avgRowList

print (f"avgOfRow: {avgOfRow (twoDList2)}")

def avgOfCol(twoD):
    avgColList = []  
    firstColumn = []
    secondColumn = []
    thirdColumn = []

    for element in twoD:
        firstColumn.append(element[0])
        secondColumn.append(element[1])
        thirdColumn.append(element[2])

    count1 = len(firstColumn)
    sum1 = 0
    for i in range(count1):
        sum1 += firstColumn[i]
    avg = round(sum1 / count1, 4)
    avgColList.append(avg)
    
    count2 = len(secondColumn)
    sum2 = 0
    for i in range(count2):
        sum2 += secondColumn[i]
    avg = round(sum2 / count2, 4)
    avgColList.append(avg)
    
    count3 = len(thirdColumn)
    sum3 = 0
    for i in range(count3):
        sum3 += thirdColumn[i]
    avg = round(sum3 / count3, 4)
    avgColList.append(avg)

    return avgColList

print (f"avgOfCol: {avgOfCol (twoDList2)}")    