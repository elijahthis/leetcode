from collections import defaultdict

def convert(rates, source, target):
    graph = defaultdict(list)

    # Build bidirectional graph
    for src, dst, rate in rates:
        graph[src].append((dst, rate))
        graph[dst].append((src, 1 / rate))

    visited = set()

    def dfs(curr, rate):
        if curr == target:
            return rate
        visited.add(curr)

        for neighbor, r in graph[curr]:
            if neighbor not in visited:
                result = dfs(neighbor, rate * r)
                if result:
                    return result
        return None

    return dfs(source, 1)

# Example usage
rates = [
    ['USD', 'JPY', 110],
    ['USD', 'AUD', 1.45],
    ['JPY', 'GBP', 0.0070]
]

print(round(convert(rates, 'GBP', 'AUD'), 2))  # Output: 1.89
