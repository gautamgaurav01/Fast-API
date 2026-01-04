-- =============================================
-- joins_queries_explained.sql
-- Purpose: Examples of SQL JOINs and aggregation with explanations
-- =============================================
-- 1. RIGHT JOIN
-- Use: Get all users and their posts (if any). Shows all users even if they have no posts
SELECT
    *
FROM
    posts
    RIGHT JOIN users ON posts.owner_id = users.id;

-- 2. LEFT JOIN
-- Use: Get all posts and their owners (if any). Shows all posts even if owner does not exist
SELECT
    *
FROM
    posts
    LEFT JOIN users ON posts.owner_id = users.id;

-- 3. LEFT JOIN with COUNT (group by user)
-- Use: Count how many posts each user has
SELECT
    users.id,
    COUNT(*)
FROM
    posts
    LEFT JOIN users ON posts.owner_id = users.id
GROUP BY
    users.id;

-- 4. View all users
SELECT
    *
FROM
    users;

-- 5. RIGHT JOIN with COUNT (group by user)
-- Use: Count posts per user, ensuring all users appear even if no posts
SELECT
    users.id,
    COUNT(*)
FROM
    posts
    RIGHT JOIN users ON posts.owner_id = users.id
GROUP BY
    users.id;

-- 6. RIGHT JOIN with COUNT(posts.id)
-- Use: Only counts actual posts for each user, 0 if none
SELECT
    users.id,
    COUNT(posts.id)
FROM
    posts
    RIGHT JOIN users ON posts.owner_id = users.id
GROUP BY
    users.id;

-- 7. LEFT JOIN posts and votes
-- Use: Shows all posts with votes (if any). Posts without votes will still appear
SELECT
    *
FROM
    posts
    LEFT JOIN votes ON posts.id = votes.post_id;

-- 8. RIGHT JOIN posts and votes
-- Use: Shows all votes with post details (if any). Votes without post details will still appear
SELECT
    *
FROM
    posts
    RIGHT JOIN votes ON posts.id = votes.post_id;

-- 9. LEFT JOIN with COUNT (posts and votes)
-- Use: Count votes per post, include posts with 0 votes
SELECT
    posts.id,
    COUNT(*)
FROM
    posts
    LEFT JOIN votes ON posts.id = votes.post_id
GROUP BY
    posts.id;

-- 10. RIGHT JOIN with COUNT (posts and votes)
-- Use: Count votes per post, include votes with missing post info if any
SELECT
    posts.id,
    COUNT(*)
FROM
    posts
    RIGHT JOIN votes ON posts.id = votes.post_id
GROUP BY
    posts.id;