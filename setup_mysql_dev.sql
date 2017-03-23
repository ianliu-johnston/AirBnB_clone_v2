-- Sets up hbnb_dev_db for user hbnb_dev, granting all privileges
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
GRANT ALL ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- GRANT ALL PRIVILEGES ON `hbnb_dev_db TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON 'performance_schema'.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
