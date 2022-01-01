n = int(input())
up = "* " * (n//2 + n%2)
down = " *" * (n//2)

for i in range(n):
    print(up + "\n" + down if n != 1 else up)
