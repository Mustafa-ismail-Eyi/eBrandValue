# Soru 3: 3 haneli sayıların çarpımından elde edilen  en büyük palindrom sayısını bulan fonksiyon

def largest_palindrome_number() -> int:

    n = 0
    for i in range(999,99,-1):
        for j in range(i,99,-1):
            x = i*j
            if x > n:
                s = str(x)
                if s == s[::-1]:
                    n = x
    
    return n



print(largest_palindrome_number())