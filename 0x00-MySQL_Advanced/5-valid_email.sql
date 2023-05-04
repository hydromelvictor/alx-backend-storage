-- Write a SQL script that creates a trigger
-- that resets the attribute valid_email only
DELIMITER $$
CREATE TRIGGER ren
AFTER UPDATE
ON `users`
FOR EACH ROW
BEGIN
    IF NEW.`email` != OLD.`email`
        SET NEW.`valid_email` = 0;
    END IF;
END;$$
DELIMITER ;
