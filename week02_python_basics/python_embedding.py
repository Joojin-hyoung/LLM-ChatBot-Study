import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

import matplotlib.pyplot as plt

plt.rc('font', family='NaumBarunGothic')

words = ['사과', '배', '포도', '강아지', '고양이', '말', '자동차', '비행기']
coords = np.array([
    [1.0, 2.0],
    [1.2, 2.1],
    [0.9, 1.8],
    [3.0, 3.5],
    [3.2, 3.7],
    [2.8, 3.6],
    [5.0, 1.0],
    [5.2, 1.2]
    ])

plt.figure(figsize=(7,6))
plt.scatter(coords[:,0], coords[:,1], c="blue")

for word, (x,y) in zip(words, coords):
    plt.text(x+0.05, y+0.05, word, fontsize=12)

plt.title("단어 임베딩 벡터 공간 예시", fontsize = 14)
plt.xlabel("차원 1")
plt.ylabel("차원 2")
plt.grid(True, linestyle="--", alpha = 0.5)
plt.show()