-- This script creates a table named `first_table` in the current database on your MySQL server, with columns `id` (integer) and `name` (string of up to 256 characters).
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
