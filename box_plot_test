import matplotlib.pyplot as plt
import numpy as np
import japanize_matplotlib
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(9, 4))

np.random.seed(123)
all_data = [np.random.normal(0, std, 100) for std in range(6, 10)]
axs.boxplot(all_data)
axs.set_title('クラスごとの成績の箱ひげ図')
axs.yaxis.grid(True)
axs.set_xticks([y + 1 for y in range(len(all_data))],
               labels=['クラスA', 'クラスB', 'クラス C', 'クラスD'])
axs.set_xlabel('各クラス')
axs.set_ylabel('点数')

plt.show()
