-- creates the MySQL server user user_0d_1 and grant all priviledges.
CREATE DATABASE
	IF NOT EXISTS hbtn_0d_1;
CREATE USER
	IF NOT EXISTS user_0d_1@localhost
	IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
	ON hbtn_0d_1.*
	TO user_0d_1@localhost
