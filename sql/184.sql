SELECT d.Name Department, e1.Name Employee, e1.Salary
FROM Employee e1
JOIN Department d
ON e1.DepartmentId = d.Id
WHERE 0 = (
    SELECT COUNT(DISTINCT e2.Salary)
    FROM Employee e2
    WHERE e2.Salary > e1.Salary
    AND e2.DepartmentId = e1.DepartmentId
);