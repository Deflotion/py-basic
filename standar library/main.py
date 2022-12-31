import datetime

data_waktu = datetime.datetime.now()
print(f"Date now: {data_waktu}")
print(f"Tahun: {data_waktu.year}")
print(f"Hari: {data_waktu.strftime('%A')}")


from collections import Counter

data = ["a","c","b","d","a","b","a","a","c"]
data_count = Counter(data)
print(f"Hasilnya: {data_count}")
print(f"Jumlah a: {data_count['a']}")
print(f"Jumlah b: {data_count['b']}")
print(f"Jumlah c: {data_count['c']}")
print(f"Jumlah d: {data_count['d']}")

import io

file = io.open("file_test.txt","r")
print(file.read())