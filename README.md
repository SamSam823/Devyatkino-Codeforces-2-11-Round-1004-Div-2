# Devyatkino-Codeforces-2/11-Round-1004-Div-2
This is a fairly difficult solution I thought I could post, since problem D was interactive and I got cooked (even though it said there will be an interactive problem smh). Btw I was kinda lazy on this one but pls enjoy!

To solve this problem, we need to determine the minimum number of operations required to make a number n contain at least one digit '7' in its decimal representation. Each operation consists of adding a positive integer whose decimal representation contains only the digit 9.


We can break down the solution by checking if the number already contains a '7': If the number n already contains the digit '7', no operation is needed, and the answer is 0.

Otherwise, add a number with only 9s: In each operation, we add a number that contains only the digit 9 (e.g., 9, 99, 999, etc.) to n. The goal is to find the smallest such number to make n contain a '7' after the addition. The logic is to keep adding numbers that contain only 9s (increasing in size: 9, 99, 999, etc.) and check whether n has a '7' in its decimal representation. Keep track of the number of operations required.

Efficient search:

For each test case, we check whether the current number contains a '7' after each addition of a number with only 9s. Since the maximum value of n is 10^9, we only need to perform a limited number of operations because the sum will eventually cover the range that includes a '7'.

Solution:
We can implement this approach with a loop that starts by checking if the number contains a '7'. If not, keeps adding numbers consisting of the digit '9' until a '7' is encountered in the result. 

Notes: I used python because of my experience with "for n in range():", While loops, and parsing in python.
