-- This script lists all records from the `second_table` of the `hbtn_0c_0` database where the `name` is not empty, 
-- and orders the results by score in descending order.
SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;
