def min_operations_to_seven(n):
    if '7' in str(n):
        return 0
    add = 9
    ops = 1
    while '7' not in str(n + add):
        if add > 10**9:  
            break
        add = add * 10 + 9  
        ops += 1
    return ops


def process_test_cases():
    t = int(input())  
    test_cases = [int(input()) for _ in range(t)]
    results = [str(min_operations_to_seven(n)) for n in test_cases]
    print("\n".join(results))


process_test_cases()
