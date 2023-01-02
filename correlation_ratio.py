def correlation_ratio(x: list, y: list) -> float:
    array_x = np.array(x)
    array_y = np.array(y)
    class_sum = 0
    variation = ((array_x - array_x.mean()) ** 2).sum()
    for i in np.unique(array_y):
        class_sum += sum([((array_x[array_y == i] -
                           array_x[array_y == i].mean()) ** 2).sum()])
    return class_sum / variation
