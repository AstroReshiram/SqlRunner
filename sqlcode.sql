SET NOCOUNT ON --pyodbc doesn't like it and reports multiple lines. you can uncomment if using pymssql

IF NOT EXISTS (
    SELECT *
    FROM INFORMATION_SCHEMA.TABLES
      WHERE TABLE_NAME = 'people'
)
BEGIN
    CREATE TABLE people (
    name VARCHAR(50),
    age INT,
	date_registered DATE
);
END

INSERT INTO people (name, age, date_registered)
VALUES ('Mate', 20, '2023-01-01');

SELECT * FROM people ORDER BY name