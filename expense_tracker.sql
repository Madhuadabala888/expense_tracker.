
-- Expense Tracker & Personal Finance Manager

CREATE DATABASE expense_tracker;

USE expense_tracker;

-- Create Expenses Table

CREATE TABLE expenses (
    expense_id INT PRIMARY KEY AUTO_INCREMENT,
    expense_date DATE NOT NULL,
    category VARCHAR(50) NOT NULL,
    description VARCHAR(100),
    amount DECIMAL(10,2) NOT NULL
);

-- Insert Sample Expenses

INSERT INTO expenses (expense_date, category, description, amount)
VALUES
('2026-09-01', 'Food', 'Dinner', 350.00),
('2026-09-02', 'Travel', 'Bus Fare', 100.00),
('2026-09-03', 'Shopping', 'Groceries', 250.00);

-- View Expenses

SELECT * FROM expenses;

-- Update Expense

UPDATE expenses
SET category = 'Food',
    description = 'Dinner',
    amount = 350.00
WHERE expense_id = 1;

-- Delete Expense

DELETE FROM expenses
WHERE expense_id = 3;

-- Total Expense

SELECT SUM(amount) AS TotalExpense
FROM expenses;

-- Search Expense

SELECT *
FROM expenses
WHERE category LIKE '%Food%';

-- Category-wise Expense

SELECT category, SUM(amount) AS TotalAmount
FROM expenses
GROUP BY category;
