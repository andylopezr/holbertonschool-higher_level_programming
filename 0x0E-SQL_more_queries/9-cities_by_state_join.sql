-- Lists all cities and displays state information using join

SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states
ON cities.state_id=states.id;
