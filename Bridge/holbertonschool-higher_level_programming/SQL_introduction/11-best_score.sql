-- This script retrieves all records from the `second_table` in the `hbtn_0c_0` database where the `score` is greater than or equal to 10, 
-- and orders the results by the `score` column in descending order.
SELECT score, name 
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
