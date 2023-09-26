# Basic Arithmetic Operations
# Write function calc(m, n) that multiplies two variables m and n of type int,
# then divides the product by two, and outputs the remainder with respect to division by 7.
def calc(m, n):
    return (m*n//2) % 7


# Statistics
# Count as well as sum up the natural numbers that are divisible by 2 or 7
# up to a given maximum value (exclusive) and output it to the console.
# Write function calc_sum_and_count_all_numbers_div_by_2_or_7(max_exclusive).
# Extend it so that it returns the two values instead of performing the console output.
def calc_sum_and_count_all_numbers_div_by_2_or_7(max_exclusive):
    divisors_of_2 = [number for number in range(1, max_exclusive) if number % 2 == 0]
    divisors_of_7 = [number for number in range(1, max_exclusive) if number % 7 == 0 and number not in divisors_of_2]
    return len(divisors_of_2) + len(divisors_of_7), sum(divisors_of_2) + sum(divisors_of_7)


# Perfect Numbers
# By definition, a natural number is called a perfect number if its value is equal to the sum
# of its real divisors. This is true, for example, for the numbers 6 and 28:
# Write function calc_perfect_numbers(max_exclusive) that calculates the perfect numbers
# up to a maximum value, say 10,000.
def calc_perfect_numbers(max_exclusive):
    pass


if __name__ == '__main__':
    print("Basic Arithmetic Operations:")
    print(calc(6, 7))
    print(calc(5, 5))

    print("Statistics:")
    print(calc_sum_and_count_all_numbers_div_by_2_or_7(3))
    print(calc_sum_and_count_all_numbers_div_by_2_or_7(8))
    print(calc_sum_and_count_all_numbers_div_by_2_or_7(15))
