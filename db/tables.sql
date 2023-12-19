CREATE DATABASE `hospital`;
USE `hospital`;

CREATE TABLE doctors_cardiology (
    doctors_cardiology_id int NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    address VARCHAR(100) NOT NULL,
    phone_number VARCHAR(50) NOT NULL,
    specialization VARCHAR(50) NOT NULL,
    PRIMARY KEY (doctors_cardiology_id)
);

CREATE TABLE doctors_dermatology (
    doctors_dermatology_id int NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    address VARCHAR(100) NOT NULL,
    phone_number VARCHAR(50) NOT NULL,
    specialization VARCHAR(50) NOT NULL,
    PRIMARY KEY (doctors_dermatology_id)
);

CREATE TABLE doctors_endocrinology (
    doctors_endocrinology_id int NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    address VARCHAR(100) NOT NULL,
    phone_number VARCHAR(50) NOT NULL,
    specialization VARCHAR(50) NOT NULL,
    PRIMARY KEY (doctors_endocrinology_id)
);

CREATE TABLE doctors_gastroenterology (
    doctors_gastroenterology_id int NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    address VARCHAR(100) NOT NULL,
    phone_number VARCHAR(50) NOT NULL,
    specialization VARCHAR(50) NOT NULL,
    PRIMARY KEY (doctors_gastroenterology_id)
);

SHOW TABLES; 

SELECT * FROM doctors_cardiology;
SELECT * FROM doctors_dermatology;
SELECT * FROM doctors_endocrinology;
SELECT * FROM doctors_gastroenterology;