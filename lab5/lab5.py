from collections import deque

def solve():
    with open('input.txt', 'r', encoding='utf=8') as f:
        lines = [line.split('#')[0].strip() for line in f]
        lines = [line for line in lines if line]

        if not lines:
            return

        root = int(lines[0])
        graph = {}

        for line in lines[1:]:
            u, v = map(int, line.split(','))
            if u not in graph:
                graph[u] = []
            graph[u].append(v)

        queue = deque([(root, 1)])
        min_depth = 0

        while queue:
            node, depth = queue.popleft()

            if node not in graph or not graph[node]:
                min_depth = depth
                break

            for child in graph[node]:
                queue.append((child, depth + 1))

        print(min_depth)

        with open('output.txt', 'w', encoding='utf=8') as f:
            f.write(str(min_depth))

if __name__ == '__main__':
    solve()