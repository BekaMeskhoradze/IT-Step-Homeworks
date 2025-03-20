import concurrent.futures

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51]

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(is_prime, num_list))

for num, result in zip(num_list, results):
    print(f"{num} არის {'მარტივი' if result else 'არა მარტივი'}")
