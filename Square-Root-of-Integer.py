class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A==0:
            return 0
        if A < 4:
            return 1
        else:
            start = 2
            end = A // 2
            mid = (start + end) // 2
            while(start <= mid <= end):
                if ((mid*mid) <= A) and (((mid+1) * (mid+1) ) > A):
                    return mid
                if ((mid*mid) > A):
                    end = mid - 1
                    mid = (start + end) // 2
                else:
                    start = mid + 1
                    mid = (start + end) // 2
