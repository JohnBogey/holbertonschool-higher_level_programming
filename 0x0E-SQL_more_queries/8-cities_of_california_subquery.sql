-- lists all cities of california
SELECT id, name FROM cities WHERE state_id = (
       SELECT id FROM cities WHERE name = "California"
) ORDER BY id ASC;
