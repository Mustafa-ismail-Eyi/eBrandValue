# Soru 7: tiny.cc/isimlistesi adresindeki isim listesini download edip alfabetik olarak sıralayınız.
# sıralama için quick sort kullanınız
# tekrar eden isimleri siliniz
# bu işlemlerden sonra skor dönmelisiniz
# ["AHMET"]
# birinci sırada olduğu için 1
# A = 1, H = 10, M=16, E=6, T=24
#skor => 1 x (1 + 10 + 16 + 6 + 24)


import requests, json
import pandas as pd

# download data and save it as txt file
def download_data():
    # chrome -> network -> any response -> headers -> user-agent otherwise it will throw error
    headers = {'User-Agent':'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    url = "http://tiny.cc/isimlistesi"
    data = requests.get(url=url, headers=headers,).content.decode()
    with open('./data.txt', 'w+') as file:
        file.write(data)



def read_data() -> str:
    with open(file='data.txt', mode='r+') as file:
        data = file.read()
    return data
    
def return_index_letter(letter) -> int:
    alphabet =    { 'A':1,
                    'B':2,
                    'C':3,
                    'Ç':4,
                    'D':5,
                    'E':6,
                    'F':7,
                    'G':8,
                    'Ğ':9,
                    'H':10,
                    'I':11,
                    'İ':12,
                    'J':13,
                    'K':14,
                    'L':15,
                    'M':16,
                    'N':17,
                    'O':18,
                    'Ö':19,
                    'P':20,
                    'R':21,
                    'S':22,
                    'Ş':23,
                    'T':24,
                    'U':25,
                    'Ü':26,
                    'V':27,
                    'Y':28,
                    'Z':29,
                    ' ': 0}
    return alphabet[letter]


# returns names score without multiplying their place score
def score_without_index(row) -> int:
    total = 0
    for char in row:
        total  = total + return_index_letter(char.capitalize())
    return total

# returns score with multiplying place score
def final_score(row, index):
    return row * (index+1)


def manupulate_data():


    # read data from txt file and load it as data frame
    data = pd.DataFrame(read_data().split('\n'),columns=['Names'])
    # dropping duplicates
    data.drop_duplicates(inplace=True)
    #sortin in quicksort
    data.sort_values(by=['Names'],kind='quicksort',inplace=True)
    data.reset_index(drop = True, inplace=True)
    data['index'] = data.index.values
    # dealing with mathematical stuff
    data['Score'] = data['Names'].apply(score_without_index)
    data['Final_Score'] = (data['index'] + 1) * data['Score']

    print(data.head())
    print("Skor toplamları", sum(data['Final_Score']))

manupulate_data()

