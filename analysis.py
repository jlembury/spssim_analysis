# Jessica Embury, San Diego State University, Fall 2022
# Functions for conducting the SpSSIM analysis

import pandas as pd
from util import combine_csv_files


def matrixcsv2df(csv_in, index_name):
    df = pd.read_csv(csv_in)
    df = df.set_index(index_name)
    return df


def create_weighted_matrix(df_values, df_weights):
    df = df_values.mul(df_weights)
    return df


def calc_matrix_mean(df):
    column_mean = df[list(df.columns)].mean()
    df_mean = column_mean.mean()
    return df_mean


def calc_num_df_cells(df):
    n = len(df) * len(list(df.columns))
    return n


def calc_matrix_variance(df, df_mean, n):
    temp = df.copy(deep=True)
    temp = temp.apply(lambda x: (x - df_mean) ** 2)
    temp['row_sum'] = temp.sum(axis=1)
    temp_sum = temp['row_sum'].sum()
    df_variance = temp_sum / (n - 1)
    return df_variance


def calc_covariance(df1, df2, df1_mean, df2_mean, n):
    temp1 = df1.copy(deep=True)
    temp2 = df2.copy(deep=True)

    temp1 = temp1.apply(lambda x: x - df1_mean)
    temp2 = temp2.apply(lambda x: x - df2_mean)

    temp = temp1.mul(temp2)
    temp['row_sum'] = temp.sum(axis=1)
    temp_sum = temp['row_sum'].sum()
    covariance = temp_sum / (n - 1)
    return covariance


def calc_local_spssim(matrix1_csv, matrix2_csv, weights_csv, index_name, c1, c2):
    df1 = matrixcsv2df(matrix1_csv, index_name)
    df2 = matrixcsv2df(matrix2_csv, index_name)
    w = matrixcsv2df(weights_csv, index_name)

    df1w = create_weighted_matrix(df1, w)
    df2w = create_weighted_matrix(df2, w)

    n = calc_num_df_cells(df1w)

    df1_mean = calc_matrix_mean(df1w)
    df2_mean = calc_matrix_mean(df2w)

    df1_var = calc_matrix_variance(df1w, df1_mean, n)
    df2_var = calc_matrix_variance(df2w, df2_mean, n)

    covar = calc_covariance(df1w, df2w, df1_mean, df2_mean, n)

    spssim = ((2 * df1_mean * df2_mean + c1) * (2 * covar + c2)) / (
                (df1_mean ** 2 + df2_mean ** 2 + c1) * (df1_var + df2_var + c2))
    return n, df1_mean, df2_mean, df1_var, df2_var, covar, spssim


def calc_global_spssim(matrix1_csv, matrix2_csv, weights_csv, results_tbl_csv, index_name, distance_bins, c1=0, c2=0):
    local_spssim_list = []
    results = pd.DataFrame(
        columns=['matrix1', 'matrix2', 'distance_bin', 'constant1', 'constant2', 'n', 'mean1', 'mean2', 'variance1',
                 'variance2', 'covariance', 'local_spssim'])

    for b in distance_bins:
        n, mean1, mean2, var1, var2, covar, local_spssim = calc_local_spssim(matrix1_csv, matrix2_csv,
                                                                             weights_csv.format(b[0], b[1]), index_name,
                                                                             c1, c2)
        local_spssim_list.append(local_spssim)
        tmp_result = pd.DataFrame(
            data={'matrix1': matrix1_csv[2:-4], 'matrix2': matrix2_csv[2:-4], 'distance_bin': str(b), 'constant1': c1,
                  'constant2': c2, 'n': n, 'mean1': mean1, 'mean2': mean2, 'variance1': var1, 'variance2': var2,
                  'covariance': covar, 'local_spssim': local_spssim}, index=[0])
        results = pd.concat([results, tmp_result], ignore_index=True)

    spssim = sum(local_spssim_list) / len(local_spssim_list)
    results['global_spssim'] = spssim
    results.to_csv(results_tbl_csv, index=False)
    print(matrix1_csv, matrix2_csv, spssim)
    return spssim, results


def calc_spssim_constants(results_dir_list):
    # read all results into one df
    for r in results_dir_list:
        tmp = combine_csv_files(r)
        if r == results_dir_list[0]:
            df = tmp.copy(deep=True)
        else:
            df = pd.concat([df, tmp], ignore_index=True)

    # find min local_spssim to calculate constants
    min_local = df['local_spssim'].min()
    min_index = df.index[df['local_spssim'] == min_local].tolist()
    df1_mean = df['mean1'].loc[min_index[0]]
    df2_mean = df['mean2'].loc[min_index[0]]
    df1_var = df['variance1'].loc[min_index[0]]
    df2_var = df['variance2'].loc[min_index[0]]
    covar = df['covariance'].loc[min_index[0]]

    # find constants c1 and c2 such that least similar index score = 0
    # spssim = ((2 * df1_mean * df2_mean + c1) * (2 * covar + c2)) / (df1_mean ** 2 + df2_mean ** 2 + c1) * (df1_var + df2_var + c2))
    c1a = -1 * (2 * df1_mean * df2_mean)
    c1b = -1 * (df1_mean ** 2 + df2_mean ** 2)
    c1 = max(c1a, c1b)

    c2a = -1 * (2 * covar)
    c2b = -1 * (df1_var + df2_var)
    c2 = max(c2a, c2b)
    return c1, c2, df1_mean, df1_var, df2_mean, df2_var, covar
