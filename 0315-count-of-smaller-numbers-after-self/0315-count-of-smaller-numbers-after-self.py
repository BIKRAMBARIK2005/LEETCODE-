class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Brute Force Approch
        # count = 0
        # n = len(nums)
        # counts = [0] * n
        # for i in range(n):
        #   count = 0
        #   for j in range(i + 1, n):
        #     if nums[i] > nums[j]:
        #       count = count + 1
        #       counts[i] = count
        # return counts
        
        # Optimized Approach
        n = len(nums)
        counts = [0] * n
        indices = list(range(n))
        def merge_sort(left, right):
          if left >= right:
            return
          
          mid = (left + right) // 2

          merge_sort(left, mid)
          merge_sort(mid + 1, right)

          temp = []
          i  = left
          j = mid + 1
          right_count = 0

          while i <= mid and j <= right:
            if nums[indices[i]] > nums[indices[j]]:
              temp.append(indices[j])
              right_count += 1
              j += 1
            else:
              counts[indices[i]] += right_count
              temp.append(indices[i])
              i += 1
          while i <= mid:
            counts[indices[i]] += right_count
            temp.append(indices[i])
            i += 1
          while j <= right:
            temp.append(indices[j])
            j += 1
          indices[left:right+1] = temp
        merge_sort(0, n - 1)
        return counts