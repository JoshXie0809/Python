def LoadData(path, ColumnUChoose = None):
    import pandas as pd

    df = pd.read_csv(path)
    if ColumnUChoose is not None:
        data = df[ColumnUChoose].copy()
    else:
        data = df.copy()
    return data
