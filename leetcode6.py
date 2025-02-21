#You are given an integer array score of size n,
#  where score[i] is the score of the ith athlete in a competition.
#  All the scores are guaranteed to be unique.

class Solution:
    def findRelativeRanks(self,score):
        sorted_score = sorted(score, reverse = True)
        rank = {}
        for i,s in  enumerate(sorted_score):
            if i == 0 :
                rank[s] = "Gold Medal"
            elif i == 1:
                rank[s] = "Silver Medal"
            elif i == 2:
                rank[s] = "Bronze Medal"
            else :
                rank[s] = str(i+1)
        return [rank[s] for s in score]


d = Solution()
score = [5,4,3,2,1]
f = d.findRelativeRanks(score)
print(f)
