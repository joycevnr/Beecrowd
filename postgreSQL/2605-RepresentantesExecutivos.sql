SELECT 
    p.name, v.name 
FROM
    products p, providers v
WHERE 
     id_categories = 6 AND
     p.id_providers = v.id --garante que os produtos sejam associados aos fornecedores corretos.

    -- products (representada pela abreviação p)
     -- tabela providers (representada pela abreviação v)