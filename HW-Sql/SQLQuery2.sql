USE sakila;

SELECT
    category.name AS category_name,
    (
        SELECT AVG(film.rental_duration)
        FROM film
        WHERE film.film_id IN (
            SELECT film_category.film_id
            FROM film_category
            WHERE film_category.category_id = category.category_id
        )
    ) AS avg_rental_duration
FROM category;

