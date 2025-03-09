class Solution:
    def countPrimes(self, n: int) -> int:
        if not n or n == 1:
            return 0
        
        isPrime = [True] *(n)
        isPrime[0] = isPrime[1] = False
        primeNumbers = 0

        for i in range(n):
            if isPrime[i]:
                primeNumbers+=1
                for j in range(i * i, n, i):
                    isPrime[j] = False
        
        # print(primeNumbers,isPrime)
        return primeNumbers