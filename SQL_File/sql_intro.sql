
--SELECT * FROM products
--SELECT * FROM products where inventory=0 and is_sale=true or price > 200 or id in (1,2,3,4);

--SELECT * FROM products where name LIKE '%R%'; -- filtering the details 

--SElECT * FROM products ORDER BY created_at DESC  --DESC descending ASC ascending

--SELECT * FROM products WHERE price >300 LIMIT 2

--INSERT INTO products (name,price,inventory) VALUES ('sandesh',500,1);  -- add items

--DELETE FROM products where id =12 ;  --delete rows

--UPDATE products SET name = 'TV' , price =400 WHERE id=2  -- update item

--UPDATE products SET is_sale=false WHERE id =6 RETURNING *  -- update item 


--SELECT * FROM products