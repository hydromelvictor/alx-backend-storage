-- Write a SQL script that creates a trigger
-- that resets the attribute valid_email only
CREATE TRIGGER ren
AFTER UPDATE
ON `users`
FOR EACH ROW
Update `users`
SET valid_email = 0
WHERE `eamil` = NEW.`email`;
