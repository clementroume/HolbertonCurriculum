-- This script converts the `first_table` in the `hbtn_0c_0` database to use the UTF-8 character set (utf8mb4) 
-- with the `utf8mb4_unicode_ci` collation in your MySQL server for better support of multi-language and special characters.
USE hbtn_0c_0;
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
