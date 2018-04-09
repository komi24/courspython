import pandas as pd
data = {"state": ["Ohio", "Ohio", "Ohio",
"Nevada", "Nevada"],
"year": [2000, 2001, 2002, 2001, 2002],
"pop": [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = pd.DataFrame(data)
# ordre des colonnes
pd.DataFrame(data, columns=["year", "state", "pop"])
# index des lignes et valeurs manquantes (NaN)
frame2=pd.DataFrame(data, columns=["year", "state",
"pop", "debt"],
index=["one", "two", "three", "four", "five"])
# liste des colonnes
frame.columns
# valeurs d’une colonnes
frame["state"]
frame.year
# "imputation"
frame2["debt"] = 16.5
frame2
# créer une variable
frame2["eastern"] = frame2.state == "Ohio"
frame2
# supprimer une variable
del frame2[u"eastern"]
frame2.columns

# importation
import pandas as pd
data=pd.read_csv("fichier.csv")
# ou encore de façon équivalente
data=pd.read_table("fichier.csv", sep=",", header=0, index_col='ID_Device')

converters={'date':pd.to_datetime}


data = pd.DataFrame({"food":["bacon","pulled pork",
"bacon", "Pastrami",
"corned beef", "Bacon", "pastrami", "honey ham",
"nova lox"],
"ounces": [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

meat_to_animal = {
"bacon": "pig",
"pulled pork": "pig",
"pastrami": "cow",
"corned beef": "cow",
"honey ham": "pig",
"nova lox": "salmon"
}
data["animal"] = data["food"].map(
str.lower).map(meat_to_animal)

# la table de données
frame = pd.DataFrame(np.random.randn(4,3),
columns=list("bde"),
index=["Utah", "Ohio", "Texas", "Oregon"])
# une fonction
f = lambda x: x.max() - x.min()
frame.apply(f, axis=1)


dfs = pd.DataFrame(np.arange(5 * 4).reshape(5, 4))
sampler = np.random.permutation(5)
sampler
dfs
dfs.take(sampler)


frame = pd.DataFrame(np.arange(8).reshape((2,4)),
index=["three", "one"],
columns=["d", "a", "b", "c"])
frame.sort_index()
frame.sort_index(axis=1)
frame.sort_index(axis=1, ascending=False)
frame.sort_index(by="b")
frame.sort_index(by=["a", "b"])

frame = pd.DataFrame({"b": [4.3, 7, -3, 2],
"a": [0, 1, 0, 1],"c": [-2, 5, 8, -2.5]})
frame.rank(axis=1)
frame.rank(axis=0)

# tables
df1 = pd.DataFrame({"key": ["b", "b", "a", "c","a","a", "b"],"data1": range(7)})
df2 = pd.DataFrame({"key": ["a", "b", "d"],
"data2": range(3)})
pd.merge(df1,df2,on="key")
pd.merge(df1,df2,on="key", how="outer")