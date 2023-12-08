#https://goheels.com/sports/mens-basketball/roster

import pandas as pd
player = {"Last Name": ["High", "Ryan", "Davis", "Cadeau","Bacot", "Trimble", "Wojcik", "Washington", "Lebo", "Landry", "Withers", "Okonkwo","Farris", "Ingram"],
          "First Name": ["Zayden", "Cormac","RJ","Elliot", "Armando", "Seth", "Paxson","Jalen", "Creighton", "Rob", "Jae'Lyn","James","Duwe","Harrison"],
          "height": [81, 77, 72, 73, 83, 75, 77, 82,73,76,81,80,79,79],
          "weight": [225, 195, 180, 180, 240, 195, 195, 230, 180, 190,215,240,210,235]}
data = pd.DataFrame(player)

data["bmi"] = (data ["weight"]/2.205/(data["height"]/39.37)**2)

data["bmi"] = data["bmi"].round(2)

print(data)

data.to_csv("bmi.csv")