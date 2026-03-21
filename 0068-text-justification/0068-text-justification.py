from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            # Step 1: pick words for current line
            line_words = []
            line_len = 0

            while i < n and line_len + len(words[i]) + len(line_words) <= maxWidth:
                line_words.append(words[i])
                line_len += len(words[i])
                i += 1

            # Step 2: calculate spaces
            spaces = maxWidth - line_len
            gaps = len(line_words) - 1

            # Step 3: build line
            # Case 1: last line OR single word
            if i == n or gaps == 0:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                space_each = spaces // gaps
                extra = spaces % gaps

                line = ""
                for j in range(gaps):
                    line += line_words[j]
                    # extra spaces go to left slots
                    line += " " * (space_each + (1 if j < extra else 0))
                line += line_words[-1]

            res.append(line)

        return res