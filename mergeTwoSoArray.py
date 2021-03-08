
def merge( nums1, m, nums2, n):

        for i in range(n):
            temp = nums2[i]
            print(temp)
            for j in range(m+n):
                if(nums1[j] > temp and nums1[j] > nums1[j-1] and j != 0):
                    nums1[m+n-1] = nums1[j]
                    nums1[j] = temp
                    print(nums1)
                    print("ddddd")
                    k = j+1
                    while(k < m+n-1):
                        temp1 = nums1[k]
                        print(temp1)
                        nums1[k] = nums1[m+n-1]
                        # print(nums1)
                        # t=input()
                        nums1[m+n-1] = temp1
                        # print(k,nums1)
                        # t=input()
                        k = k+1
                        
                    break
                if(nums1[j] < temp and nums1[j] < nums1[j-1] and j != 0 and nums1[j]==0 ):
                    nums1[j]=temp
                    break

            
        print(nums1)


a = [1,2,3,0,0,0]
b = [2,5,6]
m = 3
n = 3
#sol = Solution
merge(a, m,b,n)
