# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Assignment6A.py

def bubbleSort(list):
    sort = True
    flipCount = 0
    if len(list)>1:
        while sort:
            flipCount = 0
            for i in range(len(list)-1):
                var, var1 = list[i], list[i+1]
                flipCount += 1 if list[i]>list[i+1] else 0
                if list[i]>list[i+1]:
                    list[i], list[i+1] = var1, var
            sort = True if flipCount>0 else False
    else:
        print("This list has less than 2 elements. It cannot be sorted.")
def countPositive(list):
    positive = 0
    for i in list:
        positive += 1 if i>=0 else 0
    return positive
def countNegative(list):
    negative = 0
    for i in list:
        negative += 1 if i<0 else 0
    return negative

flag = True
inputList = []
while flag:
    addToList = input('Type a number to be added to the list (type "done" to finish): ')
    if str(addToList).lower()=="done":
        flag = False
        break
    try:
        addToList = int(addToList)
        inputList.append(int(addToList))
    except:
        print(f"You entered {addToList}, which is an invalid input. Please try again.")

sortList = inputList.copy()
bubbleSort(sortList)
print(f"Input list: {inputList}")
print(f"Sorted list: {sortList}")
print(f"Positive numbers: {countPositive(inputList)}")
print(f"Negative numbers: {countNegative(inputList)}")