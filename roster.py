#https://goheels.com/sports/mens-basketball/roster

import pandas as pd
roster = ["High", "Ryan", "Davis"]
player = {"Last Name": roster,
          "First Name": ["Zayden", "Cormac","RJ"],
          "height": [81, 77, 72],
          "weight": [225, 195, 180]}
data = pd.DataFrame(player)
print(data)