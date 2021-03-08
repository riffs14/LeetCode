class Solution(object):
    def findNumbers(self, num):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        maxCount=0
        
        for i in range(len(num)):
            if(num[i]>9 and num[i]<100 or num[i]>999 and num[i]<10000 or num[i]>99999 and num[i]<1000000):
                count=count+1
            #if nums[i]>9 and nums[i]<100:
            
        return count    
#Code has been accepted
#python is not a good programming language for practice though
