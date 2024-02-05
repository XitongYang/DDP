from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return("Hello, World!")


@app.route('/search_dishes', methods=['POST'])
def search_dishes():
    data = request.json
    allergen = data['allergen']

    # Connect database
    conn = sqlite3.connect('/Users/yangxitong/Desktop/flask_content/mydatabase.sqlite3')
    cursor = conn.cursor()

    # 查询不含特定过敏源的菜品
    query = '''
    SELECT Dishes.Name, Dishes.Description
    FROM Dishes
    LEFT JOIN Dish_Allergens ON Dishes.Dish_ID = Dish_Allergens.Dish_ID
    LEFT JOIN Allergens ON Dish_Allergens.Allergen_ID = Allergens.Allergen_ID
    WHERE Allergens.Name IS NULL OR Allergens.Name != ?
    '''

    cursor.execute(query, (allergen,))
    dishes = cursor.fetchall()

    cursor.close()
    conn.close()

    # return to the result
    response_data = {'dishes': dishes}
    return jsonify(response_data)

@app.route('/get-food-categories')
def get_food_categories():
    conn = sqlite3.connect('/Users/yangxitong/Desktop/flask_content/mydatabase.sqlite3')
    cursor = conn.cursor()

    cursor.execute("SELECT Dish_ID, Name, Calorie FROM Dishes")
    categories = [{"id": row[0], "name": row[1], "calories": row[2]} for row in cursor.fetchall()]

    cursor.close()
    conn.close()

    return jsonify(categories)

if __name__ == '__main__':
    app.run(debug=True)
