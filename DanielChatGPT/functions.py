'''
LAB 5
Functions
'''

def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    ans = 0
    
    if x < 0 or y < 0:
        ans = x - y
        
    else:
        print( x, y )
        ans = recurse( x-1, y ) + recurse( x, y-1 )
        
    return ans



def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    
    if m % n == 0:
        ans = n
        
    else:
        ans = gcd( n, m % n )
        
    return ans



def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    count = 0
    vowels = 'aeiou'
    char = 0
    
    if s == '':
        count
    
    else:
        print( count )
        if s[char] not in vowels:
            char += 1
            vowel_count(s)
            
        else:
            char += 1
            count += 1
            vowel_count(s)

    return count



    #
    #
    #
    # vowels = "aeiou"
    # count = 0
    #
    # for c in s:
    #     if c.lower() in vowels:
    #         count = count + 1
    #
    # return count
    #


def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """
    ans = 0

    if power == 1:
        ans = base
        
    elif power < 1 
        
    else:
        print( base, power )
        base = base * base
        to_power( base, power - 1 )
        
    return ans



def is_palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    
    
    
    
    

    
    
    
    
    
    