def average(a: float, b: float):
    """
    Returns the average of two numbers a and b.
    """
    sum = a + b
    return sum / 2

def main():
    # Example averages
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    
    # Find the average of the two averages
    final = average(avg_1, avg_2)
    
    # Print the results
    print("avg_1:", avg_1)
    print("avg_2:", avg_2)
    print("final average:", final)
    

# Boilerplate code to run main
if __name__ == '__main__':
    main()
