-- Write a SQL script that creates a function
-- SafeDiv that divides (and returns) the first
DELIMITER $$
CREATE FUNCTION SafeDiv(a, b)
BEGIN
    IF b = 0
        SET 0;
    SET b / a;
END$$
DELIMITER ;