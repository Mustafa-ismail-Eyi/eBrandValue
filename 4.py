# Soru 4: 10101. asal sayıyı bulduran fonksiyon

def given_nth_prime_number(num):
    count = 1
    n = 0
    nth_prime = 0
    while(count != num):
        if is_prime(n):
            count+=1
            nth_prime = n
        n += 1
    return nth_prime

def is_prime(num):
    for i in range(2,num//2+2):
        if num % i == 0:
            return False
    if num < 2:
        return False
    return True

print(given_nth_prime_number(10101))