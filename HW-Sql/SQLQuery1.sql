USE sakila
SELECT *
FROM film
WHERE film_id NOT IN (
    SELECT DISTINCT film_id
    FROM inventory
    WHERE inventory_id IN (
        SELECT inventory_id
        FROM rental
        WHERE inventory_id IS NOT NULL
    )
    AND film_id IS NOT NULL
);

