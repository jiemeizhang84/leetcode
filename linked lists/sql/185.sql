SELECT d.Name Department, e.Name Employee, e.Salary Salary
FROM Employee e JOIN Department d
    ON e.DepartmentId = d.Id
WHERE 3 > (
    SELECT COUNT(DISTINCT Salary)
    FROM Employee e1
    WHERE e1.Salary > e.Salary
    AND e1.DepartmentId = e.DepartmentId
)

--solution2
select d.name department, e.name employee, e.salary
from
(select departmentId,
       salary,
       name,
       dense_rank() over(partition by departmentId order by salary desc) as rk
from employee) e
inner join department d
on e.departmentId=d.id
where rk<=3
order by 1,3 desc