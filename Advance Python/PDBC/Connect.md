

If you already have MySQL installed on your system and want to install XAMPP's MySQL server, here are the steps to avoid conflicts and successfully set up both:

---

### 1. **Check Existing MySQL Installation**
   - Confirm that MySQL is installed and running by executing:
     ```bash
     mysql --version
     ```
   - Note the existing MySQL port (default is `3306`):
     - Open `my.cnf` or `my.ini` (MySQL configuration file).
     - Look for:
       ```ini
       [mysqld]
       port=3306
       ```
     - If it is `3306`, you'll need to adjust the port for XAMPP's MySQL server later.

---

### 2. **Download and Install XAMPP**
   - Download the XAMPP installer from [Apache Friends](https://www.apachefriends.org/).
   - Run the installer and follow the instructions.
   - During installation, select `MySQL` as a component to install.

---

### 3. **Change XAMPP MySQL Port**
   To avoid port conflicts with the existing MySQL server:
   1. **Open XAMPP's MySQL Configuration File**:
      - Navigate to the XAMPP installation directory (e.g., `C:\xampp`).
      - Open `mysql\bin\my.ini` using a text editor.
   2. **Update the Port**:
      - Change the port to something other than `3306`, such as `3307`:
        ```ini
        [mysqld]
        port=3307
        ```
   3. **Save and Close the File**.

---

### 4. **Start XAMPP's MySQL Server**
   - Open the XAMPP Control Panel.
   - Start the MySQL service.
   - Ensure it runs without errors.

---

### 5. **Access the Correct MySQL Instance**
   - Use the default `3306` port for the existing MySQL.
   - Use the `3307` port to access XAMPP's MySQL server.
   - Example command for XAMPP's MySQL server:
     ```bash
     mysql -u root -p --port=3307
     ```

---

### 6. **Verify Using phpMyAdmin**
   - Open `phpMyAdmin` in a browser via XAMPP (e.g., `http://localhost/phpmyadmin`).
   - Check the port and ensure you can connect to the XAMPP MySQL server.

---

### 7. **Optional: Disable/Stop One MySQL Server**
   If you do not need both MySQL instances running simultaneously, consider stopping or disabling one:
   - To stop the existing MySQL service:
     ```bash
     sudo service mysql stop    # For Linux
     net stop mysql             # For Windows
     ```
   - To stop XAMPP's MySQL, use the XAMPP Control Panel.

---



open xampp 
sql config > my.ini > port = 3333
config > service and port settings > mysql > port 3333
apache cofig > phpMyAdmin> config.inc.phb> `$cfg['Servers'][$i]['host'] = '127.0.0.1:3333';`

 

# connection
open cmd on location
`C:\xampp\mysql\bin`
`mysql -u root -p --port=3333`


`pip install mysql-connector-python`


# to fetch records from the database we do have following functions in the cursor 
- cursor.fetchall(): it is used to read all records
- cursor.fetchone(): to read only one record
- cursor.fetchmany(): to read with condition


write a python script for PDBC use the following methods 
- cursor.fetchone()
- cursor.fetchmany()


to update the record 
- update students set name='anvesh' where id = 101;
