n = int(input())
seen = set()
for _ in range(n):
    text = input()
    if text not in seen:
        print(text)
        seen.add(text)
