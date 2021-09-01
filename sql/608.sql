SELECT id,
       CASE 
            WHEN id = (SELECT t.id FROM tree t WHERE t.p_id IS NULL) THEN 'Root'
            WHEN id IN (SELECT DISTINCT t1.p_id FROM tree t1) THEN 'Inner'
            ELSE 'Leaf'
       END AS Type 
FROM tree
ORDER BY id;