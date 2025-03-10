## 1. SQL executes the queries in the following order
- FROM
- WHERE
- GROUP BY
- HAVING
- SELECT
- DISTINCT
- ORDER BY
- LIMIT / OFFSET

### FROM
From selects the target the table
```sql
select * FROM table_name
```

### WHERE
Filter condition that happens before aggregations
```sql
select * from table_name WHERE condition
```
Some conditions are such as:
- WHERE column_name = 'sales'
- WHERE column_name > 100
- WHERE column_name BETWEEN 10 AND 100
- WHERE column_name first_condition AND second_condition AND third_condition
- WHERE column_name first_condition OR second_condition
- WHERE column_name in ('first_value', 'second_value', 'third_value')
- WHERE column_name LIKE 'A%' -> Filter value that starts with the letter 'A'
- WHERE column_name IS NULL
- WHERE (condition_one and condition_two) or (condition_three and condition_four)

### GROUP BY
Collect rows that share a common value in one or more columns into summary row.
Often used with aggregate functions such as COUNT, SUM, AVG, MAX, MIN
```sql
employee_id	name	department	salary
      1	    Alice	Sales	    50000
      2	    Bob	    HR	        45000
      3	    Charlie	Sales	    55000
      4	    David	IT	        60000
      5	    Eve	    HR	        48000

SELECT department, COUNT(*) AS num_employees
FROM employees
GROUP BY department;

RESULT:
department	employee_count
Sales	    2
HR	        2
IT	        1
```
Group By usages:
- select aggregate_func as new_column_name from table GROUP BY column

### HAVING
Similar to a where condition, used when you need to filter after a aggregate function
like count, sum, avg, max, min etc.
```sql
employee_id	name	department	salary
      1	    Alice	Sales	    50000
      2	    Bob	    HR	        45000
      3	    Charlie	Sales	    55000
      4	    David	IT	        60000
      5	    Eve	    HR	        48000

SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 1;

RESULT:
department	employee_count
Sales	    2
HR	        2
```
Usages:
- HAVING aggregate_func conditions
- HAVING condition_one AND condition_two


### SELECT
Selecting columns from a table or from a sub query, or from a CTE
```sql
SELECT column_1, column_2 from table_name
```
Usage:
- select multiple columns from table
- select column_1, column_2 from (select column_3, column_4 from table 1)
- select all from (CTE)


### DISTINCT
To remove duplicate rows from the result set of a query. Ensures only unique values
are returned

```sql
# Return unique values from the particular column
select DISINCT column_name from table_name

# Return counts of unique 
Return number of unique 
SELECT COUNT(DISTINCT customer_id) AS unique_customers
FROM orders;
```
Usage:
- select DISTINCT column_name...
- DISTINCT must come after select


### Order By
Arranges the final set of results in an asc or desc order

```sql
SELECT product_name, price
FROM products
ORDER BY price;

# Default ordering is by asc
```
Usages:
- Multiple ordering, ORDER BY department, salary DESC; -> For each employee in the same department, order them in desc
- Ordering by column position, ORDER BY 3; -> Order in asc by the 3rd column


### Limit / Offset
The LIMIT and OFFSET clauses are often used together to control the number of rows returned in a query, making them especially useful for pagination.
Limit -> Limit the number of rows returned
Offset -> Skip the first n rows and return from there
```sql
SELECT * FROM customers
ORDER BY customer_id
LIMIT 5 OFFSET 10;

# Skip the first 10 rows, then return the next 5 rows
```

## 2. Aggregate Functions
### COUNT
When used as COUNT(*), it counts all rows, including those with NULL values. 
When used as COUNT(column), it counts only the rows where the column value is not NULL.
### SUM
It adds up all numeric values in a column. It's important that the column contains numeric data, as SUM only works 
with numbers.
### AVG
It calculates the average (mean) of the values in a numeric column. Like SUM, AVG operates on numeric data and 
ignores NULLs.
### MAX
It returns the maximum value in a column. This can be applied to both numeric and text data (for text, it uses 
lexicographical order).
### MIN
It returns the minimum value in a column. Like MAX, this works with both numeric and text data.

## 3. Mathematical Functions
### LIKE
To perform pattern-based searches in text data.
% matches any sequence of characters (including none).
    - %ABC -> filter rows with values ending with ABC
    - ABC% -> filter rows with values starting with ABC
_ matches exactly one character.
### BETWEEN
To determine if a value lies within a certain range. It is inclusive, meaning it includes both the lower and 
upper bounds in the result.
```sql
expression BETWEEN lower_bound AND upper_bound

# Lexicographically
SELECT *
FROM employees
WHERE last_name BETWEEN 'A' AND 'M';

# Date Range
SELECT *
FROM orders
WHERE order_date BETWEEN '2025-01-01' AND '2025-01-31';
```
### "!= or <>"
Not Equal
### "> / >="
More or more and equal to
### "< / <="
Less or less and equal to
### IN / NOT IN
Filters out rows that are in or not inside the list
### IS NULL / IS NOT NULL
Checks for null values
### ROUND
used to round a numeric value to a specified number of decimal places. This function is valuable for formatting output, 
ensuring numeric precision, and making data more readable.
```sql
SELECT product_name,
       price,
       ROUND(price, 2) AS rounded_price
FROM products;

Rounding to 2 decimal places
```
### EXISTS
Test existence of a record in a sub query
```sql
SELECT customer_id, name
FROM customers
WHERE EXISTS (
    SELECT 1
    FROM orders
    WHERE orders.customer_id = customers.customer_id
);

```
### ANY / ALL
Compares a value to any or all values returned by a subquery
```sql
SELECT product_name, price
FROM products
WHERE price > ANY (
    SELECT price
    FROM products
    WHERE category = 'Electronics'
);
```


## 4a. Window Functions (Must have OVER keyword after using a Window function)
Window functions in SQL let you perform calculations across a set of table rows related to the current 
row without collapsing the result set. Various databases have their own sets of varying
window functions. A window function is called OVER a set of rows. The OVER keyword is always
present after a window function in a sql query.
### A. Ranking Functions
#### RANK()
Ranks WITH skipping when encountering similar values
eg:
1 Rank 1
1 Rank 1
2 Rank 3
#### DENSE_RANK()
Ranks WITHOUT skipping when encountering similar values
eg:
1 Rank 1
1 Rank 1
2 Rank 2
#### ROW_NUMBER()
Assigns a unique sequential integer counter to each row within a result set.
Starts from 1.
```sql
SELECT 
    employee_name,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```
#### NTILE(n)
Divides the rows in a partition into n approximate equal group


### B. Value Functions
#### LAG
Returns the value from a previous row in the window (by default, immediately the preceding row)
```sql
CREATE TABLE Sales (
    sale_id INT,
    sale_date DATE,
    revenue DECIMAL(10,2)
);

For each sale, this query retrieves the revenue from the previous sale (ordered by sale_date). 
If there’s no previous row (like the first row), it returns 0 (the default).
```
#### LEAD
Returns the value from a previous row in the window (by default, the immediately preceding row).
```sql
SELECT 
    sale_id,
    sale_date,
    revenue,
    LEAD(revenue, 1, 0) OVER (ORDER BY sale_date) AS next_revenue
FROM Sales;

For each sale, this retrieves the revenue from the next sale (by sale_date). If there’s no next row, it returns 0.
```
#### FIRST_VALUE
Returns the first value in the window (based on the ordering).
```sql
SELECT 
    sale_id,
    sale_date,
    revenue,
    FIRST_VALUE(revenue) OVER (
        ORDER BY sale_date 
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS first_sale_revenue
FROM Sales;

This gives the revenue of the very first sale when ordered by sale_date. 
The window frame (using ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) ensures that the entire partition 
is considered.
```
#### LAST_VALUE
Returns the last value in the window.
```sql
SELECT 
    sale_id,
    sale_date,
    revenue,
    LAST_VALUE(revenue) OVER (
        ORDER BY sale_date 
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS last_sale_revenue
FROM Sales;

This returns the revenue of the very last sale in the ordering. Note that without specifying the proper window frame, 
the default might not cover the entire partition and might return the current row's value instead.
```
#### NTH_VALUE
Returns the nth value in the window.
```sql
SELECT 
    sale_id,
    sale_date,
    revenue,
    NTH_VALUE(revenue, 2) OVER (
        ORDER BY sale_date 
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS second_sale_revenue
FROM Sales;

This retrieves the revenue from the second sale in the ordered list. Like LAST_VALUE, 
specifying the window frame ensures you’re considering all rows in the partition.
```

### C. Distribution Functions
#### PERCENT_RANK()
Calculates the relative rank of a row as a percentage.
PERCENT_RANK= (rank - 1) / (total_rows - 1)
```sql
SELECT 
    sale_id,
    revenue,
    PERCENT_RANK() OVER (ORDER BY revenue) AS percent_rank
FROM Sales;

This query orders the rows by revenue. For each row, it calculates what percentage of rows come before it. 
If a row is the first (lowest revenue), it gets 0. If it’s the last (highest revenue), it gets 1.
```

#### CUME_DIST()
Calculates the fraction of rows that have a value less than or equal to the current row’s value. 
Essentially, it tells you the cumulative proportion of rows up to that point.
```sql
SELECT 
    sale_id,
    revenue,
    CUME_DIST() OVER (ORDER BY revenue) AS cume_dist
FROM Sales;

This query also orders the rows by revenue. For each row, CUME_DIST() returns the ratio of the number of rows with a 
revenue less than or equal to the current row’s revenue to the total number of rows. Thus, if 70% of the rows have 
revenue less than or equal to the current row, CUME_DIST() will return 0.7.
```

#### Agg functions as window functions
Aggregate functions like SUM(), AVG(), MIN(), MAX(), and COUNT() are typically used to summarize data. When used with 
an OVER() clause, they become window functions that can compute these summaries across a specific “window” of rows 
while still returning individual row details.
```sql
SELECT 
    sale_id,
    sale_date,
    revenue,
    SUM(revenue) OVER (
        ORDER BY sale_date 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM Sales;

For each row, the SUM() function calculates the total revenue from the first sale up to the current sale 
(ordered by sale_date). The window frame ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW ensures that the aggregation 
covers all rows from the beginning of the partition up to the current row.


SELECT 
    sale_id,
    sale_date,
    revenue,
    AVG(revenue) OVER (
        PARTITION BY YEAR(sale_date)
    ) AS yearly_avg
FROM Sales;


This query divides the data into partitions based on the year. Within each partition (year), AVG() calculates the 
average revenue. Each row in the same year will show the same yearly_avg.
```

## 4b. PARTITION BY
Used in conjunction with window function. Partition by divides the result sets into partitions for the window function
to act upon. The window function is then applied independently to each partition using the OVER keyword
```sql
SELECT employee_id, department, salary,
       AVG(salary) OVER (PARTITION BY department) AS avg_dept_salary
FROM employees;
```
Usages
- Partition by multiple columns
- Dynamic Partition -> PARTITION BY YEAR(sale_date)
- No Partition
```sql
 SELECT 
    sale_id, 
    sale_date, 
    revenue,
    SUM(revenue) OVER (ORDER BY sale_date) AS running_total
FROM Sales;
```

## 5. Conditional Expressions
### Case When Then
To implement conditional logic in SQL. Think of it as If Else Then.
Purpose: Compute or derive new values using conditional logic.
Effect: Adds new computed columns or influences ordering, but it does not remove rows from the result set.
```sql
SELECT employee_id, salary,
       CASE 
         WHEN salary >= 60000 THEN 'High'
         WHEN salary >= 40000 THEN 'Medium'
         ELSE 'Low'
       END AS salary_category
FROM employees;

This categorization clearly differentiates CASE WHEN from filtering clauses like WHERE or HAVING, emphasizing its 
role in computing conditional values rather than filtering rows.
```
Usage:
- Used in Where
```sql
SELECT employee_id, salary
FROM employees
WHERE (CASE 
         WHEN department = 'Sales' THEN salary
         ELSE salary * 1.1
       END) > 50000;
       
Here, the CASE expression applies a different multiplier depending on the department, and then filters based 
on the computed value.
```
- Used in Order By
```sql
SELECT employee_id, salary
    FROM employees
    ORDER BY CASE 
           WHEN salary >= 60000 THEN 1
           WHEN salary >= 40000 THEN 2
           ELSE 3
         END;
         
This orders the rows based on the computed category, placing high-salary employees first, followed by medium, then low.
```

### COALESCE
Returns the first non-NULL value in a list of expressions.
```sql
SELECT employee_id, COALESCE(commission, 0) AS commission_amount
FROM employees;

This ensures that if commission is NULL, 0 is used instead.
```

### NULLIF
Compares two expressions and returns NULL if they are equal; otherwise, returns the first expression.
```sql
SELECT employee_id,
       NULLIF(salary, 0) AS non_zero_salary
FROM employees;

This returns NULL for rows where the salary is 0.
```

## 6. Types and Conversions
### CAST
Convert and expression from one type to another
```sql
CAST(expression AS data_type)

SELECT CAST('2025-03-08' AS DATE) AS my_date;
```

### DATE / DATETIME / TIMESTAMP
DATE type in the form of '2025-01-01'
DATETIME / TIMESTAMP in the form of '2025-01-01 12:00:00' (Varies across SQL dialects)

### VARCHAR(n) / TEXT / CHAR(n)
VARCHAR(10) -> String type in the form of 'string'. (10) represents 10 characters.
TEXT -> Larger blocks of text
CHAR(5) -> String of 5 chars, if shorter, padded with spaces

### SMALLINT / INT / BIGINT / DECIMAL / FLOAT
SMALLINT -> -32,768 to 32767 (2 bytes)
INT -> -2,147,483,648 to 2,147,483,647 (4 bytes)
BIGINT ->  -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 (8 bytes)
DECIMAL(5,2) -> 5 digits, 2 decimal places
FLOAT -> Approx type, can cause rounding errors. 7 decimal precision only

### BOOLEAN
BOOLEAN -> true / false


## 7. JOINS
### LEFT / RIGHT JOIN
Retrieves all records from left table and only matching records from right table. (Vice Versa for right join)
```sql
SELECT * FROM A LEFT/RIGHT JOIN B ON A.key = B.key
```

### INNER JOIN
Retrieves records with matching values from both table
```sql
SELECT * FROM A INNER JOIN B ON A.key = B.key
```

### FULL JOIN
Retrieves all records when there is a match
```sql
SELECT * FROM A FULL OUTER JOIN B ON A.key = B.key
```

### LEFT / RIGHT JOIN with NULL CHECK
Filter only the records where there is no match in the left/right table. Return rows that exist in A but not in B
```sql
SELECT * FROM A LEFT/RIGHT JOIN B ON A.key = B.key WHERE B.key IS NULL
```

### FULL JOIN WITH NULL CHECK
Filters only records where there is no match between A or B (NULL values check in either)
```sql
SELECT * FROM A FULL OUTER JOIN B ON A.key = B.key WHERE A.key IS NULL OR B.key IS NULL
```
