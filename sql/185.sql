SELECT d.Name Department, e.Name Employee, e.Salary Salary
FROM Employee e JOIN Department d
    ON e.DepartmentId = d.Id
WHERE 3 > (
    SELECT COUNT(DISTINCT Salary)
    FROM Employee e1
    WHERE e1.Salary > e.Salary
    AND e1.DepartmentId = e.DepartmentId
)