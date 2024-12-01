-- This script calculates the average temperature for each city during the months of July and August (months 7 and 8) 
-- from the `temperatures` table, then orders the cities by average temperature in descending order 
-- and limits the result to the top 3 cities with the highest average temperatures.
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month=7 OR month=8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
