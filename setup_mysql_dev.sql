-- Sets up a MySQL db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT PRIVILEGES ON 'performance_schema'.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
