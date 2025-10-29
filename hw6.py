#hw6.2 : you have a list of numbers;output;- a list containing indices of odd numbers .

only_num = []
elem = int(input("how many elements you want :")) + 1
for i in range (1, elem):
    n = int(input("enter number:"))
    only_num.append(n)

odd= []
for i in only_num:
    if (i%2)!= 0:
        odd.append(only_num.index(i))   #using this technique have an issue: if same element comes multiple times then
                                        #only the index of the first one is showing 
print ("index numbers of odd elements is:",odd)    




#  hw6.1build a proper pyramid:

user_input = int(input("enter the number of total floors in the pyramid:"))
for i in range (1, user_input + 1):
    print(" " * (user_input - i) + "* " * i)


#hw6.3. 
# You will be given an image as a 2d list. The pixel values can be in the range of [0,255] 
# but sometime the range can be narrow. modify the given image so that:
# find absolute min and absolute max from the image
# use min-max normalization to scale the to range of [0, 255]
# Example:

# Original Image (narrow range): 
# [[100, 105, 110, 105] 
# [105, 115, 120, 115] 
# [110, 120, 125, 120] 
# [105, 115, 120, 115] ]

# Normalized Image (stretched to full range [0, 255]): 
# [[0, 51, 102, 51] 
# [51, 153, 204, 153] 
# [102, 204, 255, 204] 
# [51, 153, 204, 153]]


original = [[100, 105, 110, 105], 
            [105, 115, 120, 115], 
            [110, 120, 125, 120], 
            [105, 115, 120, 115]]
normalized = []

# new range = [0,255]
#normalizing value formula = (actual - min)* 255 / (max-min)    
# initally didnt used *255, but when ans was not coming right then used gpt
#and told to use *255 to get the desired ans

lowest= original[0][0]     # sobar prothom value ke low, high mone kora
highest = original[0][0]

for element in original:
    for value in element:
        if value < lowest:
            lowest = value
        if value > highest:
            highest = value    

print (lowest, highest)     #original tar min, max

for i in range (len(original)):
    element = len(original[i])

    for j in range (element):
      current = original[i][j]
      new = ( (current - lowest) *255  / (highest-lowest) ) 
      normalized.append(int(new))
print(normalized)
