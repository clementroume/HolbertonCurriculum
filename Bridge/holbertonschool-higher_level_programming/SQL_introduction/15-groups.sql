-- This script counts the number of records with the same score in the `second_table` of the `hbtn_0c_0` database,
-- grouping the results by score and ordering them in descending order by the count of each score.
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
