n = input()
binary_list = []

def replace(n, m, a):
    n_list = list(n)
    n_list[m] = a
    return ''.join(n_list)
def listOfBinary(n):
        if '?' not in n:
            return [n]

        index = n.index('?')
        n_zero = replace(n, index, '0')
        n_one = replace(n, index, '1')
        list_zero = listOfBinary(n_zero)
        list_one = listOfBinary(n_one)

        return list_zero + list_one
l = listOfBinary(n)
for i in l:
    binary_list.append(int(i))
binary_list2 = sorted(binary_list ,reverse= True)
for i in binary_list2:
    print(i)