# 0x0D. SQL - Introduction
## About
An introductory project on:
- Whats a database
- Whats a relational database
- What does SQL stand for
- Whats MySQL
- How to create a database in MySQL
- What does `DDL` and `DML` stand for
- How to `CREATE` or ALTER a table
- How to `SELECT` data from a table
- How to `INSERT`, `UPDATE` or `DELETE` data
- What are subqueries
- How to use MySQL functions
## Requirements
- Ubuntu 14.04
- MySQL 5.7

## File Descriptions
### Mandatory
**[0-list_databases.sql](0-list_databases.sql)** - Lists all databases of your MySQL server.

**[1-create_database_if_missing.sql](1-create_database_if_missing.sql)** - Creates the database `hbtn_0c_0` in your MySQL server.

**[2-remove_database.sql](2-remove_database.sql)** - Deletes the database `hbtn_0c_0` in your MySQL server.

**[3-list_tables.sql](3-list_tables.sql)** - Lists all the tables of a database in your MySQL server.

**[4-first_table.sql](4-first_table.sql)** - Creates a table called `first_table` in the current database in your MySQL server.

**[5-full_table.sql](5-full_table.sql)** - Prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

**[6-list_values.sql](6-list_values.sql)** - Lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

**[7-insert_value.sql](7-insert_value.sql)** - Inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.

**[8-count_89.sql](8-count_89.sql)** - Displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.

**[9-full_creation.sql](9-full_creation.sql)** - Creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.

**[10-top_score.sql](10-top_score.sql)** - Llists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

**[11-best_score.sql](11-best_score.sql)** - ists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

**[12-no_cheating.sql](12-no_cheating.sql)** - Updates the score of Bob to `10` in the table `second_table`.

**[13-change_class.sql](13-change_class.sql)** - Removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

**[14-average.sql](14-average.sql)** - Computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

**[15-groups.sql](15-groups.sql)** - Lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

**[16-no_link.sql](16-no_link.sql)** - Lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

### Advanced
**[100-move_to_utf8.sql](100-move_to_utf8.sql)** - Converts `hbtn_0c_0` database to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`) in your MySQL server.

**[101-avg_temperatures.sql](101-avg_temperatures.sql)** - Displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

**[102-top_city.sql](102-top_city.sql)** - Displays the top 3 of cities temperature during July and August ordered by temperature (descending)

**[103-max_state.sql](103-max_state.sql)** - Displays the max temperature of each state (ordered by State name).
