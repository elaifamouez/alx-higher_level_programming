-- create user and set password
CREATE USER IF NOT EXISTS 'user_0d_i1'@'localhost';
SET PASSWORD FOR 'user_0d_1'@'localhost' = 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
