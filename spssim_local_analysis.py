# Jessica Embury, San Diego State University, Fall 2022
# Functions for conducting the local SpSSIM analysis

import pandas as pd
import numpy as np
from util import *
from matrixes import *
import warnings
warnings.filterwarnings('ignore')


def calc_local_spssim_singlebin(dfw1, dfw2, spssim_csv, distance_bin, c1, c2):
    # n, mean, var
    dfw1.loc['n'] = dfw1.count()
    dfw1.loc['mean1'] = dfw1[0:-1].mean()
    dfw1.loc['var1'] = dfw1[0:-2].var()

    dfw2.loc['mean2'] = dfw2.mean()
    dfw2.loc['var2'] = dfw2[0:-1].var()

    # prep for covar
    cov1 = dfw1
    cov1 = cov1 - cov1.loc['mean1']
    cov1 = cov1[0:-3]

    cov2 = dfw2
    cov2 = cov2 - cov2.loc['mean2']
    cov2 = cov2[0:-2]

    # COVARIANCE
    cov = pd.DataFrame(data=None, columns=cov1.columns, index=cov1.index)
    cov = cov1.mul(cov2)
    cov.loc['cov'] = cov.sum()/(cov.count() - 1)

    # calculate spssim
    spssim = pd.concat([dfw1.tail(3), dfw2.tail(2), cov.tail(1)])
    spssim.loc['distance_bin'] = str(distance_bin)
    spssim.loc['c1'] = c1
    spssim.loc['c2'] = c2
    spssim.loc['bin_local'] = ((2 * spssim.loc['mean1'] * spssim.loc['mean2'] + c1) * (2 * spssim.loc['cov'] + c2)) / ((spssim.loc['mean1'] ** 2 + spssim.loc['mean2'] ** 2 + c1) * (spssim.loc['var1'] + spssim.loc['var2'] + c2)).replace(0, np.nan)

    # transpose df
    spssim = spssim.transpose()
    spssim = spssim[['distance_bin', 'n', 'mean1', 'mean2', 'var1', 'var2', 'cov', 'c1', 'c2', 'bin_local']]
    spssim.to_csv(spssim_csv.format(distance_bin[0], distance_bin[1]))
    return spssim


def calc_local_spssim(probability_matrix_csv1, probability_matrix_csv2, weights_csv, spssim_bin_csv, spssim_local_csv, distance_bins, index_name, c1=0, c2=0):
    print(probability_matrix_csv1, probability_matrix_csv2)
    df = pd.DataFrame(columns=[index_name, 'distance_bin', 'n', 'mean1', 'mean2', 'var1', 'var2', 'covar', 'c1', 'c2', 'bin_local'])
    df1 = matrixcsv2df(probability_matrix_csv1, index_name)
    df2 = matrixcsv2df(probability_matrix_csv2, index_name)

    for b in distance_bins:
        print(b)
        w = matrixcsv2df(weights_csv.format(b[0], b[1]), index_name)
        dfw1 = pd.DataFrame(df1.values*w.values, columns=df1.columns, index=df1.index)
        dfw2 = pd.DataFrame(df2.values*w.values, columns=df2.columns, index=df2.index)
        dfs = calc_local_spssim_singlebin(dfw1, dfw2, spssim_bin_csv, b, c1, c2).reset_index()
        dfs = dfs.rename(columns={'index':index_name})
        df = pd.concat([df, dfs])

    df = df.rename(columns={index_name:'cbg'})
    dfpiv = df.pivot(index='cbg', columns='distance_bin', values='bin_local')
    print(len(df), len(dfpiv))
    # calculate local spssims
    dfpiv['local_spssim'] = dfpiv.mean(axis=1)
    dfpiv['count'] = dfpiv.count(axis='columns')
    dfpiv['count'] = dfpiv['count'].replace(-1, 0)
    dfpiv = dfpiv.sort_values('count')
    pivot_cols = []
    for b in distance_bins:
        pivot_cols.append(str(b))
    pivot_cols.extend(['local_spssim', 'count'])
    dfpiv = dfpiv[pivot_cols]  # reorder columns
    dfpiv = dfpiv.sort_index()
    dfpiv.to_csv(spssim_local_csv)

    return dfpiv


def calc_local_constants(results_dir_list):
    # read all results into one df
    for r in results_dir_list:
        tmp = combine_csv_files(r)
        if r == results_dir_list[0]:
            df = tmp.copy(deep=True)
        else:
            df = pd.concat([df, tmp], ignore_index=True)

    # find min local spssim to calculate constants
    min_local = df['bin_local'].min()
    print('Minimum local/bin SpSSIM = {}'.format(min_local))

    min_index = df.index[df['bin_local'] == min_local].tolist()
    df1_mean = df['mean1'].loc[min_index[0]]
    df2_mean = df['mean2'].loc[min_index[0]]
    df1_var = df['var1'].loc[min_index[0]]
    df2_var = df['var2'].loc[min_index[0]]
    covar = df['cov'].loc[min_index[0]]

    # find constants c1 and c2 such that least similar index score = 0
    # spssim = ((2 * df1_mean * df2_mean + c1) * (2 * covar + c2)) / (df1_mean ** 2 + df2_mean ** 2 + c1) * (df1_var + df2_var + c2))
    c1a = -1 * (2 * df1_mean * df2_mean)
    c1b = -1 * (df1_mean ** 2 + df2_mean ** 2)
    c1 = max(c1a, c1b)
    if c1 < 0:
        c1 = 0

    c2a = -1 * (2 * covar)
    c2b = -1 * (df1_var + df2_var)
    c2 = max(c2a, c2b)
    if c2 < 0:
        c2 = 0

    spssim = ((2 * df1_mean * df2_mean + c1) * (2 * covar + c2)) / ((df1_mean ** 2 + df2_mean ** 2 + c1) * (df1_var + df2_var + c2))
    print('Updated minimum local SpSSIM = {}'.format(spssim))

    return c1, c2
