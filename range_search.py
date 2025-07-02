import sys
sys.setrecursionlimit(10000)

# Test arrays for range search
# L = [1,1,1,1,1,1,1]
L = [2,3,3,3,3,3]  # Sorted array with duplicates

def left (L, l, r, x):
    """
    Binary search to find the leftmost (first) occurrence of x in sorted array L
    Args:
        L: sorted array
        l: left boundary index
        r: right boundary index  
        x: target value to search for
    Returns:
        Index of leftmost occurrence of x, or None if not found
    """
    if (l>=r):
        if L[l] == x:
            return l
        else:
            return None
    index = int((l+r)/2)  # Calculate middle index
    if L[index] > x:
        return left(L,l,index-1,x)  # Search left half
    elif L[index] < x:
        return left(L,index+1,r,x)  # Search right half
    else:
        return left(L,l,index,x)    # Found x, continue searching left for first occurrence

def right (L, l, r, x):
    """
    Binary search to find the rightmost (last) occurrence of x in sorted array L
    Args:
        L: sorted array
        l: left boundary index
        r: right boundary index
        x: target value to search for
    Returns:
        Index of rightmost occurrence of x, or None if not found
    """
    if (l>=r):
        if L[r] == x:
            return r
        else:
            return None
    index = int((l+r+1)/2)  # Calculate middle index (biased right for last occurrence)
    if L[index] > x:
        return right(L,l,index-1,x)  # Search left half
    elif L[index] < x:
        return right(L,index+1,r,x)  # Search right half
    else:
        return right(L,index,r,x)    # Found x, continue searching right for last occurrence

# Test the functions
print(left(L, 0, 5, 2))   # Find leftmost occurrence of 2
print(right(L, 0, 5, 2))  # Find rightmost occurrence of 2

# Check if element exists in array
if (left(L, 0, 5, 2) == None):
    print(0)  # Element not found

