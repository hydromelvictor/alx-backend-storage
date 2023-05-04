-- Write a SQL script that ranks country origins
-- ordered by the number of (non-unique)
SELECT `origin`, COUNT(`fans`)
FROM `metal_bands`
GROUP BY `origin`;
