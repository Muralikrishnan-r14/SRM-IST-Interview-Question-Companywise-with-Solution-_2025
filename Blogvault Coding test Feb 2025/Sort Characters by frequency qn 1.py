'''Sort Characters by Frequency Given a string, sort and return its characters in decreasing
order based on their frequency of occurrence. If multiple characters have the same frequency,
sort them in alphabetical order'''
# Example: Input: "tree Output: "eetr" Explanation: 'e appears twice while and both appear once.
# So 'e' should come first, followed by and in alphabetical order.
# Example 2: Input: "cccaaa" Output: "cccaaa" Explanation: Both 'c' and 'a' appear three times,
# so they are sorted alphabetically. Constraints:
'''1<=string length <= 100
String contains only lowercase English letters
String will not be empty'''
def srt_by_frequency(string):
    from collections import Counter
    dic = Counter(string)
    s_dic = sorted(dic.keys(), key = lambda ch: (-dic[ch], ch))
    return "".join(ch * dic[ch] for ch in s_dic)
string = 'tree'
srt_by_frequency(string)

