
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

def twoSum(nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
        for i in range(len(nums)):  # [2,5,5,11]
            value = nums[i]  
            # value2 = nums[i+1]
            if (i+1) <= len(nums):
                for j in range(i+1,len(nums)):
                    value2 = nums[j]
                    if (value + value2 == target):
                        # return(i,j) 
                        print(i,j)
                        break 
                    else: 
                        continue
            else: 
                break
        
        
        
        
        # for i,nums[0] in enumerate(nums): # i = -3
        #     if nums[i+1] < len(nums):
        #      for j,nums[i+1] in enumerate(nums):  # j = 4
        #          if(nums[i] + nums[i+1] == target):
        #              break
        # for i in range(nums[0],len(nums)):
        #     for j in range(nums[i+1], len(nums)-1):
        #         if (nums[i] + nums[j] == target):
        #             break
                
                
                     
    # """
    #     فكرة الحل هنا يصديقى عشان لما ترجعلها تانى 
    #     انى عايزك تحاول تثبت اول قيمة وتجمع  عليها كل الى بعدها لو منفعش 
    #     ادخل على بعده وعيد المحاولة تانى 
    #     """

       
    
        
# nums = [1,2,4,5,6] 
# nums = [3,2,3]
nums = [2,5,5,11]
target = 10 
# print(len(nums)+1)

# give on number valid 
# if valid I got it , stop the program 
twoSum(nums,target)
       
         # for indx,numbs in enumerate(nums): # first loop , indx = 0 
        #     if indx != (len(nums) - 1):
        #         if (nums[indx] + nums[indx+1] == target):
        #             return print(list([indx,indx+1]))
        #             break
        #         elif (nums[indx] + nums[-1] == target):
        #             return print(list([indx, len(nums)-1]))
        #             break
        #         else:
        #             continue
        #         break
        # for i in range(0,len(nums),2): 
        #     if i != (len(nums) -1 ):
        #         if (nums[i] + nums[i+2] == target):
        #             return print(list([i,i+2]))
        #             break 
        #         break
                