#https://goheels.com/sports/mens-basketball/roster

import pandas as pd
roster = ["High", "Ryan", "Davis"]
player = {"Last Name": roster}
data = pd.DataFrame(player)
print(data)