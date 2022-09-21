# Jessica Embury, San Diego State University, Fall 2022
# Functions related to the creation of flow matrixes for the SpSSIM analysis

import pandas as pd
import geopandas as gpd
import numpy as np
from util import Diff


def odtable2matrix(csv_in, csv_out, index_name, columns_name, values_name):
    df = pd.read_csv(csv_in)
    print('{}\nO-D table has {} rows.'.format(csv_in, len(df)))

    # pivot od table to create od matrix
    df_pivot = df.pivot(index=index_name, columns=columns_name, values=values_name)
    df_pivot = df_pivot.fillna(0)

    # drop cbg if exists (coastline water only)
    try:
        df_pivot = df_pivot.drop([60739901000], axis=0)
        df_pivot = df_pivot.drop([60739901000], axis=1)
    except:
        pass

    # check for differences between rows and columns
    rows = list(df_pivot.index.values)
    cols = list(df_pivot.columns)
    diff = Diff(rows, cols)
    print('Pivot table has {} rows and {} columns. {} differences: {}'.format(len(rows), len(cols), len(diff), diff))

    df_pivot.to_csv(csv_out)
    return df_pivot


def create_distbased_probability_matrix(csv_in, csv_out, index_name, exclude_within_flow=True):
    # sum all row values
    df = pd.read_csv(csv_in)
    df[index_name] = df[index_name].astype(str)
    df = df.set_index(index_name)

    if exclude_within_flow:
        within_flow = df.index.values[:, None] == df.columns.values
        df = pd.DataFrame(np.select([within_flow], [0], df.values), columns=df.columns, index=df.index)

    df['row_total'] = df.sum(axis=1)

    # get flow probabilities
    cols = list(df.columns)
    cols.remove('row_total')
    df_probs = df[cols].div(df.row_total, axis=0)
    print('Raw matrix has {} rows. Probabilities matrix has {} rows.'.format(len(df), len(df_probs)))
    df_probs.to_csv(csv_out)

    # check that probabilities for each cbg have a sum=1
    df_probs['row_total'] = df_probs.sum(axis=1)
    print(df_probs.row_total.unique())

    return df_probs


def create_local_probability_matrix(csv_in, csv_out, index_name,  inflow=True, exclude_within_flow=True):
    # INFLOWS = Calculations down columns
    # OUTFLOWS = Calculations across rows --> Transpose to calculate down columns

    # raw matrix
    df = pd.read_csv(csv_in)
    df[index_name] = df[index_name].astype(str)
    df = df.set_index(index_name)

    # change within flow values to None
    if exclude_within_flow:
        within_flow = df.index.values[:, None] == df.columns.values
        df = pd.DataFrame(np.select([within_flow], [np.nan], df.values), columns=df.columns, index=df.index)

    # if outflow (inflow=False), transpose the df
    if inflow==False:
        df = df.transpose()

    # get flow probabilities
    df.loc['total'] = df.sum()
    df.loc['total'] = df.loc['total'].replace(0, np.nan)
    probs = df[:-1].div(df.loc['total']).replace(np.inf, np.nan)
    probs.to_csv(csv_out)

    # check that probabilities for each cbg have a sum=1 (or 0 if no flow to/from the CBG)
    probs.loc['total'] = probs.sum()
    print(probs.loc['total'].unique())

    return probs[:-1]


def create_distance_matrix(shp_in, cbg_check_csv, csv_out):
    gdf = gpd.read_file(shp_in)

    gdf1 = gdf[['geoid', 'geometry']]
    gdf1 = gdf1.rename(columns={'geoid': 'orig_geoid', 'geometry': 'orig_geometry'})
    gdf1 = gdf1.sort_values(by='orig_geoid')

    gdf2 = gdf[['geoid', 'geometry']]
    gdf2 = gdf2.rename(columns={'geoid': 'dest_geoid', 'geometry': 'dest_geometry'})
    gdf2 = gdf2.sort_values(by='dest_geoid')

    cross = gdf1.merge(gdf2, how='cross')
    geom1 = gpd.GeoSeries(list(cross['orig_geometry']))
    geom2 = gpd.GeoSeries(list(cross['dest_geometry']))
    distances = geom1.distance(geom2)

    cross['dist_ft'] = distances
    cross['dist_km'] = cross['dist_ft'] / 3281
    cross['dist_km'] = cross['dist_km'].round(1)
    cross = cross[['orig_geoid', 'dest_geoid', 'dist_km']]
    cross = cross.rename(columns={'orig_geoid': 'cbg_orig', 'dest_geoid': 'cbg_dest'})
    matrix = cross.pivot(index='cbg_orig', columns='cbg_dest', values='dist_km')

    df = pd.read_csv(cbg_check_csv)
    li1 = list(df['cbg_orig'])
    li2 = list(matrix.index.values)
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    if len(li_dif) > 0:
        for dif in li_dif:
            try:
                matrix = matrix.drop([dif], axis=0)
                matrix = matrix.drop([dif], axis=1)
            except:
                pass

    matrix.to_csv(csv_out)
    return matrix


def create_weights_matrix(csv_in, csv_out, dist_bin):
    df = pd.read_csv(csv_in)
    df = df.set_index('cbg_orig')

    for col in list(df.columns):
        df[col] = df[col].apply(lambda x: 1 if (x >= dist_bin[0]) & (x < dist_bin[1]) else 0)

    df.to_csv(csv_out.format(dist_bin[0], dist_bin[1]))
    return df


def create_weighted_matrix(df_values, df_weights):
    df = df_values.mul(df_weights)
    return df


def matrixcsv2df(csv_in, index_name):
    df = pd.read_csv(csv_in)
    df = df.set_index(index_name)
    return df
