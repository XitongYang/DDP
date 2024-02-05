import sqlite3

conn = sqlite3.connect('/Users/yangxitong/Desktop/flask_content/mydatabase.sqlite3')
cursor = conn.cursor()

# 创建 Shops 表
cursor.execute('''
CREATE TABLE Shops (
    Shop_ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Address TEXT,
    Phonenumber INTEGER,
    Time TEXT,
    Events TEXT
)
''')

# 创建 Dishes 表
cursor.execute('''
CREATE TABLE Dishes (
    Dish_ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Price FLOAT,
    Ingredient TEXT,
    Description TEXT,
    Shop_ID INTEGER,
    FOREIGN KEY (Shop_ID) REFERENCES Shops(Shop_ID)
)
''')

# 创建 SpecialDiets 表
cursor.execute('''
CREATE TABLE SpecialDiets (
    Diet_ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
)
''')

try:
    cursor.execute('ALTER TABLE Dishes ADD COLUMN Calories INT')
    conn.commit()
    print("Calories column added successfully to the Dishes table.")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")

# 创建 Dish_SpecialDiets 表
cursor.execute('''
CREATE TABLE Dish_SpecialDiets (
    Dish_ID INTEGER,
    Diet_ID INTEGER,
    FOREIGN KEY (Dish_ID) REFERENCES Dishes(Dish_ID),
    FOREIGN KEY (Diet_ID) REFERENCES SpecialDiets(Diet_ID)
)
''')

# 创建 Allergens 表
cursor.execute('''
CREATE TABLE Allergens (
    Allergen_ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
)
''')

# 创建 Dish_Allergens 表
cursor.execute('''
CREATE TABLE Dish_Allergens (
    Dish_ID INTEGER,
    Allergen_ID INTEGER,
    FOREIGN KEY (Dish_ID) REFERENCES Dishes(Dish_ID),
    FOREIGN KEY (Allergen_ID) REFERENCES Allergens(Allergen_ID)
)
''')

# 提交更改
conn.commit()

# 关闭连接
cursor.close()
conn.close()

