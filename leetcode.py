# # class Solution(object):
# #     def twoSum(self, nums, target):
# #         """
# #         :type nums: List[int]
# #         :type target: int
# #         :rtype: List[int]
# #         """
# #         i = 0
# #         j = len(nums)-1
# #         while i < j:
# #             if nums[i] + nums[j] > target:
# #                 j-=1
# #             elif nums[i] + nums[j] < target:
# #                 i+=1
# #             else:
# #                 return [i,j]
# #         return []
    
# # print(Solution.twoSum(Solution,[5,7,9],12))


# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         sum = 0
#         for i in range(len(l1)):
#             sum += l1[i]*10**i
#         for j in range(len(l2)):
#             sum += l2[i]*10**j
#         print(sum)

# Solution.addTwoNumbers(Solution,[1,1,1],[1,1,1,1])

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        while length != 0:
            i=0
            while i <= len(s) - length:
                d = []
                for j in range(i,i+length):
                    if s[j] not in d:
                        d.append(s[j])
                        if j == i+length-1:
                            return length
                    elif s[j] in d:
                        break
                i+=1
            length-=1
        return 0
    
print(Solution.lengthOfLongestSubstring(Solution, "abcabcbb"))