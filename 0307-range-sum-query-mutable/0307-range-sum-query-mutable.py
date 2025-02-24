class SegmentTree:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None
class NumArray:


    def __init__(self, nums: List[int]):
        def createTree(nums, l, r):
            if l > r:
                return None
            if l == r:
                n = SegmentTree(l,r)
                n.total = nums[l]
                return n
            
            mid = (l + r) // 2

            root = SegmentTree(l,r)

            root.left = createTree(nums,l,mid)
            root.right = createTree(nums,mid+1,r)

            root.total = root.left.total + root.right.total

            return root
        
        self.root = createTree(nums,0,len(nums)-1)

    def update(self, index: int, val: int) -> None:

        def updateVal(root,i,val):
            if root.start == root.end:
                root.total = val
                return val

            mid = (root.start + root.end) // 2

            if i <= mid:
                updateVal(root.left,i, val)
            
            else: 
                updateVal(root.right, i, val)

            root.total = root.left.total + root.right.total

            return root.total

        return updateVal(self.root,index,val)
        

    def sumRange(self, left: int, right: int) -> int:

        def rangeSum(root,i,j):
            if root.start == i and root.end == j:
                return root.total

            mid = (root.start + root.end) // 2

            if j <= mid:
                return rangeSum(root.left, i, j)


            elif i >= mid + 1:
                return rangeSum(root.right, i, j)
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid+1, j)
        return rangeSum(self.root,left,right)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)