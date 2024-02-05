import sqlite3

try:
    conn = sqlite3.connect('/Users/yangxitong/Desktop/flask_content/mydatabase.sqlite3')
    cursor = conn.cursor()

    # 向 Dishes 表添加 Calorie 列
    cursor.execute('ALTER TABLE Dishes ADD COLUMN Calorie INT')

    # 提交更改
    conn.commit()
    print("Calorie column added successfully to the Dishes table.")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    # 关闭连接
    cursor.close()
    conn.close()
