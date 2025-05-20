import itertools

def func():
    n, m = map(int, input().split())
    cases = []

    for _ in range(n):
        bits = input().split()
        num = int(''.join(bits), 2)
        cases.append(num)
    target = (1 << m)-1

    for i in range(m):
        mask = 1 << i
        if not any((case & mask) != 0 for case in cases):
            print(-1)
            return

    for k in range(1, n+1):
        for combo in itertools.combinations(cases, k):
            total = 0
            for c in combo:
                total |= c
            if total == target:
                print(k)
                return

if __name__ == '__main__':
    func()