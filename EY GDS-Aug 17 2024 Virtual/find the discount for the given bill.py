'''An e-commerce company plans to give their customers a discount.
The discount will be calculated on the basis of the total bill of the order placed.
The discount amount is the sum of all the odd digits in the customer's total bill.
If no odd digit Is present in the total bill, then the discount will be zero.'''

'''Input:The input consists of an integer - billAmount, representing the customer's total bill.
Output:Print an integer representing the discount for the given total bill'''

'''Input:2514795, Output:27'''

def discountbill(billamount):
    discount= 0
    for num in billamount:
        num=int(num)
        if num % 2 != 0:
            discount+=num
    return discount

str="2514795"
print(discountbill(str))

'''Time complexity is O(d), where d is the number of digits in billAmount'''
'''Space complexity is O(1)'''
