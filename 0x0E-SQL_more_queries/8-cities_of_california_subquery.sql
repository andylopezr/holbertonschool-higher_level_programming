-- Selects all cities in California by getting id from second table

SELECT id, name FROM cities WHERE state_id=(SELECT id FROM states
WHERE name="California") ORDER BY id
