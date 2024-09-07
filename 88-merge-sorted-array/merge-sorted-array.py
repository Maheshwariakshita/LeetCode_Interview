class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        k = m + n - 1

        # Merge nums1 and nums2 from the end
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1

        # If nums2 still has remaining elements, copy them into nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         if m==0:
#             return nums2
#         # if n==0:
#         #     return nums1
#         i,j=m-1,n-1
#         while i>=0 and j>=0:
#             if nums1[i]<nums2[j]:
#                 nums1[m+n-1]=nums2[j]
#                 n-=1
#                 j-=1
#             else:
#                 nums1[m+n-1]=nums1[i]
#                 m-=1
#                 i-=1


        # arr=[]
        # i=0
        # j=0
        # while i<m and j<n:
        #     if nums1[i]<nums2[j]:
        #         arr.append(nums1[i])
        #         i+=1
        #     else:
        #         arr.append(nums2[j])
        #         j+=1
        # if i<len(nums1):
        #     arr+=nums1[i:]
        # if j<len(nums2):
        #     arr+=nums2[j:]
        # return arr









         
        # # Initialize nums1's index
        # i = m - 1
        # # Initialize nums2's index
        # j = n - 1
        # # Initialize a variable k to store the last index of the 1st array...
        # k = m + n - 1
        # while j >= 0:
        #     if i >= 0 and nums1[i] > nums2[j]:
        #         nums1[k] = nums1[i]
        #         k -= 1
        #         i -= 1
        #     else:
        #         nums1[k] = nums2[j]
        #         k -= 1
        #         j -= 1
     











        # last=m+n-1
        # while m>0 and n>0:
        #     if nums1[m-1]>=nums2[n-1]:
        #         nums1[last]=nums1[m-1]
        #         m-=1
        #     else: 
        #         nums1[last]=nums2[n-1]
        #         n-=1
        #     last-=1
        # while n>0:
        #     nums1[last]=nums2[n-1]
        #     n-=1
        #     last-=1
        