SELECT COUNT(*) AS author_count FROM authors;

SELECT AVG(year_published) AS average_year FROM books;

SELECT author_id, COUNT(*) AS book_count
FROM books
GROUP BY author_id;