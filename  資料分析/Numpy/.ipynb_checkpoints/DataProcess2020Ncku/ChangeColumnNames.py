def ChangeColumnNames(data):
    import pandas as pd

    colnames = data.columns
    newcolumnlist = []
    for colname in colnames:
        try:
            new_colname = input(colname + '\t changes to :(  or a enter to skip  )')
            if new_colname == '':
                newcolumnlist.append(colname)
            else:
                newcolumnlist.append(new_colname)
        except:
            print('error at  ' + colname)
    print(newcolumnlist)

    newdi = dict(zip(colnames, newcolumnlist))
    data = data.rename(columns=newdi)
    return data
