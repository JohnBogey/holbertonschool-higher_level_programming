-- creates user with all privleges of MySql server
CREATE USER IF NOT EXIST 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
