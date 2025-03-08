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

## 3. Comparison Functions
### LIKE
### BETWEEN
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


## 4a. Window Functions
Window functions in SQL let you perform calculations across a set of table rows related to the current 
row without collapsing the result set. Various databases have their own sets of varying
window functions. A window function is called OVER a set of rows. The OVER keyword is always
present after a window function in a sql query.
### Ranking Functions
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


### Value Functions
#### LAG
#### LEAD
#### FIRST_VALUE
#### LAST_VALUE
#### NTH_VALUE

### Distribution Functions
#### PERCENT_RANK()
#### CUME_DIST()
#### Agg functions as window functions


## 4b. PARTITION BY
Used in conjunction with window function. Partition by divides the result sets into partitions for the window function
to act upon. The window function is then applied independently to each partition using the OVER keyword
```sql
SELECT employee_id, department, salary,
       AVG(salary) OVER (PARTITION BY department) AS avg_dept_salary
FROM employees;
```
