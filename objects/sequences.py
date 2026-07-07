def square_numbers(n):
    """
    Generate the first n square numbers.

    Args:
        n (int): Number of square numbers to generate.

    Returns:
        list[int]: The first n cube numbers.
    """
    return [i**2 for i in range(1, n + 1)]

def cube_numbers(n):
    """
    Generate the first n cube numbers.

    Args:
        n (int): Number of cube numbers to generate.

    Returns:
        list[int]: The first n cube numbers.
    """
    return [i**3 for i in range(1, n + 1)]

def triangular_numbers(n):
    """
    Generate the first n triangular numbers.

    Args:
        n (int): Number of triangular numbers to generate.

    Returns:
        list[int]: The first n triangular numbers.
    """
    if n <= 0:
        return [i * (i + 1) // 2 for i in range(1, n + 1)]

def fibonacci(n):
    """
    Generate the first n fibonacci numbers.

    Args:
        n (int): Number of fibonacci numbers to generate.

    Returns:
        list[int]: The first n fibonacci numbers.
    """
    if n <= 0:
        return []

    seq = [0, 1]

    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])

    return seq[:n]

def prime_numbers(n):
    """
    Generate the first n prime numbers.

    Args:
        n (int): Number of primes to generate.

    Returns:
        list[int]: The first n prime numbers.
    """
    candidate = 2
    primes = []
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if (prime)**2 > candidate:
                break
            elif candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 1
    return primes