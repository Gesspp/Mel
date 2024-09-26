def check(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

a = int(input())
b = int(input())
nums = []

for i in range(a, b + 1):
    if check(i):
        nums.append(i)
    else:
        continue

cnt = 0

for i in range(len(nums)):
    for j in range(i, len(nums)):
        if abs(i - j) == 2:
            cnt += 1
            print(i, j)

print(cnt)