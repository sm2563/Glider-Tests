str = "2020 1111 2321 2222 60000 2231 9"

ls = str.split(' ')
ls.sort()
ls.sort(key=lambda data: sum(int(i) for i in list(data)))

print(ls)