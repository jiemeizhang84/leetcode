SELECT
    a.id,
    a.company,
    a.salary
FROM
    employee a
WHERE
    (
        (
            SELECT
                count(1)
            FROM
                employee
            WHERE
                a.company = company
                AND salary > a.salary
        ) = (
            SELECT
                count(1)
            FROM
                employee
            WHERE
                a.company = company
                AND salary < a.salary
        )
    )
    OR abs(
        (
            SELECT
                count(1)
            FROM
                employee
            WHERE
                a.company = company
                AND salary > a.salary
        ) - (
            SELECT
                count(1)
            FROM
                employee
            WHERE
                a.company = company
                AND salary < a.salary
        )
    ) = 1
group by 2,3

