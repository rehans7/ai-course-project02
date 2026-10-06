import csv
import pandas as pd
import numpy as np

df=pd.read_csv("day02_usage.csv")
cht=df["Chat"].to_numpy()
vid=df["Video"].to_numpy()
std=df["Study"].to_numpy()
game=df["Games"].to_numpy()

chtMins=cht.sum()
vidMins=vid.sum()
stdMins=std.sum()
gameMins=game.sum()

chtAvg=cht.mean().round(2)
vidAvg=vid.mean().round(2)
stdAvg=std.mean().round(2)
gameAvg=game.mean().round(2)

stuGamDiff=std-game
print(int(stuGamDiff.argmax())+1,stuGamDiff.max())
print(int(stuGamDiff.argmin())+1,stuGamDiff.min())

maxPerDay=df.idxmax(axis=1)
print(maxPerDay)

