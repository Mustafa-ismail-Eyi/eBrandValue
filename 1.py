#Soru 1: Asal çarpanları sadece 2, 3 veya 5'ten oluşan 1milyondan küçük doğal sayıların toplamını bulan fonksiyon yazınız.
from math import log
def numbers_include_prime_factors(max_number : int):
    
    temp = max_number
    max_divider = 0
    number_list = []

    
    # 2^0 x 3^0 x 5^0 'dan 2^temp x 3^temp x 5^temp ' e kadar sayılar çarpılarak 1 milyondan küçük olduğu kontrol edildi
    for i in range(0,int(log(max_number,2)+1)):
        for j in range(0,int(log(max_number,3)+1)):
            for k in range(0, int(log(max_number,5)+1)):
                temp = (2**i)*(3**j)*(5**k)
                if(temp < max_number):
                    number_list.append(temp)

    # 1 dahil edilmeyecek
    return sum(number_list[1:])



print(numbers_include_prime_factors(1000000))
