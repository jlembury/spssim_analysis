# Jessica Embury, San Diego State University, Fall 2022
# Local SpSSIM analysis of LODES and SafeGraph flow data

from matrixes import *
from spssim_local_analysis import *

###############
# SOURCE DATA #
###############
BG_CSV = './data/source_data/cbgs_2019.csv'
BG_SHP = './data/source_data/CENSUS_BLOCKGROUPTIGER2010/CENSUS_BLOCKGROUPTIGER2010.shp'
LODES_CSV_IN = './data/source_data/lodes_od_2019.csv'
SG_ANNUAL_CSV_IN = './data/source_data/sg_od_2019.csv'
SG_MONTH_CSV_IN = './data/source_data/sod_od_{}.csv'  # Specify month in YYYYMM format.
SG_DOW_CSV_IN = './data/source_data/sg_od_2019_dow{}.csv'  # Specify day of week (00=Sun - 06=Sat, wd=weekdays, we-weekends)

################
# MATRIX PATHS #
################
DIST_MATRIX = './data/cbg_distance_matrix.csv'  # max distance = 123.1km
WEIGHTS_MATRIX = './data/weights_{}km_bins/weights_matrix_{}km_{}km.csv'

LODES_ANNUAL_INFLOW_OD_MATRIX = './data/spssim_local/od_matrixes/lodes2019_inflow_od_matrix.csv'
LODES_ANNUAL_OUTFLOW_OD_MATRIX = './data/spssim_local/od_matrixes/lodes2019_outflow_od_matrix.csv'
SG_ANNUAL_INFLOW_OD_MATRIX = './data/spssim_local/od_matrixes/sg2019_annual_inflow_od_matrix.csv'
SG_ANNUAL_OUTFLOW_OD_MATRIX = './data/spssim_local/od_matrixes/sg2019_annual_outflow_od_matrix.csv'
SG_MONTH_INFLOW_OD_MATRIX = './data/spssim_local/od_matrixes/sg2019_month{}_inflow_od_matrix.csv'
SG_MONTH_OUTFLOW_OD_MATRIX = './data/spssim_local/od_matrixes/sg2019_month{}_outflow_od_matrix.csv'
SG_DOW_INFLOW_OD_MATRIX = './data/spssim_local/od_matrixes/sg2019_dow{}_inflow_od_matrix.csv'
SG_DOW_OUTFLOW_OD_MATRIX = './data/spssim_local/od_matrixes/sg2019_dow{}_outflow_od_matrix.csv'

LODES_ANNUAL_INFLOW_PROB_MATRIX = './data/spssim_local/flow_probabilities/lodes2019_inflow_probability_matrix.csv'
LODES_ANNUAL_OUTFLOW_PROB_MATRIX = './data/spssim_local/flow_probabilities/lodes2019_outflow_probability_matrix.csv'
SG_ANNUAL_INFLOW_PROB_MATRIX = './data/spssim_local/flow_probabilities/sg2019_annual_inflow_probability_matrix.csv'
SG_ANNUAL_OUTFLOW_PROB_MATRIX = './data/spssim_local/flow_probabilities/sg2019_annual_outflow_probability_matrix.csv'
SG_MONTH_INFLOW_PROB_MATRIX = './data/spssim_local/flow_probabilities/sg2019_month{}_inflow_probability_matrix.csv'
SG_MONTH_OUTFLOW_PROB_MATRIX = './data/spssim_local/flow_probabilities/sg2019_month{}_outflow_probability_matrix.csv'
SG_DOW_INFLOW_PROB_MATRIX = './data/spssim_local/flow_probabilities/sg2019_dow{}_inflow_probability_matrix.csv'
SG_DOW_OUTFLOW_PROB_MATRIX = './data/spssim_local/flow_probabilities/sg2019_dow{}_outflow_probability_matrix.csv'

################
# SPSSIM PATHS #
################
SG_ANNUAL_INFLOW_BINS = './data/spssim_local/inflow_{}km_bin_results/spssim_inflow_sg2019_lodes2019_bin{}km{}km.csv'
SG_ANNUAL_INFLOW_LOCAL = './data/spssim_local/spssim_inflow_sg2019_lodes2019_{}km_bins.csv'
SG_ANNUAL_OUTFLOW_BINS = './data/spssim_local/outflow_{}km_bin_results/spssim_outflow_sg2019_lodes2019_bin{}km{}km.csv'
SG_ANNUAL_OUTFLOW_LOCAL = './data/spssim_local/spssim_outflow_sg2019_lodes2019_{}km_bins.csv'
SG_MONTH_INFLOW_BINS = './data/spssim_local/inflow_{}km_bin_results/spssim_inflow_sg{}_lodes2019_bin{}km{}km.csv'
SG_MONTH_INFLOW_LOCAL = './data/spssim_local/spssim_inflow_sg{}_lodes2019_{}km_bins.csv'
SG_MONTH_OUTFLOW_BINS = './data/spssim_local/outflow_{}km_bin_results/spssim_outflow_sg{}_lodes2019_bin{}km{}km.csv'
SG_MONTH_OUTFLOW_LOCAL = './data/spssim_local/spssim_outflow_sg{}_lodes2019_{}km_bins.csv'
SG_DOW_INFLOW_BINS = './data/spssim_local/inflow_{}km_bin_results/spssim_inflow_sg2019dow{}_lodes2019_bin{}km{}km.csv'
SG_DOW_INFLOW_LOCAL = './data/spssim_local/spssim_inflow_sg2019dow{}_lodes2019_{}km_bins.csv'
SG_DOW_OUTFLOW_BINS = './data/spssim_local/outflow_{}km_bin_results/spssim_outflow_sg2019dow{}_lodes2019_bin{}km{}km.csv'
SG_DOW_OUTFLOW_LOCAL = './data/spssim_local/spssim_outflow_sg2019dow{}_lodes2019_{}km_bins.csv'
INFLOW_DIR = './data/spssim_local/inflow_{}km_bin_results/'
OUTFLOW_DIR = './data/spssim_local/outflow_{}km_bin_results/'

#############
# CONSTANTS #
#############
MONTH_LIST = ['201901', '201902', '201903', '201904', '201905', '201906', '201907', '201908', '201909', '201910', '201911', '201912']
DOW_LIST = ['00', '01', '02', '03', '04', '05', '06', 'wds', 'wes']

DISTANCE_BINS_10 = [(0, 10), (10, 20), (20, 30), (30, 40), (40, 50), (50, 60), (60, 70)]  # , (70, 80), (80, 90), (90, 100), (100, 110), (110, 120), (120, 130)]
BIN_SIZE_10 = '10'

DISTANCE_BINS_05 = [(0, 5), (5, 10), (10, 15), (15, 20), (20, 25), (25, 30), (30, 35), (35, 40), (40, 45), (45, 50), (50, 55), (55, 60), (60, 65), (65, 70)]  # , (70, 75), (75, 80), (80, 85), (85, 90), (90, 95), (95, 100), (100, 105), (105, 110), (110, 115), (115, 120), (120, 125)]
BIN_SIZE_05 = '05'

INDEX_NAME = 'cbg_orig'
COLUMN_NAME = 'cbg_dest'
LODES_VALUES = 'num_jobs'
SG_VALUES = 'dev_count'
CONSTANT1 = 0
CONSTANT2 = 0.000001  # 1.603250954187884e-08

########
# MAIN #
########
if __name__ == '__main__':
    # CREATE ALL MATRIXES FOR ANALYSIS (INFLOW/OUTFLOW PROBABILITIES, WEIGHTS) - ONLY NEED TO RUN ONCE FOR EACH SOURCE DATASET OR BIN SIZE
    # annual data
    lodes_in_prob = create_local_probability_matrix(LODES_CSV_IN, LODES_ANNUAL_INFLOW_OD_MATRIX, LODES_ANNUAL_INFLOW_PROB_MATRIX, INDEX_NAME, COLUMN_NAME, LODES_VALUES, inflow=True)
    lodes_out_prob = create_local_probability_matrix(LODES_CSV_IN, LODES_ANNUAL_OUTFLOW_OD_MATRIX, LODES_ANNUAL_OUTFLOW_PROB_MATRIX, INDEX_NAME, COLUMN_NAME, LODES_VALUES, inflow=False)
    sg_annual_in_prob = create_local_probability_matrix(SG_ANNUAL_CSV_IN, SG_ANNUAL_INFLOW_OD_MATRIX, SG_ANNUAL_INFLOW_PROB_MATRIX, INDEX_NAME, COLUMN_NAME, SG_VALUES, inflow=True)
    sg_annual_out_prob = create_local_probability_matrix(SG_ANNUAL_CSV_IN, SG_ANNUAL_OUTFLOW_OD_MATRIX, SG_ANNUAL_OUTFLOW_PROB_MATRIX, INDEX_NAME, COLUMN_NAME, SG_VALUES, inflow=False)
    # monthly and daily data
    for m in MONTH_LIST:
        sg_month_in_prob = create_local_probability_matrix(SG_MONTH_CSV_IN.format(m), SG_MONTH_INFLOW_OD_MATRIX, SG_MONTH_INFLOW_PROB_MATRIX.format(m), INDEX_NAME, COLUMN_NAME, SG_VALUES, inflow=True)
        sg_month_out_prob = create_local_probability_matrix(SG_MONTH_CSV_IN.format(m), SG_ANNUAL_OUTFLOW_OD_MATRIX, SG_MONTH_OUTFLOW_PROB_MATRIX.format(m), INDEX_NAME, COLUMN_NAME, SG_VALUES, inflow=False)
    for d in DOW_LIST:
        sg_dow_in_prob = create_local_probability_matrix(SG_DOW_CSV_IN.format(d), SG_DOW_INFLOW_OD_MATRIX, SG_DOW_INFLOW_PROB_MATRIX.format(d), INDEX_NAME, COLUMN_NAME, SG_VALUES, inflow=True)
        sg_dow_out_prob = create_local_probability_matrix(SG_DOW_CSV_IN.format(d), SG_DOW_OUTFLOW_OD_MATRIX, SG_DOW_OUTFLOW_PROB_MATRIX.format(d), INDEX_NAME, COLUMN_NAME, SG_VALUES, inflow=False)
    
    # distance weights
    for b10 in DISTANCE_BINS_10:
        w10 = create_weights_matrix(DIST_MATRIX, WEIGHTS_MATRIX.format(BIN_SIZE_10, b10[0], b10[1]), b10)
    for b05 in DISTANCE_BINS_05:
        w05 = create_weights_matrix(DIST_MATRIX, WEIGHTS_MATRIX.format(BIN_SIZE_05, b05[0], b05[1]), b05)

    # CALCULATE LOCAL SPSSIM (10KM BINS)
    # annual

    sg_annual_in = calc_local_spssim(LODES_ANNUAL_INFLOW_PROB_MATRIX, SG_ANNUAL_INFLOW_PROB_MATRIX, WEIGHTS_MATRIX.format(BIN_SIZE_10, '{}', '{}'), SG_ANNUAL_INFLOW_BINS.format(BIN_SIZE_10, '{}', '{}'), SG_ANNUAL_INFLOW_LOCAL.format(BIN_SIZE_10), DISTANCE_BINS_10, INDEX_NAME, CONSTANT1, CONSTANT2)
    sg_annual_out = calc_local_spssim(LODES_ANNUAL_OUTFLOW_PROB_MATRIX, SG_ANNUAL_OUTFLOW_PROB_MATRIX, WEIGHTS_MATRIX.format(BIN_SIZE_10, '{}', '{}'), SG_ANNUAL_OUTFLOW_BINS.format(BIN_SIZE_10, '{}', '{}'), SG_ANNUAL_OUTFLOW_LOCAL.format(BIN_SIZE_10), DISTANCE_BINS_10, INDEX_NAME, CONSTANT1, CONSTANT2)
    # months
    for m in MONTH_LIST:
        sg_month_in = calc_local_spssim(LODES_ANNUAL_INFLOW_PROB_MATRIX, SG_MONTH_INFLOW_PROB_MATRIX.format(m), WEIGHTS_MATRIX.format(BIN_SIZE_10, '{}', '{}'), SG_MONTH_INFLOW_BINS.format(BIN_SIZE_10, m, '{}', '{}'), SG_MONTH_INFLOW_LOCAL.format(m, BIN_SIZE_10), DISTANCE_BINS_10, INDEX_NAME, CONSTANT1, CONSTANT2)
        sg_month_out = calc_local_spssim(LODES_ANNUAL_OUTFLOW_PROB_MATRIX, SG_MONTH_OUTFLOW_PROB_MATRIX.format(m), WEIGHTS_MATRIX.format(BIN_SIZE_10, '{}', '{}'), SG_MONTH_OUTFLOW_BINS.format(BIN_SIZE_10, m, '{}', '{}'), SG_MONTH_OUTFLOW_LOCAL.format(m, BIN_SIZE_10), DISTANCE_BINS_10, INDEX_NAME, CONSTANT1, CONSTANT2)
    # dow
    for d in DOW_LIST:
        sg_dow_in = calc_local_spssim(LODES_ANNUAL_INFLOW_PROB_MATRIX, SG_DOW_INFLOW_PROB_MATRIX.format(d), WEIGHTS_MATRIX.format(BIN_SIZE_10, '{}', '{}'), SG_DOW_INFLOW_BINS.format(BIN_SIZE_10, d, '{}', '{}'), SG_DOW_INFLOW_LOCAL.format(d, BIN_SIZE_10), DISTANCE_BINS_10, INDEX_NAME, CONSTANT1, CONSTANT2)
        sg_dow_out = calc_local_spssim(LODES_ANNUAL_OUTFLOW_PROB_MATRIX, SG_DOW_OUTFLOW_PROB_MATRIX.format(d), WEIGHTS_MATRIX.format(BIN_SIZE_10, '{}', '{}'), SG_DOW_OUTFLOW_BINS.format(BIN_SIZE_10, d, '{}', '{}'), SG_DOW_OUTFLOW_LOCAL.format(d, BIN_SIZE_10), DISTANCE_BINS_10, INDEX_NAME, CONSTANT1, CONSTANT2)

    # CALCULATE LOCAL SPSSIM (05KM BINS)
    # annual
    sg_annual_in = calc_local_spssim(LODES_ANNUAL_INFLOW_PROB_MATRIX, SG_ANNUAL_INFLOW_PROB_MATRIX, WEIGHTS_MATRIX.format(BIN_SIZE_05, '{}', '{}'), SG_ANNUAL_INFLOW_BINS.format(BIN_SIZE_05, '{}', '{}'), SG_ANNUAL_INFLOW_LOCAL.format(BIN_SIZE_05), DISTANCE_BINS_05, INDEX_NAME, CONSTANT1, CONSTANT2)
    sg_annual_out = calc_local_spssim(LODES_ANNUAL_OUTFLOW_PROB_MATRIX, SG_ANNUAL_OUTFLOW_PROB_MATRIX, WEIGHTS_MATRIX.format(BIN_SIZE_05, '{}', '{}'), SG_ANNUAL_OUTFLOW_BINS.format(BIN_SIZE_05, '{}', '{}'), SG_ANNUAL_OUTFLOW_LOCAL.format(BIN_SIZE_05), DISTANCE_BINS_05, INDEX_NAME, CONSTANT1, CONSTANT2)
    # months
    for m in MONTH_LIST:
        sg_month_in = calc_local_spssim(LODES_ANNUAL_INFLOW_PROB_MATRIX, SG_MONTH_INFLOW_PROB_MATRIX.format(m), WEIGHTS_MATRIX.format(BIN_SIZE_05, '{}', '{}'), SG_MONTH_INFLOW_BINS.format(BIN_SIZE_05, m, '{}', '{}'), SG_MONTH_INFLOW_LOCAL.format(m, BIN_SIZE_05), DISTANCE_BINS_05, INDEX_NAME, CONSTANT1, CONSTANT2)
        sg_month_out = calc_local_spssim(LODES_ANNUAL_OUTFLOW_PROB_MATRIX, SG_MONTH_OUTFLOW_PROB_MATRIX.format(m), WEIGHTS_MATRIX.format(BIN_SIZE_05, '{}', '{}'), SG_MONTH_OUTFLOW_BINS.format(BIN_SIZE_05, m, '{}', '{}'), SG_MONTH_OUTFLOW_LOCAL.format(m, BIN_SIZE_05), DISTANCE_BINS_05, INDEX_NAME, CONSTANT1, CONSTANT2)
    # dow
    for d in DOW_LIST:
        sg_dow_in = calc_local_spssim(LODES_ANNUAL_INFLOW_PROB_MATRIX, SG_DOW_INFLOW_PROB_MATRIX.format(d), WEIGHTS_MATRIX.format(BIN_SIZE_05, '{}', '{}'), SG_DOW_INFLOW_BINS.format(BIN_SIZE_05, d, '{}', '{}'), SG_DOW_INFLOW_LOCAL.format(d, BIN_SIZE_05), DISTANCE_BINS_05, INDEX_NAME, CONSTANT1, CONSTANT2)
        sg_dow_out = calc_local_spssim(LODES_ANNUAL_OUTFLOW_PROB_MATRIX, SG_DOW_OUTFLOW_PROB_MATRIX.format(d), WEIGHTS_MATRIX.format(BIN_SIZE_05, '{}', '{}'), SG_DOW_OUTFLOW_BINS.format(BIN_SIZE_05, d, '{}', '{}'), SG_DOW_OUTFLOW_LOCAL.format(d, BIN_SIZE_05), DISTANCE_BINS_05, INDEX_NAME, CONSTANT1, CONSTANT2)

    # CALCULATE CONSTANTS
    constant1, constant2 = calc_local_constants([INFLOW_DIR.format(BIN_SIZE_05), OUTFLOW_DIR.format(BIN_SIZE_05), INFLOW_DIR.format(BIN_SIZE_10), OUTFLOW_DIR.format(BIN_SIZE_10)])
    print(constant1, constant2)

