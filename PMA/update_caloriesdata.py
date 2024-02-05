import sqlite3

# 假设的菜品和它们的卡路里数值
dish_calories = {
    'Grilled Chicken Salad': 350,
    'Vegan Burger': 500,
    'Spicy Wings': 600,
    'Sushi Platter': 450,
    # ... 为其他菜品也添加卡路里数值
}

try:
    conn = sqlite3.connect('/Users/yangxitong/Desktop/flask_content/mydatabase.sqlite3')
    cursor = conn.cursor()

    # 为每个菜品更新卡路里数值
    for dish_name, calories in dish_calories.items():
        cursor.execute('''
            UPDATE Dishes
            SET Calorie = ?
            WHERE Name = ?''', (calories, dish_name))

    # 提交更改
    conn.commit()
    print("Calorie data updated successfully in the Dishes table.")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
finally:
    # 关闭连接
    cursor.close()
    conn.close()
