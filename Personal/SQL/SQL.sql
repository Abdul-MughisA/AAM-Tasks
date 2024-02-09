-- Drop the tables if they exist --
DROP TABLE IF EXISTS TableProducts;
DROP TABLE IF EXISTS TableSubscriptions;
DROP TABLE IF EXISTS TableCustomers;

-- Create the databases --
CREATE TABLE TableProducts(
    ProductID CHAR(4) NOT NULL PRIMARY KEY,
    ProductName VARCHAR(20) NOT NULL,
    Subject VARCHAR(255),
    Level INT,
    Price DECIMAL(10,2),
);

CREATE TABLE TableCustomers(
    CustomerID CHAR(4) NOT NULL PRIMARY KEY,
    Title VARCHAR(50),
    FirstName VARCHAR(50),
    Surname VARCHAR(50),
    Email VARCHAR(50),
);

CREATE TABLE TableSubscriptions(
    SubscriptionID INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    StartDate DATE,
    EndDate DATE,
    -- Creating relationships --
    ProductID CHAR(4),
    CustomerID CHAR(4),
    FOREIGN KEY (ProductID) REFERENCES TableProducts(ProductID),
    FOREIGN KEY (CustomerID) REFERENCES TableCustomers(CustomerID),
);

INSERT INTO TableProducts VALUES ("P24", "Equations", "Maths", 2, 12.00);
INSERT INTO TableProducts VALUES ("P36", "Programming", "Comp Science", 4, 25.00);
INSERT INTO TableProducts VALUES ("P47", "Database", "Comp Science", 4, 25.00);

INSERT INTO TableCustomers VALUES ("C111", "Mr", "Fred", "Carr", "fcarr53@gmail.com");
INSERT INTO TableCustomers VALUES ("C245", "Miss", "Mabel", "Jenkins", "mabel777@bt.com");
INSERT INTO TableCustomers VALUES ("C364", "Miss", "Jasmine", "Kumar", "jkumar@icloud.com")

INSERT INTO TableSubscriptions (StartDate, EndDate, ProductID, CustomerID) VALUES ("2016-02-25", "2017-02-24", "P36", "C111");
INSERT INTO TableSubscriptions (StartDate, EndDate, ProductID, CustomerID) VALUES ("2016-02-01", "2017-01-31", "P47", "C111");
INSERT INTO TableSubscriptions (StartDate, EndDate, ProductID, CustomerID) VALUES ("2016-02-04", "2017-02-03", "P36", "C245");

SELECT * FROM TableProducts;
SELECT * FROM TableCustomers;
SELECT * FROM TableSubscriptions;
