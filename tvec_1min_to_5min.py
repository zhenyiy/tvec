import pandas as pd
import os

if __name__ == '__main__':
    output_dir = 'data/output'
    data_1min_dir = 'data/tmp_1min'
    data_5min_dir = 'data/tmp_5min'
    file_name = 'IYR.csv'

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    data_1min = pd.read_csv(data_1min_dir + '/' + file_name, sep=',')
    data_5min = pd.read_csv(data_5min_dir + '/' + file_name, sep=',')

    row_num_5min = len(data_5min.iloc[:, 0])
    row_num_1min = len(data_1min.iloc[:, 0])
    arr = data_1min.iloc[:, 0]
    date = data_5min.iloc[:, 0][0]
    frst_match_data_1min = data_1min[arr == date].index
    step = 5
    data_1min_sm = data_1min[
        (data_1min.index >= frst_match_data_1min.to_list()) & ((data_1min.index - frst_match_data_1min) % step == 0)]
    data_5min.iloc[:, 1] = data_1min_sm.iloc[:, 1].values

    data_5min.to_csv(output_dir + '/' + file_name, index=False)
    print("Done")
