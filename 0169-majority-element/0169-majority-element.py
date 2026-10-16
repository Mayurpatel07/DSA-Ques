class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # count = {}
        # for i in nums :
        #     if i in count :
        #         count[i]+=1 
        #     else :
        #         count[i]=1 
        # return max(count, key = count.get)
        n = len(nums)
        a = n//2
        f={}
        b =[]
        for i in nums:
            f[i]= f.get(i,0)+1 
        for i,j in f.items():
            if j > a:
              return i  
        
