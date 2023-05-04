-- Write a SQL script that creates a stored
-- procedure ComputeAverageScoreForUser
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INTEGER)
BEGIN
    SELECT AVG(`score`)
    FROM `corrections`
    WHERE `corrections`.`user_id` = "user_id";
END$$
DELIMITER ;
