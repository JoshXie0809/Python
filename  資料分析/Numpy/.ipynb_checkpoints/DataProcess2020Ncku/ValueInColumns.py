def ValueInColumns(data):
    colnames = data.columns
    for colname in colnames:
        print(data[colname].value_counts().index)

