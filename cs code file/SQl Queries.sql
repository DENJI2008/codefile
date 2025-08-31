-- Create table
CREATE TABLE Student (
    RollNo INT PRIMARY KEY,
    Name VARCHAR(30),
    Class INT,
    Marks INT
);

-- Insert values
INSERT INTO Student VALUES (1, 'Aman', 12, 85);
INSERT INTO Student VALUES (2, 'Pooja', 12, 90);
INSERT INTO Student VALUES (3, 'Raj', 11, 78);

-- ALTER (add column)
ALTER TABLE Student ADD Age INT;

-- ALTER (modify datatype)
ALTER TABLE Student MODIFY Name VARCHAR(50);

-- ALTER (drop column)
ALTER TABLE Student DROP COLUMN Age;

-- UPDATE
UPDATE Student SET Marks = 95 WHERE RollNo = 2;

-- ORDER BY ascending
SELECT * FROM Student ORDER BY Marks ASC;

-- ORDER BY descending
SELECT * FROM Student ORDER BY Marks DESC;

-- DELETE
DELETE FROM Student WHERE RollNo = 3;

-- GROUP BY (aggregate functions)
SELECT Class, COUNT(*), MIN(Marks), MAX(Marks), SUM(Marks), AVG(Marks)
FROM Student
GROUP BY Class;
