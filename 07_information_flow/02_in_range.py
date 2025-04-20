# def in_range(n, low, high):
#     """
#     Returns True if n is between low and high, inclusive. 
#     high is guaranteed to be greater than low.
#     """
#     if low <= n <= high:
#         return True
#     return False



def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if low <= n <= high:
        return True
    return False

def main():
    # Test examples
    print(in_range(5, 1, 10))  # Should print True
    print(in_range(0, 1, 10))  # Should print False
    print(in_range(10, 1, 10)) # Should print True
    print(in_range(7, 5, 7))   # Should print True
    print(in_range(3, 5, 7))   # Should print False

if __name__ == '__main__':
    main()
