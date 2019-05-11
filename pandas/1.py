import pandas

df1 = pandas.DataFrame([[2,4,6], [10,20,30]], columns=["col1", "col2", "col3"], index=["row1", "row2"])
print df1

df2 = pandas.DataFrame([{"ColName":"Bill", "Surname":"Williams"}, {"ColName":"John"}])
print df2

print type(df1)
print dir(df1)

print df1.mean()
print type(df1.mean())

print df1.mean().mean()
print type(df1.mean().mean())

print df1.col1