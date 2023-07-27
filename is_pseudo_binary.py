def sum_of_divisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

def is_pseudo_binary(number):
    if number <= 0:
        return False
    return number & (number - 1) == 0


n = int(input())
divisor_sum = sum_of_divisors(n)
c = is_pseudo_binary(divisor_sum)
if c == False:
    print(0)
else:
    print(1)