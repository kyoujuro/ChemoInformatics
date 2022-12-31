class CramersInkageCoefficient:

    def __init__(self, list_x, list_y):
        self.list_x = list_x
        self.list_y = list_y

    def _cramersV(self):
        table = np.array(pd.crosstab(self.list_x, self.list_y))
        n = table.sum()
        col_sum = table.sum(axis=0)
        row_sum = table.sum(axis=1)
        expect_value = np.outer(row_sum, col_sum) / n
        chisq = np.sum((table - expect_value) ** 2 / expect_value)
        return np.sqrt(chisq / (n * np.min(table.shape) - 1))

    def inkage_confficient(self):
        name = []
        result = []
        for column_name, item in df.iteritems():
            name.append(column_name)
            caramers_value = self._cramersV()
            result.append(caramers_value)
        df_result = pd.DataFrame({'変数': name, 'クラメールの連関係数': result})
        return df_result
