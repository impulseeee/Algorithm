
from collections import deque
def func():
    n, m = map(int, input().split())
    covers = []
    for _ in range(n):
        row = list(map(int, input().split()))
        covers.append(row)

    module_coverd = [False] * m
    for row in covers:
        for i in covers:
            for i in range(m):
                if row[i] == 1:
                    module_coverd[i] = True
    if not all(module_coverd):
        print(-1)
    else:
        masks = []
        for row in covers:
            mask = 0
            for i in range(m):
                if row[i] == 1:
                    mask |= 1 << i
            masks.append(mask)

    full_mask = (1<<m) -1

    visited = {}
    queue = deque()
    queue.append((0,0))
    visited[0] = 0
    ans = -1

    while queue:
        current_mask, count = queue.popleft()
        if current_mask == full_mask:
            ans = count
            break
    for mask in masks:
        new_mask = current_mask |mask
        new_count = count + 1
        if new_mask not in visited or new_count<visited.get(new_mask, float('inf')):
            visited[new_mask] = new_count
            queue.append((new_mask, new_count))

    print(ans if ans != -1 else -1)

if __name__ == '__main__':
    func()
