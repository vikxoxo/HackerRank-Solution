---https://www.hackerrank.com/challenges/the-pads/problem

SELECT CONCAT(Name,'(',SUBSTRING(Occupation, 1, 1),')') FROM OCCUPATIONS
ORDER BY NAME ASC;

SELECT CONCAT('There are a total of ', COUNT(Occupation), ' ', LOWER(Occupation), 's.') 
FROM OCCUPATIONS
GROUP BY OCCUPATIONS.Occupation
ORDER BY COUNT(Occupation) ASC, Occupation ASC;
