class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        
        """
        
        for i in range(n):
            temp = nums2[i]
            #print(temp)
            for j in range(m+n):
                if(nums1[j] > temp ):
                    nums1[m+n-1] = nums1[j]
                    nums1[j] = temp
                    #print(nums1)
                    #print("ddddd")
                    k = j+1
                    while(k < m+n-1):
                        temp1 = nums1[k]
                        #print(temp1)
                        nums1[k] = nums1[m+n-1]
                        # print(nums1)
                        # t=input()
                        nums1[m+n-1] = temp1
                        # print(k,nums1)
                        # t=input()
                        k = k+1
                        
                    break
                if(nums1[j] < temp   and j>i+m-1 and nums1[j]==0):
                    nums1[j]=temp
                    break
                