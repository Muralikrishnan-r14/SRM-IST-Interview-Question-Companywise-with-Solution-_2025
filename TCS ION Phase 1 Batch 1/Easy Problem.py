''' The problem statement is : Fetch the workout details for a week from the user
and return the sum and average of the workout duration in mins '''
#Soln
Sum = 0
for i in range(7):                       #A week contains 7 days so i directly declared end value as 7 in the loop
    n = int(input(f"Enter the workout duration of day{i+1} in mins:"))                # Refer line 10
    Sum += n
print(f"The sum of workout duration is: {Sum} mins")
print(f"The average workout duration is: {Sum//7}mins")


'''In Python, you can't concatenate different types (string and integer) directly within the input()
 function call so we are using f strings - formatted string literals is used enable string interpolation'''
# f-strings are faster than the older .format() method and manual concatenation,
# as they are evaluated at runtime and optimized for performance.


