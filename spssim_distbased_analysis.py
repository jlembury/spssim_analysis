# Jessica Embury, San Diego State University, Fall 2022
# Functions for conducting the distance-based SpSSIM analysis

import pandas as pd
from statistics import mean
from util import combine_csv_files
from matrixes import *


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


def calc_distbased_spssim(matrix1_csv, matrix2_csv, weights_csv, index_name, c1, c2):
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

    spssim = ((2 * df1_mean * df2_mean + c1) * (2 * covar + c2)) / ((df1_mean ** 2 + df2_mean ** 2 + c1) * (df1_var + df2_var + c2)) if ((df1_mean ** 2 + df2_mean ** 2 + c1) * (df1_var + df2_var + c2)) != 0 else 0

    return n, df1_mean, df2_mean, df1_var, df2_var, covar, spssim


def calc_global_distbased_spssim(matrix1_csv, matrix2_csv, weights_csv, results_tbl_csv, index_name, distance_bins, c1=0, c2=0):
    distbased_spssim_list = []
    results = pd.DataFrame(
        columns=['matrix1', 'matrix2', 'distance_bin', 'constant1', 'constant2', 'n', 'mean1', 'mean2', 'variance1',
                 'variance2', 'covariance', 'distbased_spssim'])

    for b in distance_bins:
        n, mean1, mean2, var1, var2, covar, distbased_spssim = calc_distbased_spssim(matrix1_csv, matrix2_csv,
                                                                                     weights_csv.format(b[0], b[1]),
                                                                                     index_name, c1, c2)
        distbased_spssim_list.append(distbased_spssim)
        print(distbased_spssim_list)
        tmp_result = pd.DataFrame(
            data={'matrix1': matrix1_csv[2:-4], 'matrix2': matrix2_csv[2:-4], 'distance_bin': str(b), 'constant1': c1,
                  'constant2': c2, 'n': n, 'mean1': mean1, 'mean2': mean2, 'variance1': var1, 'variance2': var2,
                  'covariance': covar, 'distbased_spssim': distbased_spssim}, index=[0])
        results = pd.concat([results, tmp_result], ignore_index=True)

    spssim = sum(distbased_spssim_list) / len(distbased_spssim_list)
    results['global_spssim'] = spssim
    results.to_csv(results_tbl_csv, index=False)
    print(matrix1_csv, matrix2_csv, spssim)
    return spssim, results


def calc_distbased_spssim_constants(results_dir_list):
    # read all results into one df
    for r in results_dir_list:
        tmp = combine_csv_files(r)
        if r == results_dir_list[0]:
            df = tmp.copy(deep=True)
        else:
            df = pd.concat([df, tmp], ignore_index=True)

    # find min distbased_spssim to calculate constants
    min_distbased = df['distbased_spssim'].min()
    print('Minimum distbased SpSSIM = {}'.format(min_distbased))

    min_index = df.index[df['distbased_spssim'] == min_distbased].tolist()
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
    spssim = ((2 * df1_mean * df2_mean + c1) * (2 * covar + c2)) / ((df1_mean ** 2 + df2_mean ** 2 + c1) * (df1_var + df2_var + c2))
    print('Updated minimum distbased SpSSIM = {}'.format(spssim))

    return c1, c2


def calc_distbased_results_summaries(results_dir, global_summary_csv, distbased_summary_csv):
    df = combine_csv_files(results_dir)
    df = df.query('global_spssim != 1')

    # global summary
    global_df = df[['global_spssim', 'matrix_pair']].drop_duplicates()
    global_df = global_df.sort_values(by=['global_spssim'])
    global_df.to_csv(global_summary_csv)

    # distbased summary by distance bin
    dist_bins = df['distance_bin'].unique()
    distbased_df = pd.DataFrame(columns=['distance_bin', 'mean_distbased_spssim', 'min_distbased_spssim', 'min_matrix_pair', 'max_distbased_spssim', 'max_matrix_pair', 'distbased_spssim_list', 'matrix_pairs'])
    for d in dist_bins:
        tmp1 = df.query('distance_bin == @d')
        list_spssim = list(tmp1['distbased_spssim'])
        list_mats = list(tmp1['matrix_pair'])
        l = [[list_spssim[i], list_mats[i]] for i in range(len(tmp1))]
        l.sort()

        tmp2 = pd.DataFrame(data={'distance_bin': d, 'mean_distbased_spssim': mean(list_spssim), 'min_distbased_spssim': l[0][0], 'min_matrix_pair': l[0][1], 'max_distbased_spssim': l[-1][0], 'max_matrix_pair': l[-1][1], 'distbased_spssim_list': [[l[i][0] for i in range(len(l))]], 'matrix_pairs': [[l[i][1] for i in range(len(l))]]})
        distbased_df = pd.concat([distbased_df, tmp2], ignore_index=True)
    distbased_df.to_csv(distbased_summary_csv)

    return global_df, distbased_df
