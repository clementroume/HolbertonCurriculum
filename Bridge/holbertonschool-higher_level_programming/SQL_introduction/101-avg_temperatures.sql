-- This script calculates the average temperature in Fahrenheit for each city from the `temperatures` table, 
-- then orders the cities by the average temperature in descending order to show the hottest cities first.
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
