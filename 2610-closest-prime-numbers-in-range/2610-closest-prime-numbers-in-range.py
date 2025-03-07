class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        isPrime = [True] *(right + 1)
        isPrime[0] = isPrime[1] = False
        primeNumbers = []

        num1,num2 = left - 1,right + 1
        
        for i in range(right + 1):
            if isPrime[i]:
                if i >= left:
                    primeNumbers.append(i)
                    if len(primeNumbers) > 1:
                        diff = primeNumbers[-1] - primeNumbers[-2]
                        if diff < 3:
                            return primeNumbers[-2:]
                        if diff < num2 - num1:
                            num1,num2 = primeNumbers[-2:]

                for j in range(i * i, right + 1, i):
                    isPrime[j] = False

        return [-1, -1] if num1 < left or num2 > right else [num1, num2]