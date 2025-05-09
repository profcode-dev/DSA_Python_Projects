
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
       
