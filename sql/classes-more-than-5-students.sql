# https://leetcode.com/problems/classes-more-than-5-students/solution/
# Write your MySQL query statement below
SELECT class FROM Courses 
GROUP BY class
HAVING COUNT(student) >=5 ; 
