-- Write a SQL script that creates an index
-- idx_name_first_score on the table names
CERATE INDEX idx_name_first_score
ON `names` (name(1), score);
