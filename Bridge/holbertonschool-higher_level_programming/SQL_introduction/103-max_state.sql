-- This script retrieves the maximum temperature recorded for each state from the `temperatures` table. 
-- It groups the results by state and orders them alphabetically by state name.
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
