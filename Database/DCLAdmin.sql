
CREATE USER 'anvesh'@'localhost' IDENTIFIED BY 'Anv@14078';


-- only select on a particular table 
GRANT SELECT ON ihub.employees TO 'anvesh'@'localhost';
GRANT SELECT,INSERT ON ihub.employees TO 'anvesh'@'localhost';


-- one data base all tables
GRANT ALL PRIVILEGES on ihub.* TO 'anvesh'@'localhost';

-- all databases all tables 
GRANT ALL PRIVILEGES on *.* TO 'anvesh'@'localhost';


SHOW GRANTS FOR 'anvesh'@'localhost'


REVOKE SELECT ON ihub.employees FROM 'anvesh'@'localhost';



DROP USER 'anvesh'@'localhost';


ALTER USER 'admin'@'localhost' IDENTIFIED WITH 'Anv@14078' BY 'Anv@14078';
FLUSH PRIVILEGES;
