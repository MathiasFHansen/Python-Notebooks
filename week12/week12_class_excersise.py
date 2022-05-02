# import all necessary libs
from locale import D_FMT
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

df = pd.read_csv("dronning.csv", index_col=0)

wordcloud = WordCloud().generate(df)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()