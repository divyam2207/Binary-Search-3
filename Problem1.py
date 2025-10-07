"""
TC: O(log N) {The time complexity is logarithmic because the exponent 'n' is halved in every iteration of the while loop, drastically reducing the number of multiplications.}
SC: O(1) {The space complexity is constant as we only use a few variables (res, x, n) regardless of the size of the exponent.}

Approach:

This problem is solved using the Exponentiation by Squaring algorithm, which is an optimized way to calculate powers. This method leverages the binary representation of the exponent 'n' to perform the calculation in logarithmic time.

First, we handle the case where the exponent 'n' is negative by inverting the base x and making the exponent positive: 
x^n = (1/x)^-n .

We initialize the result to 1.0. The core of the algorithm is a loop that processes the exponent 'n' bit by bit. In each iteration, if the current exponent 'n' is odd, it means the current power of x is necessary for the final result, so we multiply res by x. We then square the base x and halve the exponent n. This iterative process efficiently computes x^n by only performing the necessary multiplications.

The problem ran successfully on LeetCode.
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1.0
        #handle negative n
        if n < 0:
            x = 1/x
            n *= -1
        
        while n > 0:

            if n%2 != 0:
                res *= x

            x *= x
            n = n//2
        
        return res