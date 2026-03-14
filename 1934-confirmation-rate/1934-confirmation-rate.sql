WITH table1 AS (
SELECT s.user_id,
COUNT(c.user_id) AS total_request,
SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END) AS confirmation_request
FROM Signups s
LEFT JOIN Confirmations c
ON s.user_id = c.user_id
GROUP BY s.user_id
)

SELECT user_id,
CASE
WHEN total_request = 0 THEN 0
ELSE ROUND(confirmation_request / total_request, 2)
END AS confirmation_rate
FROM table1;