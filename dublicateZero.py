class Solution:
    #def swap(a,b):
        
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        while(i<len(arr)-1):
            
            if(arr[i]==0):
                arr[len(arr)-1]=arr[i+1]
                arr[i+1]=0
                k=i+2
                i=i+1
                #print(arr)
                while(k<len(arr)-1):
                    temp=arr[k]
                    #print(i,k)
                    arr[k]=arr[len(arr)-1]
                    arr[len(arr)-1]=temp
                    k=k+1
                #print("Automated",arr)
            i=i+1