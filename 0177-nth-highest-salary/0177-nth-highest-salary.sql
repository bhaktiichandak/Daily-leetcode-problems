CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
select(
    select salary as getNthHighestSalary
    from(
        select id,salary , 
        dense_rank() over(order by salary desc)  ranksalary
        from Employee
    )t
    where ranksalary = N
    limit 1
)t
  );
END