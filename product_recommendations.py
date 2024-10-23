import joblib
product_recommendations = {
    0: ['L Oreal', 'MAC', 'Vaseline','Softsoap','Nivea','Gold Bond','Aveeno'],
    1: ['The Bible', 'Harry Potter Series', 'The Lord of the Rings','The Twilight Saga','Think and Grow Rich'],
    2: ['Levis', 'Louis Phillippe', 'Nike','Armani','Gucci','Pepe Jeans','Aime Leon Dore','Allen Solly','Gap','Peter England'],
    3: ['phone', 'bluetooth', 'watches','charger','calculator','laptop','Xbox','mouse','pendrive','headset'],
    4: ['pizza', 'burger', 'biryani','friedrice','chocalates','sweets','cooldrinks','vegetables','dryfruits','seafoods','groceries'],
    5: ['BP MONITORS', 'Glucometers', 'massagers','mass gainers','fat burners','weighting scales','vitamins & supplements','Healthcare packages','Ayurvedic supplements'],
    6: ['washing machine', 'AC', 'Cooler','fridge','beds','lights','mats','blankets','fans','TV','mixer','Grinder','stove','pan']
}

joblib.dump(product_recommendations, 'product_recommendations.pkl')