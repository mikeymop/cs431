--Finished DB Schema
create table Photographer
(
PName varchar(50),
PBDate date,
Pbio varchar(100),
Paddress varchar(100),
Pnationality varchar(30),
Color ENUM('C','B/W') NOT NULL,
PRIMARY KEY (PName, PBDate)
);

Create Table Customer (
    LoginName VARCHAR(25) PRIMARY KEY,
    `Password` VARCHAR(50),
    CName VARCHAR(50),
    CardType VARCHAR(8),
    BillingAddress VARCHAR(50),
    Str1 VARCHAR(25),
    Str2 VARCHAR(25),
    City VARCHAR(25),
    State VARCHAR(4),
    Zip VARCHAR(10)
);

Create Table Transaction (
    TransID int Auto_Increment PRIMARY KEY,
    TDate date,
    CardNo VARCHAR(25),
    `Card Type` VARCHAR(10),
    CardExpDate Date,
    TotalAmount Decimal(6,3),
    LoginName VARCHAR(25) Not NULL,
    FOREIGN KEY (LoginName) REFERENCES Customer(LoginName)
);

create table Photo (
 PhotoID int AUTO_INCREMENT PRIMARY KEY,
 Speed varchar(10),
 Film varchar(25),
 `F-Stop` varchar(20),
 Color ENUM('C','B/W') NOT NULL,
 Resolution VARCHAR(12),
 Price DECIMAL(6,3),
 `Date` Date,
 TransID int,
 PName varchar(50),
 PBDate date,
 Constraint pk_pname FOREIGN KEY (`PName`,`PBDate`) REFERENCES Photographer(`PName`,`PBDate`)
);

create table Model (
    MName VARCHAR(50),
    MBDate Date,
    MBio VARCHAR(250),
    MSex ENUM('M','F') NOT NULL,
    Primary Key (MName, MBDate)
);

create table Models (
	PhotoID int AUTO_INCREMENT PRIMARY KEY,
    MName VARCHAR(50),
    MBDate Date,
    Agency VARCHAR(25),
    Constraint pk_mname FOREIGN KEY (`MName`, `MBDate`) REFERENCES Model(`MName`, `MBDate`)
);

create table Location (
    Place VARCHAR(50),
    Country VARCHAR(25),
    Description VARCHAR(250),
    Primary Key (Place, Country)
);

create table Landscape (
	PhotoID int AUTO_INCREMENT PRIMARY KEY,
    Place VARCHAR(50),
    Country VARCHAR(25),
    Constraint pk_loc FOREIGN KEY (`Place`, `Country`) REFERENCES Location(`Place`, `Country`)
);

create table Influences (
	EPName VARCHAR(50),
    EPBDate Date,
    RPName VARCHAR(50),
    RPBDate Date,
    Primary Key (`EPName`, `EPBDate`),
    Constraint pk_rpname FOREIGN KEY (`RPName`, `RPBDate`) REFERENCES Photographer(`PName`,`PBDate`)
);

create table Abstract (
	PhotoID int AUTO_INCREMENT PRIMARY KEY,
    Comment VARCHAR(250),
    FOREIGN KEY (`PhotoID`) REFERENCES Photo(`PhotoID`)
);
