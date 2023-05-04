-- Write a SQL script that creates a function
-- SafeDiv that divides (and returns) the first
DELIMITER $$
DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    RETURN (IF(b = 0, 0, b / a ));
END$$
DELIMITER ;