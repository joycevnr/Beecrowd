SELECT 
    p.id, p.name 
FROM
    products p, categories c
WHERE 
     c.name like 'super%'AND c.id = id_categories;