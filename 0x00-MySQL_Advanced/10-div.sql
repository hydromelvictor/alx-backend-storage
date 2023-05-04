-- Write a SQL script that creates a function
-- SafeDiv that divides (and returns) the first
DELIMITER $$
CREATE FUNCTION SafeDiv(a, b)
BEGIN
    SELECT IF(b=0, 0, b / a );
END$$
RETURNS REAL
DELIMITER ;