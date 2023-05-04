-- Write a SQL script that creates a function
-- SafeDiv that divides (and returns) the first
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
BEGIN
    RETURN (IF(b=0, 0, b / a ));
END$$
DELIMITER ;