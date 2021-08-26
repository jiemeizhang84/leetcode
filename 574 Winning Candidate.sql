SELECT Name
FROM candidate
WHERE id = (SELECT CandidateId
            FROM vote
            GROUP BY CandidateId
            ORDER BY COUNT(*) DESC
            LIMIT 1) 