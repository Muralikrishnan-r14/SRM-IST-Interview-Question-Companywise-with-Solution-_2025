# Return the string without repeating elements , the string contains upper case and lower case characters
# Test Case Input='HAPpY NeW YeAR', Output='HaPpY NeW R'
#Better soln
def repeat(str):
    st=''
    for i in str:
        if i not in st:
            st+=i
    return st
#optimal soln
def optimalsoln_repeat(str):
    seen=set()
    st=''
    for char in str:
        if char not in seen:
            seen.add(char)
            st += char
    return st

str = "HAPpY NeW YeAR"
print(optimalsoln_repeat(str))
# Test cases
'''test_cases = [
    "HAPpY NeW YeAR",  # Case with mixed case letters and spaces
    "AAABBBCCC",       # Case with repeating characters
    "abcdefghijk",     # Case with all unique characters
    "AaBbCcDdEeFf",    # Case with alternating case characters
    "",                # Empty string
    "Mississippi",     # Case with repeating characters, different cases
    "1234567890",      # Numeric characters
    "111222333444555", # Repeated numbers
    "abcdefghijklmnopqrstuvwxyz",  # All lowercase letters
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",  # All uppercase letters
    "a"*1000 + "b"*1000,  # Large input with repeating characters
]'''
#difference between optimalsoln and better soln
'''function taking significantly longer on larger inputs (like a*1000 + b*1000),
this highlights the inefficiency due to th time complexity O(n2)
optimized code will handle all the same test cases much more efficiently,
particularly for large inputs, while maintaining the correct results'''






