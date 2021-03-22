-- lists all rows of table by score, showing only those > 10
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
