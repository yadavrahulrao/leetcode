#68. Text Justification
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            line_len = len(words[i])
            j = i + 1
            
            # Fit as many words as possible into the current line
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            
            # Words for this line = words[i:j]
            line_words = words[i:j]
            num_words = j - i

            # If last line OR single word → left justify
            if j == n or num_words == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                # Fully justify
                total_letters = sum(len(w) for w in line_words)
                total_spaces = maxWidth - total_letters
                gaps = num_words - 1

                space_per_gap = total_spaces // gaps
                extra = total_spaces % gaps  # extra spaces for left gaps

                line = ""
                for k in range(gaps):
                    line += line_words[k]
                    line += " " * (space_per_gap + (1 if k < extra else 0))
                line += line_words[-1]  # last word

            res.append(line)
            i = j

        return res
