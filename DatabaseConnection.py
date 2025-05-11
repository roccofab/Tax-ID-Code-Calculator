import os
import pymysql
class DatabaseConnection:
    def __init__(self):
        self.connection = pymysql.connect(
            user = os.getenv("DB_USERNAME"),
            password = os.getenv("DB_PASSWORD"),
            host = "localhost",
            database = "tax_id_code"
        )
        self.cursor = self.connection.cursor()
        
    def insert_tax_code(self,name,surname,birth_date,gender,municipality_code,tax_code):
        """
        Insert the tax code into the table tax_code of the database tax_ID_code.
        
        Args:
            name (str): Name of the person.
            surname (str): Surname of the person.
            birth_date (str): Birth date of the person(gg-mm-yyyy).
            gender (str): Gender of the person(M/F).
            municipality_code (str): Municipality code.
            ta_code (str): Tax code to be inserted.
        """
        try:
            query = """
            INSERT INTO tax_code(name,surname,birth_date,gender,municipality_code,tax_code)
            VALUES(%s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (name,surname,birth_date, gender, municipality_code,tax_code))
            self.connection.commit()
            print("Tax code inserted successfully.")
        except pymysql.Error as e:
            print("Error: ", str(e))
        finally:
            self.cursor.close()
            self.connection.close()