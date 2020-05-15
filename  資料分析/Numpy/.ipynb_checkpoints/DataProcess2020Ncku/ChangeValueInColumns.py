def ChangeValueInColumns(data):
    import pandas as pd
    from IPython.display import clear_output  ############################################
    import time
    colnames = data.columns
    for colname in colnames:
        time.sleep(0.3)
        clear_output()  ############################################
        print(data[colname].value_counts().index)

        values = data[colname].value_counts().index
        choice = input('press aa to change other to skip :')

        if choice == 'aa':
            print('\n\n\n')

            default_values = dict(zip(list(values), list(values)))
            clean = 1
            while True:
                clean += 1
                if clean % 2 == 0:
                    time.sleep(0.4)
                    clear_output()  ############################################
                count = 1
                value1 = ''
                for value in default_values.values():
                    print("'" + value + "'", end=', ')
                    try:
                        if len(value.split(' ')) > 1:
                            if count == 1:
                                value1 = value
                                count += 1

                    except:
                        print(value + ' is error')

                WantToChange = input('What value do U want to change :\n(q1) to Exit \n(aa)' + value1 + '\n input:')
                if WantToChange == 'aa':
                    WantToChange = value1
                if WantToChange in default_values.keys():
                    ChangeValue = input('New Value : \n(a1) ' + value1.split(' ')[0]
                                        + '\n(a11) NaN' + '\n input:')
                    if ChangeValue == 'a1':
                        ChangeValue = value1.split(' ')[0]
                    if ChangeValue == 'a11':
                        ChangeValue = 'NaN'

                    default_values[WantToChange] = ChangeValue

                elif WantToChange == 'q1':
                    break

                else:
                    print('not in values!!!!!!!!!!!!!!!!!!!!!!')

                print('-' * 50)

            data[colname] = data[colname].replace(default_values)

        #             for value in values:
        #                 new_value = input(value + '\t\tchange to :(  or enter to skip)')
        #                 if new_value == '':
        #                     new_value_list.append(value)
        #                 else:
        #                     new_value_list.append(new_value)
        #             data[colname].replace(dict(zip(values, new_value_list)))

        print('\n\n', '-' * 50)
    return data