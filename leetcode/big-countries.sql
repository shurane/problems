SELECT name, population, area
FROM World
WHERE (area > 3E6) OR (population > 25E6)

# this query seems to be faster
SELECT name, population, area
FROM World
WHERE area > 3000000 OR population > 25000000

# 3 minutes