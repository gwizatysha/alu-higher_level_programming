-- lists all records of second_table with a non-null name, by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
