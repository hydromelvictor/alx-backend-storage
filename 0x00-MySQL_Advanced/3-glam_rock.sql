-- Write a SQL script that lists all bands
-- with Glam rock as their main style
SELECT `band_name`, `style`
FROM `metal_bands`
WHERE `style` = 'Glam rock';
