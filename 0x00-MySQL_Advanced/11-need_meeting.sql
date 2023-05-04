-- 
-- 
CREATE VIEW need_meeting AS
    SELECT `name`
    FROM `students`
    WHERE `students`.`score` < 80
    AND
    `students`.`last_meeting` IS NULL
    OR
    DATE_ADD(NOW(), INTERVAL -1 MONTH);
