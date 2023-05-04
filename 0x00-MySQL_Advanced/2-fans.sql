-- Write a SQL script that ranks country origins
-- ordered by the number of (non-unique)
SELECT `origin`, SUM(`fans`) as nb_fans
FROM `metal_bands`
GROUP BY `origin`
ORDER BY nb_fans DESC;
