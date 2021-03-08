class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #n=len(nums)
        maxCount=0
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count=count+1
                print(count)
                
            else:
                if(count>maxCount):
                    maxCount=count
                count=0
        if(count>maxCount):
            maxCount=count
        return maxCount