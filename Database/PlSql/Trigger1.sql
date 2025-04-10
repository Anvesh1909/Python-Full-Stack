USE IHUB;

SHOW TABLEs;

SELECT * FROM employees;

INSERT INTO employees VALUES(11,"Apra",1000000,"Borol-Hyderabad");


DROP Table logbook;

CREATE TABLE logBook(
    id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(200),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP Trigger Show_table_on_insert


CREATE TRIGGER LogBookInsert
AFTER INSERT ON employees
FOR EACH ROW
BEGIN
    INSERT INTO logbook(message) VALUES(CONCAT("Added employee ",NEW.ename));
END;


SELECT * FROM logbook;

INSERT INTO employees VALUES(12,"Apra3",1000000,"Borol-Hyderabad");


