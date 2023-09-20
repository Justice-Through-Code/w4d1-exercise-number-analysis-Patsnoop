#number_range_analysis.py

'''
Implement Number Analysis Functions

- Function to calculate the sum of numbers within the range.
- Function to find the smallest number within the range.
- Function to find the largest number within the range.
- Function to count the number of even numbers within the range.
- Function to count the number of odd numbers within the range.

'''
# TODO: IN A COMMENT WITHIN EACH DEF, WRITE PSEUDOCODE FOR EACH SOLUTION

def calculate_sum(start, end):
    """
    Calculate the sum of numbers within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The sum of numbers within the range.
    """
    # TODO: Implement the logic to calculate the sum of numbers within the range.
    # TODO: Return the calculated sum.

    # Initialize a variable "sum" to 0
    sum = 0

    # Loop from start to end (inclusive)
    for number in range(start, end + 1):
        # Add the current number to "sum"
        sum += number

    #  Return the calculated sum
    return sum
# calculate_sum()


def find_smallest_number(start, end):
    """
    Find the smallest number within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The smallest number within the range.
    """
    # TODO: Implement the logic to find the smallest number within the range.
    # TODO: Return the found smallest number.

    # Using the min function to return the smallest value in a range of numbers
    lowest_number = min(range(start, end + 1))

    # Return the lowest number
    return lowest_number


def find_largest_number(start, end):
    """
    Find the largest number within the specified range.

    Args:
        start (int): The starting number of the range ( inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The largest number within the range.
    """
    # TODO: Implement the logic to find the largest number within the range.
    # TODO: Return the found largest number.

    # Using the max function to find the largest number in the range
    largest_number = max(range(start, end + 1))

    # Return the largest number
    return largest_number

def count_even_numbers(start, end):
    """
    Count the number of even numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of even numbers within the range.
    """
    # TODO: Implement the logic to count even numbers within the range.
    # TODO: Return the count of even numbers.

    # Initialize a count for the amount of even numbers
    even_count = 0

    # Iterate through the range to count even numbers
    for number in range(start, end + 1):
        # If the current number is divisible with a remainder of 0, increase the count by 1
        if number % 2 == 0:
            even_count +=1
        
    # Return the count of even numbers
    return even_count

def count_odd_numbers(start, end):
    """
    Count the number of odd numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of odd numbers within the range.
    """
    # TODO: Implement the logic to count odd numbers within the range.
    # TODO: Return the count of odd numbers.

    # Initialize a count for the amount of odd numbers
    odd_count = 0

    # Iterate through the range to count odd numbers
    for number in range(start, end + 1):
         # If the current number is not divisible with a remainder of 0, increase the count by 1
        if number % 2 != 0:
            odd_count +=1

    # Return the count of odd numbers 
    return odd_count