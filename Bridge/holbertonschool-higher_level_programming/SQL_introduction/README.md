# SQL - Introduction

Welcome to the **SQL - Introduction** project repository! This project is part of the **Holberton School Higher-Level Programming** curriculum and serves as an introduction to SQL. It teaches how to interact with relational databases using SQL queries.

## Table of Contents

1. [Description](#description)
2. [Project Structure](#project-structure)
3. [Learning Objectives](#learning-objectives)

---

## Description

This project introduces the basics of SQL and relational database management systems (RDBMS). It covers:

- Writing SQL queries to manage and manipulate data.
- Understanding how relational databases work and how to interact with them.
- Performing simple CRUD operations (Create, Read, Update, Delete).
- Using SQL commands like `JOIN`, `GROUP BY`, `ORDER BY`, `LIMIT`, and others to extract meaningful information from data.

Through this project, hands-on experience with relational databases is gained, and the basic principles of SQL are applied to real-world database management tasks.

---

## Project Structure

Here’s an overview of the files included in the `SQL_introduction` directory:

| **File**                           | **Description**                                                                     |
| ---------------------------------- | ----------------------------------------------------------------------------------- |
| `0-list_databases.sql`             | Lists all databases in the MySQL server.                                            |
| `1-create_database_if_missing.sql` | Creates the database `hbtn_0c_0` if it doesn't already exist.                       |
| `2-remove_database.sql`            | Deletes the database `hbtn_0c_0` if it exists.                                      |
| `3-list_tables.sql`                | Lists all tables in the `hbtn_0c_0` database.                                       |
| `4-first_table.sql`                | Creates a table called `first_table` in the current database.                       |
| `5-full_table.sql`                 | Shows the table creation details for `first_table`.                                 |
| `6-list_values.sql`                | Lists all rows in the `first_table` of the `hbtn_0c_0` database.                    |
| `7-insert_values.sql`              | Inserts a new row into `first_table` of the `hbtn_0c_0` database.                   |
| `8-count_89.sql`                   | Counts the number of rows with `id = 89` in the `first_table`.                      |
| `9-full_creation.sql`              | Creates `second_table` and inserts multiple rows into it.                           |
| `10-top_score.sql`                 | Lists rows in `second_table` ordered by score in descending order.                  |
| `11-best_score.sql`                | Lists rows in `second_table` with a score >= 10, ordered by score.                  |
| `12-no_cheating.sql`               | Updates the score of Bob to 10 in `second_table`.                                   |
| `13-change_class.sql`              | Deletes records with a score <= 5 in `second_table`.                                |
| `14-average.sql`                   | Calculates the average score in `second_table`.                                     |
| `15-groups.sql`                    | Groups records by score and counts the occurrences of each score in `second_table`. |
| `16-no_link.sql`                   | Lists records in `second_table` where `name` is not empty, ordered by score.        |
| `100-move_to_utf8.sql`             | Converts `first_table` to UTF-8 encoding.                                           |
| `101-avg_temperatures.sql`         | Displays the average temperature by city, ordered by temperature.                   |
| `102-top_city.sql`                 | Displays the top 3 cities with the highest average temperature for July and August. |
| `103-max_state.sql`                | Displays the maximum temperature for each state, ordered by state name.             |

---

## Learning Objectives

By the end of this project, the following skills will be acquired:

- Mastery of SQL syntax for querying relational databases.
- Ability to create and manipulate databases and tables.
- Knowledge of how to insert, update, select, and delete data using SQL queries.
- Understanding of basic SQL operations and how they interact with relational databases.

---
