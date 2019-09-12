-- new database and user
-- sudo mysql < ./deployment/mysql.sql

-- CREATE DATABASE appdb CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE USER 'app'@'%' IDENTIFIED BY 'app';
GRANT ALL ON appdb.* TO 'app'@'%';
FLUSH PRIVILEGES;

-- CREATE USER 'app'@'localhost' IDENTIFIED BY 'app';
-- GRANT ALL ON appdb.* TO 'app'@'localhost';
-- FLUSH PRIVILEGES;
