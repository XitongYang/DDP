import sqlite3

# 连接到 SQLite 数据库
conn = sqlite3.connect('/Users/yangxitong/Desktop/flask_content/mydatabase.sqlite3')
cursor = conn.cursor()

# 插入 Shops 表的数据
cursor.executemany('''
INSERT INTO Shops (Name, Address, Phonenumber, Time, Events) VALUES (?, ?, ?, ?, ?)
''', [
    ('Benugo Bar and Kitchen', 'Warwick Arts Centre', 1234567890, '10:00-19:00', 'Weekly Specials'),
    ('Cafe Library', 'Library', 1234567891, '8:00-21:00', 'Book Club Meetings'),
    ('Fusion Sports Bar', 'Rootes Building', 1234567892, '15:00-23:00', 'Live Sports Screening'),
    ('Jidong', 'Ground floor, Students\' Union Building (South)', 1234567893, '10:00-18:00', 'Student Discounts')
])

# 插入 Dishes 表的数据
cursor.executemany('''
INSERT INTO Dishes (Name, Price, Ingredient, Description, Shop_ID) VALUES (?, ?, ?, ?, ?)
''', [
    ('Grilled Chicken Salad', 10.50, 'Chicken, Lettuce, Tomato, Dressing', 'A healthy grilled chicken salad', 1),
    ('Vegan Burger', 12.00, 'Vegan Patty, Lettuce, Tomato, Vegan Bun', 'Delicious and animal-friendly', 2),
    ('Spicy Wings', 9.00, 'Chicken Wings, Hot Sauce', 'Hot and spicy chicken wings', 3),
    ('Sushi Platter', 15.00, 'Rice, Fish, Vegetables', 'Assorted sushi selection', 4),
    # 更多菜式...
])

# 插入 SpecialDiets 表的数据
cursor.executemany('''
INSERT INTO SpecialDiets (Name) VALUES (?)
''', [
    ('Vegetarian',),
    ('Vegan',),
    ('Gluten-Free',)
])

# 插入 Dish_SpecialDiets 表的数据
cursor.executemany('''
INSERT INTO Dish_SpecialDiets (Dish_ID, Diet_ID) VALUES (?, ?)
''', [
    (1, 1),  # Grilled Chicken Salad is Vegetarian
    (2, 2),  # Vegan Burger is Vegan
    # 更多关联...
])

# 插入 Allergens 表的数据
cursor.executemany('''
INSERT INTO Allergens (Name) VALUES (?)
''', [
    ('Nuts',),
    ('Dairy',),
    ('Shellfish',)
])

# 插入 Dish_Allergens 表的数据
cursor.executemany('''
INSERT INTO Dish_Allergens (Dish_ID, Allergen_ID) VALUES (?, ?)
''', [
    (2, 1),  # Vegan Burger contains Nuts
    (3, 2),  # Spicy Wings contains Dairy
    # 更多关联...
])

# 提交更改
conn.commit()

# 关闭连接
cursor.close()
conn.close()
