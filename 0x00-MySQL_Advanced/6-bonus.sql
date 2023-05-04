-- Write a SQL script that creates a stored
-- procedure AddBonus that adds a new 
DELIMITER $$
CREATE PROCEDURE AddBonus (IN user_id  INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    SELECT IF (EXISTS(
        SELECT `name`
        FROM `projects`
        WHERE `name`=`project_name`),
        SELECT `name`
        FROM `projects`
        WHERE `name`=`project_name`,
        INSERT INTO `projects`('name')
        VALUES (`project_name`)
        ) AS result;
    INSERT INTO `corrections` (`user_id`, `project_id`, `score`)
    VALUES (`user_id`, result.`id`, `score`);
END$$
DELIMITER ;
