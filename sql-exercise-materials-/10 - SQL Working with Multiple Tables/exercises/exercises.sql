-- ============================================================
-- Exercises: SQL Working with Multiple Tables
-- Database: sakila
-- Write your query below each question. Check your work against
-- solutions.sql once you're done (or stuck).
-- ============================================================

-- 0. Use the "sakila" database.


-- 1. From the "payment" table, show 10 rows of customer_id,
--    rental_id, amount, and payment_date.


-- 2. From the "film" table, show 10 titles, release year, and
--    rental duration, for titles that start with the letter "S".


-- 3. From the "film" table, show the rental duration, how many
--    films exist for each rental duration, and the average film
--    length. Group the count and average by rental duration, and
--    round the average to 2 decimal places.
--    Rename the headers to 'Durasi_Rental', 'Banyak_Film', and
--    'Rata_Rata_Durasi_Film'.


-- 4. From the "film" table, show the title, length, and rating
--    for films whose length is above the overall average film
--    length. Show 25 rows.


-- 5. From the "film" table, show the rating, highest replacement
--    cost, lowest rental rate, and average length, grouped by
--    rating.
--    Rename the headers to 'Rating', 'Replacement_Cost_Tertinggi',
--    'Rental_Rate_Terendah', and 'Rata_Rata_Durasi'.


-- 6. Show 15 films whose title ends with the letter "K", along
--    with their title, length, and language.
--    Note: join the "film" table with the "language" table first.


-- 7. Show the film title (from "film"), first name, and last name
--    (from "actor") for the actor with actor_id = 14.
--    Note: join "film", "film_actor", and "actor" first.


-- 8. From the "city" table, show city and country_id. Only show
--    cities whose name contains the letter "d" anywhere and ends
--    with the letter "a". Show 15 rows ordered by city ascending.


-- 9. Show the genre name (from "category") and how many films
--    exist in each genre. Join "film", "film_category", and
--    "category" first, and order by film count ascending.


-- 10. From the "film" table, show title, description, length,
--     and rating for the 10 films whose title ends with the
--     letter "h" and whose length is above the average. Order
--     by title ascending.
