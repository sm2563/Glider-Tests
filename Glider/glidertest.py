strg = "asddv123ads2345sad65"

numb = []
ls = list(strg)
# print(ls)
temp = ''
for i in range(len(ls)):
    j = ls[i]
    # print(j, ls[i], j.isnumeric(), ls[i].isnumeric())
    if j.isnumeric():
        temp += j
        if i == len(ls) - 1:
            numb.append(temp)
            # temp = ''
    else:
        # print(temp)
        if temp:
            numb.append(temp)
            temp = ''

# print(numb)
numb.sort(key=lambda data: int(data))
print(numb[-1])