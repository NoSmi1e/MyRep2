def quick_merge(lists):
    numbers = []
    for current_list in lists:
        numbers.extend(current_list)
    numbers.sort()
    return numbers


n = int(input())
lists = []

for _ in range(n):
    numbers = list(map(int, input().split()))
    lists.append(numbers)

result = quick_merge(lists)
print(*result)
