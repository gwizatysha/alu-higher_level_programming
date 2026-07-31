-- 8-cities_of_california_subquery script
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (SELECT id FROM states WHERE name = "California")
ORDER BY cities.id ASC;
