-- Write a SQL script that creates a trigger
-- that decreases the quantity of an item
CREATE TRIGGER decon
AFTER INSERT
ON `orders`
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.`number`
WHERE `name` = New.`item_name`;
