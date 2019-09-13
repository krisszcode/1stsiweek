numbers=[]
num_of_nums=int(input("Give me the a number of numbers:"))
for i in range(num_of_nums):

    num=int(input("number " + str((i+1)) + ". "))
    numbers.append(num)

print(numbers)

iterations=1
for iterations in range(len(numbers)):
    
    for j in range(len(numbers)-1):

       if numbers[j]>numbers[j+1]:
            temp=numbers[j+1]
            numbers[j+1]=numbers[j]
            numbers[j]=temp

print(numbers)