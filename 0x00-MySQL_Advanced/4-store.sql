-- Write a SQL script that creates a trigger
-- that decreases the quantity of an item
CREATE TRIGGER decon
AFTER INSERT
ON `order`
FOR EACH ROW
SET @quantity = @quantity - NEW.`number`;
