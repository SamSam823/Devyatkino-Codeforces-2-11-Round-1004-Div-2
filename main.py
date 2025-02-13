def min_operations_to_make_seven(t, test_cases):
    results = []
    
    for n in test_cases:
        count = 0
        while '7' not in str(n):  
            count += 1
            n += int('9' * count)  
        results.append(count)
    
    return results

#preset test cases cuz replit devs are greedy and i couldn't test input
test_cases = [80, 999, 555, 777]
t = len(test_cases)


results = min_operations_to_make_seven(t, test_cases)
for result in results:
    print(result)
