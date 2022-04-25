
# 2
def fibonaccis_to_n(n):
    def fibonacci(n, x, y, fibs):
        if x <= n:
            fibs.append(x)
        else:
            return fibs
        return fibonacci(n, y, x + y, fibs)
        
    return fibonacci(n, 0, 1, [])

# 3, 7, 10
def primes_to_n(n):
    # Sieve of Eratosthenes
    primes = [False] * 2 + [True] * (n - 1)
    
    for i in range(2, int(n ** (1 / 2)) + 1):
        if primes[i]:
            for multiple in range(i ** 2, n + 1, i):
                primes[multiple] = False

    return [i for i, prime in enumerate(primes) if prime]

# 18, 67
def bottom_up(pyramid, base_i):
    new_base = lambda j: pyramid[base_i - 1][j] + max(pyramid[base_i][j], pyramid[base_i][j + 1])
    pyramid[base_i - 1] = [new_base(j) for j in range(len(pyramid[base_i - 1]))]

    if base_i == 1:
        return pyramid
    return bottom_up(pyramid, base_i - 1)