def collatz_steps(n: int) -> int:
    memo = {1: 0}

    def collatz_steps_memo(n: int) -> int:
        if n in memo:
            return memo[n]
        if n % 2 == 0:
            memo[n] = 1 + collatz_steps_memo(n // 2)
        else:
            memo[n] = 1 + collatz_steps_memo(3 * n + 1)
        return memo[n]

    return collatz_steps_memo(n)
