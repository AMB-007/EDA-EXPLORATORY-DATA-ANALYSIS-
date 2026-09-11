import pandas as pd

# pd.Series(data)
# data -> list/dictionary/tuple
data = [ 1,3,5,2,6,7]
series_1 = pd.Series(data)
print(series_1)

# creating the new series using dictionary
# ========================
# data = {"a":20,"b":30,"c":40,"d":50,"e":60,"f":70,"g":80,"h":90,"i":100}
# result = pd.Series(data)
# print(result.ndim)
# print(result.index)
# print(result.shape)
# print(result.dtype)
# print(result.head(3))
# extract first few values from the series given
# print(result.tail())
# extract last few vales from the series given


s_1 =pd.series([1,2,3,4,5,6,7])
s_2 = pd.series([8,9,10,11,12,13,14])
print(s_1.add(s_2))
print(s_1.multiply(s_2))
print(pd.concat([s_1,s_2]))
