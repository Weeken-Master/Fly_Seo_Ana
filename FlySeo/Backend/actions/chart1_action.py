# Connect to DB
# Query and return result
import sqlite3
import pymysql
from ..models import chart1_model
class Chart1Action:

    def __init__(self, db_connection) -> None:
        self.db_connection = db_connection

    def get_all(self):
        conn = self.db_connection
        cursor = conn.cursor()
        # sau này giới hạn phân page
        sql = 'SELECT * FROM chart1'
        cursor.execute(sql)
        rows = cursor.fetchall()
        result = []
        for row in rows:
            chart1 = chart1_model.Chart1(
                ID = row[0],
                Product=row[1],
                Price=row[2],
               
            )
            result.append(chart1.serialize())
        return result

    def get_by_id(self, id):
        conn = self.db_connection
        cursor = conn.cursor()
        sql = """
            SELECT * FROM chart1 WHERE ID = %s
        """
        #dạng toppge truyền tham số
        #(a,b,c)

        cursor.execute(sql, (id, ))
        #id duy nhất fetchone
        row = cursor.fetchone();
        result = []
        print(row)
        if row == None:
            # ko có id truyền vào = vs id  bảng chart1
            
            return  " Not Found",404
        chart1 = chart1_model.Chart1(
            ID= row[0],
            Product=row[1],
            Price=row[2],
        )
        result.append(chart1.serialize())
        return result,200

    def add(self, chart1: chart1_model.Chart1):
     
        conn = self.db_connection
        cursor = conn.cursor()
        result=[];
        sql = """
                INSERT INTO chart1(Product,Price) VALUES(%s, %s)
                """
        cursor.execute(sql, (chart1.Product,(chart1.Price)))
        conn.commit()
        return "Insert:Success!",200
    def delete(self, chart1: chart1_model.Chart1):
        conn = self.db_connection
        cursor = conn.cursor();
        sql = """
            DELETE  FROM chart1 WHERE ID = %s
            """
        cursor.execute(sql,(chart1.ID,))
        conn.commit()
          # số dòng bị tác động
        count = cursor.rowcount
        if count == 0:
            return 'Customer not found',404
        return  'Deleted successfully', 200
    def update(self, id: int, chart1: chart1_model.Chart1):
        conn = self.db_connection
        cursor = conn.cursor()
        sql = """
            UPDATE chart1
            SET Product = %s, Price = %s
            WHERE ID = %s
        """
        cursor.execute(sql, (chart1.Product,chart1.Product, id))
        conn.commit()
        n = cursor.rowcount
        if n == 0:
            return 'Customer not found', 404
        return 'Updated successfully', 200