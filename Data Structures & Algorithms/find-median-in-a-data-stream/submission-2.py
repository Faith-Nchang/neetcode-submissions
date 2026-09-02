class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        l, r = 0, len(self.arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.arr[mid] < num:
                l = mid + 1
            else:
                r = mid - 1
        self.arr.insert(l, num)


    def findMedian(self) -> float:
        
        n  = len(self.arr) 
        if n == 0:
            return 0.0
        elif n % 2 == 0:
            
            mid = n // 2
            return (self.arr[mid - 1] + self.arr[mid]) / 2
        else:
            return self.arr[n // 2]

        
        