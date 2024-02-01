DROP TABLE IF EXISTS TableProducts;
DROP TABLE IF EXISTS TableSubscriptions;
DROP TABLE IF EXISTS TableCustomers;

CREATE TABLE TableProducts(
    ProductID CHAR(4) NOT NULL PRIMARY KEY,
    ProductName VARCHAR(20) NOT NULL,
    Subject VARCHAR(255),
    Level int,
    Price DECIMAL(10,2),
);

CREATE TABLE TableCustomers(
    CustomerID CHAR(4) NOT NULL PRIMARY KEY,
    Title VARCHAR(255),
    ProductName VARCHAR(255),
    Surname VARCHAR(255),
    Email VARCHAR(255),
    FOREIGN KEY ProductName REFERENCES TableProducts(ProductName),
);

CREATE TABLE TableSubscriptions(
    SubscriptionID int NOT NULL AUTO_INCREMENT,
    StartDate DATE,
    EndDate DATE,
    CustomerID CHAR(4),
    ProductID CHAR(3),
    FOREIGN KEY ProductID REFERENCES TableProducts(ProductID),
    FOREIGN KEY CustomerID REFERENCES TableCustomers(CustomerID),
);

INSERT INTO TableProducts VALUES ("P24", "Equations", "Maths", 2, 12.00);

