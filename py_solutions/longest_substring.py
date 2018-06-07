# coding: utf-8

"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

from collections import OrderedDict

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        container = OrderedDict()
        max_norepeate = 1
        first = 0
        len_s = len(s)
        stop = False
        while not stop:
            container.clear()
            container[s[first]] = first
            for j in range(first + 1, len_s):
                if s[j] not in container:
                    container[s[j]] = j
                else:
                    break
            
            cur_len = len(container)
            # print("{}+{}={}".format(first, cur_len, first+cur_len))
            # print(len_s)
            stop = (first + cur_len) >= len_s

            first = container[s[j]] + 1
            max_norepeate = cur_len if cur_len > max_norepeate else max_norepeate
        
        return max_norepeate 
    

if __name__ == "__main__":
    s = Solution()
    test_str = 'abcabcbb'
    ans = s.lengthOfLongestSubstring(test_str)
    print(ans)