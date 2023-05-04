-- 
-- 
CREATE VIEW need_meeting (
    `students`.`score` < 80
    AND DATEDIFF(NOW(), `students`.`last_meeting`) IN (Now(), )
    )
AS SELECT * FROM `students`;