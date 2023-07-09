import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results.csv")

plt.plot(df["date"], df["score"]/df["seconds_elapsed"]*60)
plt.title("Score per seconds average")
plt.grid(True)
plt.show()
