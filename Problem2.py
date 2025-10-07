"""
TC: O(log(N-K) + K) {The time complexity is dominated by the binary search, which takes O(log(N-K)) time, followed by O(K) time to slice and return the result.}
SC: O(K) {The space complexity is determined by the storage required for the output list, which contains K elements.}

Approach:

This problem is solved using a modified Binary Search to efficiently find the starting index of the K closest elements. The goal is to find the continuous subarray of length K whose elements, when considered together, are closest to the target x.

The crucial insight is that the K elements we seek must form a continuous subarray of length K. If the input array has length N, there are N−K+1 possible starting positions for this subarray. We perform a binary search on the possible starting indices, ranging from 0 to N−K.

In each step of the binary search, we compare two potential elements that define the boundary of the optimal window: the element just before the window, arr[mid], and the element just after the window, arr[mid+k]. We compare the distances of these two elements from x. If the distance from x to arr[mid] is less than or equal to the distance from x to arr[mid+k], it means the current window is either optimal or we should try a window that starts earlier. Therefore, we set high=mid. Otherwise, the element at arr[mid+k] is closer to x, meaning the starting index is too small, and we must shift the window to the right by setting low=mid+1.

The loop terminates when low=high, and this index represents the optimal starting position of the K closest elements. The function then returns the slice arr[low:low+k].

The problem ran successfully on LeetCode.
"""
from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        low, high = 0, n - k

        while low < high:
            mid = low + (high - low)//2

            distS, distE = x - arr[mid], arr[mid+k] - x

            if distS <= distE:
                high = mid
            else:
                low = mid + 1
        
        return arr[low:low+k]



