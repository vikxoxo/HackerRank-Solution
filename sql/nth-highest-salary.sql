# https://leetcode.com/problems/nth-highest-salary/submissions/
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M = N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT IFNULL((SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT M, 1), NULL)
      
  );
END
