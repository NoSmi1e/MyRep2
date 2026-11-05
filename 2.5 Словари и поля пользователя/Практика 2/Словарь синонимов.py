synonyms = {}
for _ in range(int(input())):
    first, second = input().split()
    synonyms[first] = second
    synonyms[second] = first
print(synonyms[input()])
