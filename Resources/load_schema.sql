CREATE TABLE Employee(
	employee_id INT PRIMARY KEY,
    emp_name VARCHAR(20),
    payrate INT NOT NULL,
    weekly_hours_worked DECIMAL(4,2),
    start_date DATE NOT NULL,
    end_date DATE,
    active_employee BOOL,
    email VARCHAR(100) UNIQUE,
    phone_num VARCHAR(9) UNIQUE,
    emp_dob DATE NOT NULL
);

DESCRIBE Employee;

CREATE TABLE Products (
	product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    price DECIMAL(4, 2),
    vendor VARCHAR(50),
    category VARCHAR(50),
    prod_amount INT,
    in_stock bool
);

DESCRIBE Products;

CREATE TABLE Customers(
	customer_id INT PRIMARY KEY,
    customer_name VARCHAR(20),
    customer_email VARCHAR(50) UNIQUE,
    customer_dob DATE NOT NULL
);

DESCRIBE Customers;

CREATE TABLE Transactions(
	transaction_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    price DECIMAL,
    employee_id INT,
    emp_name VARCHAR(20),
    customer_name VARCHAR(20),
    time_of_transaction TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (employee_id) REFERENCES Employee(employee_id)
    );
    
    DESCRIBE Transactions;
    
    CREATE TABLE Supervisor(
		supervisor_id INT PRIMARY KEY,
        supervisor_name VARCHAR(20)
    );
    
    DESCRIBE Supervisor;
    
    CREATE TABLE Category(
		category_id INT PRIMARY KEY,
        category_name VARCHAR(20)
    );
    
    DESCRIBE Category;
    
    CREATE TABLE Vendor(
		vendor_id INT PRIMARY KEY,
        vendor_name VARCHAR(50),
        location VARCHAR(50),
        order_status VARCHAR(20)
    );
    
    DESCRIBE Vendor;
