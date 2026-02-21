USE sakila
SELECT TOP 10
    country.country,(
        SELECT SUM(payment.amount) 
        FROM payment
        WHERE payment.customer_id IN (
            SELECT customer.customer_id
            FROM customer
            WHERE customer.address_id IN (
                SELECT address.address_id
                FROM address
                WHERE address.city_id IN (
                    SELECT city.city_id
                    FROM city
                    WHERE city.country_id = country.country_id) ) ) )AS payment
FROM country
ORDER BY
    (
        SELECT SUM(payment.amount)
        FROM payment
        WHERE payment.customer_id IN (
            SELECT customer.customer_id
            FROM customer
            WHERE customer.address_id IN (
                SELECT address.address_id
                FROM address
                WHERE address.city_id IN (
                    SELECT city.city_id
                    FROM city
                    WHERE city.country_id = country.country_id
                )
            )
        )
    ) DESC;
