'''To solve the problem, we need to count the number of desktop products in the given list of product IDs.
 According to the problem statement, the laptop products have product IDs from a, i, e, o, u, A, I, E, O, U,
 and the rest are desktop products'''
'''Input:n=6, 'a v i k e l', output = 3'''
def cntdesktopprdt(productid):
    laptop_ids = set('aieouAIEOU')
    desktop_count = 0
    for product in productid:
        if product not in laptop_ids:
            desktop_count += 1
    return desktop_count
productid='avizOkel'
print(cntdesktopprdt(productid))
'''Time Complexity: O(n), n is length of the product string
Space Complexity: O(1), as the additional space used does not scale with the input size.'''