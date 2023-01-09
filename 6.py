# Soru 6: verilen cümledeki kelimelerin ortalama uzunluğunu bulan fonksiyon yazının noktalama işaretleri dahil değil
import re
def get_str_avg_length(string : str):
    splitted_string_letter_counts = [len(x) for x in re.sub(r'[^\w\s]', '',string = string).split(' ') ]
    return round(sum(splitted_string_letter_counts) / len(splitted_string_letter_counts), 2)

print(get_str_avg_length('Elma, portakal, armut'))