WITH RankedSalaries AS (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
    FROM Employee
)
SELECT MAX(salary) AS SecondHighestSalary 
FROM RankedSalaries 
WHERE rnk = 2;