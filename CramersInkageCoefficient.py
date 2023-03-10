import numpy as np

class CramersInkageCoefficient(object):
    """
    クラメールの連関係数を計算する。

    Attribute
    ----------
    list_x : list
        １つ目の変数のリスト。
    list_y : list
        2つ目の変数のリスト。
    """

    def __init__(self, list_x, list_y):
        self._list_x = list_x
        self._list_y = list_y
        if isinstance(list_x, list) and isinstance(list_y, list):
            pass
        elif not isinstance(list_x, list):
            raise ValueError(f'引数{list_x}はlist型ではありません。')
        else:
            raise ValueError(f'引数{list_y}はlist型ではありません。')

    def _cramersV(self):
        """
        Returns
        -------
        np.sqrt(chisq / (n * np.min(table.shape) - 1)) : float
        クラメールの連関係数。
        """
        table = np.array(pd.crosstab(self._list_x, self._list_y))
        n = table.sum()
        col_sum = table.sum(axis=0)
        row_sum = table.sum(axis=1)
        expect_value = np.outer(row_sum, col_sum) / n
        chisq = np.sum((table - expect_value) ** 2 / expect_value)
        return np.sqrt(chisq / (n * (np.min(table.shape) - 1)))

    def inkage_confficient(self):
        name = []
        result = []
        for column_name, item in df.iteritems():
            name.append(column_name)
            caramers_value = self._cramersV()
            result.append(caramers_value)
        df_result = pd.DataFrame({'変数': name, 'クラメールの連関係数': result})
        return df_result
