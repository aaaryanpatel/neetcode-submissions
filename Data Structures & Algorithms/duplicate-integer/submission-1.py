# ============================================
# CONTAINS DUPLICATE
# ============================================

# Problem:
# Given an integer array nums,
# return True if any value appears more than once.
# Otherwise return False.


# ============================================
# SOLUTION 1: BRUTE FORCE
# ============================================

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Compare every element with every element after it.
        #
        # Example:
        # nums = [1, 2, 3, 3]
        #
        # Compare:
        # 1 with 2, 3, 3
        # 2 with 3, 3
        # 3 with 3 -> duplicate found

        for i in range(len(nums)):

            # Start at i + 1 because:
            # 1. We don't want to compare nums[i] with itself.
            # 2. We don't need to check previous pairs again.
            for j in range(i + 1, len(nums)):

                if nums[i] == nums[j]:
                    return True

        return False


# Time Complexity: O(n^2)
# Because in the worst case we compare many pairs using nested loops.
#
# Space Complexity: O(1)
# We do not use any extra data structure.
#
# WHY NOT BEST?
# Very slow for large arrays.


# ============================================
# SOLUTION 2: SORTING
# ============================================

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Sort the array first.
        #
        # Example:
        # [3, 1, 2, 3]
        #
        # becomes:
        # [1, 2, 3, 3]
        #
        # After sorting, duplicate values will be beside each other.

        nums.sort()

        # Start from index 1 because we compare the current element
        # with the element before it.
        #
        # If we started at index 0,
        # nums[i - 1] would become nums[-1].

        for i in range(1, len(nums)):

            if nums[i] == nums[i - 1]:
                return True

        return False


# Time Complexity: O(n log n)
# Sorting takes O(n log n).
# The loop takes O(n).
#
# O(n log n) + O(n) = O(n log n)
#
# Space Complexity:
# Often treated as O(1) extra space for an in-place sorting approach
# at a high interview level, although Python's sorting implementation
# can use additional internal memory.
#
# WHY BETTER THAN BRUTE FORCE?
# O(n log n) is much faster than O(n^2).
#
# WHY NOT THE BEST?
# Hashing can solve the problem in O(n) average time.


# ============================================
# SOLUTION 3: HASHMAP
# ============================================

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # HashMap stores:
        #
        # number -> index
        #
        # Example:
        # {
        #     1: 0,
        #     2: 1,
        #     3: 2
        # }

        prevMap = {}

        for index, value in enumerate(nums):

            # Checking if a key exists in a HashMap
            # is O(1) average time.

            if value in prevMap:
                return True

            # Store:
            # number -> index
            prevMap[value] = index

        return False


# Time Complexity: O(n) average
# We go through the array once.
#
# HashMap lookup = O(1) average
# HashMap insertion = O(1) average
#
# Space Complexity: O(n)
# In the worst case, every number is unique,
# so we store all n numbers in the HashMap.
#
# WHY GOOD?
# Much faster than sorting and brute force.
#
# WHY NOT IDEAL FOR THIS PROBLEM?
# We store the index, but we never actually need the index.
#
# The problem only asks:
# "Have we seen this number before?"
#
# Therefore, a HashSet is cleaner.


# ============================================
# SOLUTION 4: HASHSET - BEST / CLEANEST
# ============================================

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # HashSet stores only values.
        #
        # Example:
        # seen = {1, 2, 3}
        #
        # We don't need indexes or any extra information.

        seen = set()

        for num in nums:

            # If num is already in the set,
            # then we found a duplicate.

            if num in seen:
                return True

            # Otherwise remember that we have seen it.

            seen.add(num)

        return False


# Time Complexity: O(n) average
# We visit every element once.
#
# HashSet lookup = O(1) average
# HashSet insertion = O(1) average
#
# Space Complexity: O(n)
# If all elements are unique,
# the set may contain all n elements.
#
# WHY BEST FOR THIS PROBLEM?
#
# We only need to know:
# "Have I seen this value before?"
#
# A HashSet is designed exactly for that.
#
# HashMap would also work,
# but storing an index/value pair is unnecessary here.


# ============================================
# SOLUTION 5: SORTING + HASHMAP
# VALID BUT NOT RECOMMENDED
# ============================================

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        prevMap = {}

        sorted_nums = sorted(nums)

        for index, value in enumerate(sorted_nums):

            if value in prevMap:
                return True

            prevMap[value] = index

        return False


# Time Complexity: O(n log n)
#
# sorted(nums) = O(n log n)
# loop = O(n)
#
# Total = O(n log n)
#
# Space Complexity: O(n)
#
# WHY THIS IS NOT A GOOD SOLUTION?
#
# We are doing TWO unnecessary things:
#
# 1. Sorting the array
# 2. Using a HashMap
#
# HashMap alone already gives O(n) average time.
#
# So sorting first adds extra computation for no benefit.


# ============================================
# INTERVIEW SUMMARY
# ============================================

# Worst -> Best
#
# 1. Brute Force
#    Time:  O(n^2)
#    Space: O(1)
#
# 2. Sorting
#    Time:  O(n log n)
#    Space: depends on sorting implementation
#
# 3. HashMap
#    Time:  O(n) average
#    Space: O(n)
#
# 4. HashSet
#    Time:  O(n) average
#    Space: O(n)
#    BEST / CLEANEST for this problem
#
#
# USE HASHSET WHEN:
# "Have I seen this value before?"
#
# USE HASHMAP WHEN:
# "Have I seen this value before AND I need
# some information associated with it?"
#
# Example:
#
# Contains Duplicate -> HashSet
#
# Two Sum -> HashMap
# because Two Sum needs:
# number -> index