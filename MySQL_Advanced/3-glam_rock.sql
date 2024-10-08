-- SQL script to list Glam rock bands by their longevity
SELECT 
    name AS band_name,
    CASE 
        WHEN split IS NOT NULL THEN (split - formed)
        ELSE (YEAR(CURDATE()) - formed)
    END AS lifespan
FROM 
    metal_bands
WHERE 
    style = 'Glam rock'
ORDER BY 
    lifespan DESC;
