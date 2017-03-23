--Sets up a MySQL db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT PRIVILEGES ON 'performance_schema'.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
