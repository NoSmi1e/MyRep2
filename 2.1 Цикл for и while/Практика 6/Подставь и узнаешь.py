n = int(input())
m = int(input())
found = False

for a in range(1, n):
    for b in range(1, n):
        for c in range(1, n):
            if a + 3 * b + 2 * c == m:
                print(f"{a} + 3×{b} + 2×{c} = {m}")
                found = True

if not found:
    print("При заданных n и m решений не существует.")
