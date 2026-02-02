from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        word_freq = Counter(words)
        result = []

        # Try each offset
        for i in range(word_len):
            left = i
            curr_count = 0
            seen = Counter()

            # Move in steps of word_len
            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in word_freq:
                    seen[word] += 1
                    curr_count += 1

                    # Too many of this word → shrink window
                    while seen[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        curr_count -= 1
                        left += word_len

                    # Valid window
                    if curr_count == word_count:
                        result.append(left)
                else:
                    # Reset window
                    seen.clear()
                    curr_count = 0
                    left = right + word_len

        return result
