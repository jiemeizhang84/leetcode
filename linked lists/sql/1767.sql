WITH RECURSIVE tmp AS (
    SELECT task_id, 1 subtask_id
    FROM tasks
    UNION ALL
    SELECT t.task_id, t.subtask_id + 1 subtask_id
    FROM tmp t, tasks
    WHERE t.task_id = tasks.task_id
    AND t.subtask_id < tasks.subtasks_count
)


SELECT t.task_id, t.subtask_id
FROM tmp t
LEFT JOIN executed e
ON t.task_id = e.task_id AND t.subtask_id = e.subtask_id
WHERE e.subtask_ID IS NULL