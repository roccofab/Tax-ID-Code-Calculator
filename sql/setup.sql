CREATE DATABASE IF NOT EXISTS tax_id_code;

USE tax_id_code;

CREATE TABLE `tax_code` (
  `name` varchar(45) NOT NULL,
  `surname` varchar(45) NOT NULL,
  `birth_date` date NOT NULL,
  `gender` char(1) DEFAULT NULL,
  `municipality_code` varchar(45) NOT NULL,
  `tax_code` varchar(45) NOT NULL,
  PRIMARY KEY (`tax_code`)
);