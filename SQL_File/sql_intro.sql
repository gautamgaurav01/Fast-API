-- =============================================
-- products_queries_explained.sql
-- Purpose: Common SQL operations on the `products` table with explanations
-- =============================================
-- 1. View all records from the products table
-- Use: Fetches every column and every row
SELECT
    *
FROM
    products;

-- 2. Filter with multiple conditions
-- Use: Returns products that meet ANY of the following:
--  - inventory is 0 AND product is on sale
--  - price greater than 200
--  - id is one of (1,2,3,4)
-- Note: AND has higher precedence than OR
SELECT
    *
FROM
    products
WHERE
    (
        inventory = 0
        AND is_sale = true
    )
    OR price > 200
    OR id IN (1, 2, 3, 4);

-- 3. Pattern matching using LIKE
-- Use: Finds products whose name contains letter 'R'
-- % means any number of characters
SELECT
    *
FROM
    products
WHERE
    name LIKE '%R%';

-- 4. Sorting records
-- Use: Orders products by newest first
-- DESC = descending, ASC = ascending
SELECT
    *
FROM
    products
ORDER BY
    created_at DESC;

-- 5. Limit result set
-- Use: Gets only 2 products with price greater than 300
SELECT
    *
FROM
    products
WHERE
    price > 300
LIMIT
    2;

-- 6. Insert new product
-- Use: Adds a new row to the table
INSERT INTO
    products (name, price, inventory)
VALUES
    ('sandesh', 500, 1);

-- 7. Delete a product
-- Use: Removes the row with id = 12
-- Warning: This permanently deletes data
DELETE FROM products
WHERE
    id = 12;

-- 8. Update multiple columns
-- Use: Changes name and price for product with id = 2
UPDATE products
SET
    name = 'TV',
    price = 400
WHERE
    id = 2;

-- 9. Update and return updated row
-- Use: Sets is_sale to false and shows the updated record
-- RETURNING * is supported in PostgreSQL
UPDATE products
SET
    is_sale = false
WHERE
    id = 6 RETURNING *;