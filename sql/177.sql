create function getNthHighestSalary(N INT) returns INT
begin
    declare M INT;
    set M=N-1;
    return(
        select distinct salary
        from employee
        order by salary desc
        limit 1 offset M
    );
end