
# entrada
n = int(input())
m = int(input())

# USANDO O FOR
for i in range(n, m + 1):
    if i % 2 != 0:
        print(i)

# USANDO O WHILE
while n <= m:
    if n % 2 != 0:
        print(n)
        break
    n = n - 1
    