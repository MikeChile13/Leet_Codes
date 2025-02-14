class ProductOfNumbers:

    def __init__(self):
        self.lastZero = 0 
        self.prefixProduct = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefixProduct.append(self.prefixProduct[-1])
            self.lastZero = len(self.prefixProduct)-1
        else:
            self.prefixProduct.append(self.prefixProduct[-1]*num)

    def getProduct(self, k: int) -> int:
        stop = len(self.prefixProduct) - k - 1
        if stop < self.lastZero:
            return 0
        return self.prefixProduct[-1] // self.prefixProduct[stop]

#maintain a prefix product skiping zeros.
#maintain a zero prefix array adding zeros.        
#if no zeros in range return the answer from the given range.
#otherwise return zero.

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)