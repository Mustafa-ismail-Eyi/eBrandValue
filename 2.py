# Soru 2: 5 milyondan küçük 3'e bölünebilen fibonacci sayıalrının toplamı
def fibonacci_numbers_divisible_by_three(max_number):
    # ilk iki terim
    n1, n2, nth = 0, 1, 0
    numbers = []

    while nth < max_number:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        # print(nth)
        if nth % 3 == 0:
            numbers.append(nth)

    # return sorted(numbers)
    return sum(numbers)


print(fibonacci_numbers_divisible_by_three(5000000))