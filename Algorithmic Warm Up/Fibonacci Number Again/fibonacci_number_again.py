# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    fn = [0, 1]
    is_pisano_period = False

    if n >= 2:
        index = 2
        while not is_pisano_period:
            fn.append(0)
            fn[index] = (fn[index-1]+fn[index-2])%m
            if index == n:
                return fn[index]
            is_pisano_period = True if (fn[index-1]==0 and fn[index]==1) else False
            index += 1
    else:
        return fn[n]

    fn = fn[:len(fn)-2]
    sequence_length = len(fn)
    sequence_index = n%sequence_length
    return fn[sequence_index]


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
