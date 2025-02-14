class ProductOfNumbers:

    def __init__(self):
        self.zeros = [0]
        self.prefixProduct = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefixProduct.append(self.prefixProduct[-1])
            self.zeros.append(self.zeros[-1]+1)
        else:
            self.prefixProduct.append(self.prefixProduct[-1]*num)
            self.zeros.append(self.zeros[-1])

    def getProduct(self, k: int) -> int:
        stop = len(self.prefixProduct) - k - 1
        zeroCount = self.zeros[-1] - self.zeros[stop]
        if zeroCount:
            return 0
        product = self.prefixProduct[-1] // self.prefixProduct[stop]
        return product

#maintain a prefix product skiping zeros.
#maintain a zero prefix array adding zeros.        
#if no zeros in range return the answer from the given range.
#otherwise return zero.

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)