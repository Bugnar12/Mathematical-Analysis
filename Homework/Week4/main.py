import math

print("the value of natural log of 2 is ~= ", math.log(2))

media = 0
nr = 0
for n in range(500, 10001, 500): #from 500 ->10001 jumping 500 elements at each step
    sum = 0 #the sum that is specified in the exercise
    sign = -1 #the sign that is raised to a specific power
    for i in range(1, n + 1):
        sign = -1 * sign #this instruction alternates the value of the sign 1,-1,1,-1...
        sum = sum +sign/i
    media = media + sum
    nr = nr + 1 #we are incrementing the specified number
    print("considering", n, "elements, the sum of the sequence is : ", sum)

media = media / nr
print("Overall: ", media)
print("As a conclusion, we can observe that for increasing elements the sum approaches closer and closer"
      "to the value of the log(2), which was computed in the first line")
