-- Write a SQL script that creates a stored
-- procedure ComputeAverageScoreForUser
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INTEGER)
BEGIN
    UPDATE `users`
    SET average_score = (SELECT AVG(`score` * `weight`)
    FROM `corrections`, `projects`
    WHERE `corrections`.`user_id` = `user_id`,
    `projects`.`id` = `corrections`.`project_id`)
    WHERE `id` = `user_id`;
END $$
DELIMITER ;
