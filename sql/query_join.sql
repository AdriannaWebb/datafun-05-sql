-- Inner Join query
SELECT b.title, a.first_name, a.last_name
from books b
INNER JOIN authors a ON b.author_id = a.author_id;

-- Left Join query
SELECT b.title, a.first_name, a.last_name
FROM books b
LEFT JOIN authors a ON b.author_id = a.author_id;