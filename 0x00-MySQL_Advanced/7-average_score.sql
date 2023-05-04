-- Write a SQL script that creates a stored
-- procedure ComputeAverageScoreForUser
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(user_id, )
BEGIN
    SELECT AVG(`score`)
    FROM `corrections`
    WHERE `corrections`.`user_id` = "user_id";
END$$
DELIMITER ;