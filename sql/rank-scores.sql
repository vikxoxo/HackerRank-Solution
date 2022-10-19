# Write your MySQL query statement below
# https://learnsql.com/blog/how-to-rank-rows-in-sql/
# https://leetcode.com/problems/rank-scores/submissions/
SELECT score, 
DENSE_RANK () OVER (
ORDER BY score DESC)  as 'rank'
FROM Scores ORDER BY score DESC;
