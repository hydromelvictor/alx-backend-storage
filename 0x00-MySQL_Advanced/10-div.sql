-- Write a SQL script that creates a function
-- SafeDiv that divides (and returns) the first
DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
RETURN (IF (b = 0, 0, b / a ));
