class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def count_set_bits(num):
            return bin(num).count('1')
        def increase(num,count):
            pos = 0
            while count > 0:
                if num & ( 1 << pos ) == 0:
                    num |= 1 << pos
                    count-=1
                pos+=1
            return num
        def decrease(num,count):
            pos = 0
            while count > 0:
                if num & ( 1 << pos ):
                    num ^= ( 1 << pos ) 
                    count-=1
                pos+=1
            return num
        num2_Bits,num1_Bits = count_set_bits(num2),count_set_bits(num1)

        if num2_Bits == num1_Bits:
            return num1
        elif num2_Bits > num1_Bits:
            return increase(num1,num2_Bits-num1_Bits)
        else:
            return decrease(num1,num1_Bits-num2_Bits)
