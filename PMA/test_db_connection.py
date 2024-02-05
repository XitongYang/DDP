import sqlite3

try:
    conn = sqlite3.connect('/Users/yangxitong/Desktop/flask_content/mydatabase.sqlite3')
    cursor = conn.cursor()

    # 测试查询
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # 打印表名以确认连接
    for table in tables:
        print(table)

    # 关闭连接
    cursor.close()
    conn.close()
except sqlite3.Error as e:
    print(f"数据库连接失败：{e}")
