# Jessica Embury, San Diego State University, Fall 2022
# SpSSIM analysis of LODES and SafeGraph flow data

from matrixes import *
from analysis import *

##################################
# IN/OUT PATHS FOR FLOW MATRIXES #
##################################
main_path = './data/'
bg_csv = '{}source_data/cbgs_2019.csv'.format(main_path)
lodes_csv_in = '{}source_data/lodes_od_2019.csv'.format(main_path)
lodes_raw_matrix = '{}raw_matrix/sd_lodes_2019_raw_matrix.csv'.format(main_path)
lodes_probs_matrix = '{}flow_probabilities/sd_lodes_2019_flow_probabilities_matrix.csv'.format(main_path)

sg_csv_in = '{}source_data/sg_od_2019.csv'.format(main_path)
sg_raw_matrix = '{}raw_matrix/sd_sg_2019_raw_matrix.csv'.format(main_path)
sg_probs_matrix = '{}flow_probabilities/sd_sg_2019_flow_probabilities_matrix.csv'.format(main_path)

yyyymm = ['201901', '201902', '201903', '201904', '201905', '201906', '201907', '201908', '201909', '201910', '201911', '201912']
sg1_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[0])
sg1_raw_matrix = '{}raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[0])
sg1_probs_matrix = '{}flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[0])

sg2_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[1])
sg2_raw_matrix = '{}raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[1])
sg2_probs_matrix = '{}flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[1])

sg3_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[2])
sg3_raw_matrix = '{}raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[2])
sg3_probs_matrix = '{}flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[2])

sg4_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[3])
sg4_raw_matrix = '{}raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[3])
sg4_probs_matrix = '{}flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[3])

sg5_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[4])
sg5_raw_matrix = '{}raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[4])
sg5_probs_matrix = '{}flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[4])

sg6_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[5])
sg6_raw_matrix = '{}raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[5])
sg6_probs_matrix = '{}flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[5])

sg7_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[6])
sg7_raw_matrix = '{}raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[6])
sg7_probs_matrix = '{}flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[6])

sg8_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[7])
sg8_raw_matrix = '{}raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[7])
sg8_probs_matrix = '{}flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[7])

sg9_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[8])
sg9_raw_matrix = '{}raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[8])
sg9_probs_matrix = '{}flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[8])

sg10_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[9])
sg10_raw_matrix = '{}raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[9])
sg10_probs_matrix = '{}flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[9])

sg11_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[10])
sg11_raw_matrix = '{}raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[10])
sg11_probs_matrix = '{}flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[10])

sg12_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[11])
sg12_raw_matrix = '{}raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[11])
sg12_probs_matrix = '{}flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[11])

####################################
# IN/OUT PATHS FOR DISTANCE MATRIX #
####################################
bg_shp = '{}source_data/CENSUS_BLOCKGROUPTIGER2010/CENSUS_BLOCKGROUPTIGER2010.shp'.format(main_path)
dist_matrix = '{}cbg_distance_matrix.csv'.format(main_path)  # max distance = 123.1km

#####################################
# IN/OUT PATHS FOR WEIGHTS MATRIXES #
#####################################
weights_matrix = './data/weights_10km_bins/weights_matrix_{}km_{}km.csv'

############################
# SpSSIM VARIABLES & PATHS #
############################
distance_bins = [(0, 10), (10, 20), (20, 30), (30, 40), (40, 50), (50, 60), (60, 70), (70, 80), (80, 90), (90, 100), (100, 110), (110, 120)]  # , (120, 130)]

r1csv = '{}/spssim_results/lodes2019_lodes2019.csv'.format(main_path)
r2csv = '{}/spssim_results/lodes2019_sg2019.csv'.format(main_path)
r3csv = '{}/spssim_results/lodes2019_sg201901.csv'.format(main_path)
r4csv = '{}/spssim_results/lodes2019_sg201902.csv'.format(main_path)
r5csv = '{}/spssim_results/lodes2019_sg201903.csv'.format(main_path)
r6csv = '{}/spssim_results/lodes2019_sg201904.csv'.format(main_path)
r7csv = '{}/spssim_results/lodes2019_sg201905.csv'.format(main_path)
r8csv = '{}/spssim_results/lodes2019_sg201906.csv'.format(main_path)
r9csv = '{}/spssim_results/lodes2019_sg201907.csv'.format(main_path)
r10csv = '{}/spssim_results/lodes2019_sg201908.csv'.format(main_path)
r11csv = '{}/spssim_results/lodes2019_sg201909.csv'.format(main_path)
r12csv = '{}/spssim_results/lodes2019_sg201910.csv'.format(main_path)
r13csv = '{}/spssim_results/lodes2019_sg201911.csv'.format(main_path)
r14csv = '{}/spssim_results/lodes2019_sg201912.csv'.format(main_path)
r15csv = '{}/spssim_results/sg2019_sg201901.csv'.format(main_path)
r16csv = '{}/spssim_results/sg2019_sg201902.csv'.format(main_path)
r17csv = '{}/spssim_results/sg2019_sg201903.csv'.format(main_path)
r18csv = '{}/spssim_results/sg2019_sg201904.csv'.format(main_path)
r19csv = '{}/spssim_results/sg2019_sg201905.csv'.format(main_path)
r20csv = '{}/spssim_results/sg2019_sg201906.csv'.format(main_path)
r21csv = '{}/spssim_results/sg2019_sg201907.csv'.format(main_path)
r22csv = '{}/spssim_results/sg2019_sg201908.csv'.format(main_path)
r23csv = '{}/spssim_results/sg2019_sg201909.csv'.format(main_path)
r24csv = '{}/spssim_results/sg2019_sg201910.csv'.format(main_path)
r25csv = '{}/spssim_results/sg2019_sg201911.csv'.format(main_path)
r26csv = '{}/spssim_results/sg2019_sg201912.csv'.format(main_path)

########
# MAIN #
########
if __name__ == '__main__':
    ###############################################################################
    # Use input O-D tables to create flow matrixes and probability flow matrixes. #
    ###############################################################################
    '''
    lodesa = odtable2matrix(lodes_csv_in, lodes_raw_matrix, 'cbg_orig', 'cbg_dest', 'num_jobs')
    lodesb = create_probability_matrix(lodes_raw_matrix, lodes_probs_matrix, 'cbg_orig')
    sga = odtable2matrix(sg_csv_in, sg_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sgb = create_probability_matrix(sg_raw_matrix, sg_probs_matrix, 'cbg_orig')
    sg1a = odtable2matrix(sg1_csv_in, sg1_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg1b = create_probability_matrix(sg1_raw_matrix, sg1_probs_matrix, 'cbg_orig')
    sg2a = odtable2matrix(sg2_csv_in, sg2_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg2b = create_probability_matrix(sg2_raw_matrix, sg2_probs_matrix, 'cbg_orig')
    sg3a = odtable2matrix(sg3_csv_in, sg3_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg3b = create_probability_matrix(sg3_raw_matrix, sg3_probs_matrix, 'cbg_orig')
    sg4a = odtable2matrix(sg4_csv_in, sg4_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg4b = create_probability_matrix(sg4_raw_matrix, sg4_probs_matrix, 'cbg_orig')
    sg5a = odtable2matrix(sg5_csv_in, sg5_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg5b = create_probability_matrix(sg5_raw_matrix, sg5_probs_matrix, 'cbg_orig')
    sg6a = odtable2matrix(sg6_csv_in, sg6_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg6b = create_probability_matrix(sg6_raw_matrix, sg6_probs_matrix, 'cbg_orig')
    sg7a = odtable2matrix(sg7_csv_in, sg7_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg7b = create_probability_matrix(sg7_raw_matrix, sg7_probs_matrix, 'cbg_orig')
    sg8a = odtable2matrix(sg8_csv_in, sg8_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg8b = create_probability_matrix(sg8_raw_matrix, sg8_probs_matrix, 'cbg_orig')
    sg9a = odtable2matrix(sg9_csv_in, sg9_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg9b = create_probability_matrix(sg9_raw_matrix, sg9_probs_matrix, 'cbg_orig')
    sg10a = odtable2matrix(sg10_csv_in, sg10_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg10b = create_probability_matrix(sg10_raw_matrix, sg10_probs_matrix, 'cbg_orig')
    sg11a = odtable2matrix(sg11_csv_in, sg11_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg11b = create_probability_matrix(sg11_raw_matrix, sg11_probs_matrix, 'cbg_orig')
    sg12a = odtable2matrix(sg12_csv_in, sg12_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg12b = create_probability_matrix(sg12_raw_matrix, sg12_probs_matrix, 'cbg_orig')
    '''
    ##############################################
    # Create distance matrix from CBG shapefile. #
    ##############################################
    # dist = create_distance_matrix(bg_shp, lodes_raw_matrix, dist_matrix)

    ########################################################
    # Create weights matrixes according to specified bins. #
    ########################################################
    # for b in distance_bins:
        # df = create_weights_matrix(dist_matrix, weights_matrix, b)

    #####################
    # Calculate SpSSIM. #
    #####################
    # CHECK: Same flows matrix produces SpSSIM = 1
    spssim, results = calc_global_spssim(lodes_probs_matrix, lodes_probs_matrix, weights_matrix, r1csv, 'cbg_orig', distance_bins)

    # LODES & SafeGraph
    # LODES 2019 & SafeGraph 2019 (Annual & Monthly)
    spssim, results = calc_global_spssim(lodes_probs_matrix, sg_probs_matrix, weights_matrix, r2csv, 'cbg_orig', distance_bins)
    # LODES 2019 & SafeGraph JAN 2019
    spssim, results = calc_global_spssim(lodes_probs_matrix, sg1_probs_matrix, weights_matrix, r3csv, 'cbg_orig', distance_bins)
    # LODES 2019 & SafeGraph FEB 2019
    spssim, results = calc_global_spssim(lodes_probs_matrix, sg2_probs_matrix, weights_matrix, r4csv, 'cbg_orig', distance_bins)
    # LODES 2019 & SafeGraph MAR 2019
    spssim, results = calc_global_spssim(lodes_probs_matrix, sg3_probs_matrix, weights_matrix, r5csv, 'cbg_orig', distance_bins)
    # LODES 2019 & SafeGraph APR 2019
    spssim, results = calc_global_spssim(lodes_probs_matrix, sg4_probs_matrix, weights_matrix, r6csv, 'cbg_orig', distance_bins)
    # LODES 2019 & SafeGraph MAY 2019
    spssim, results = calc_global_spssim(lodes_probs_matrix, sg5_probs_matrix, weights_matrix, r7csv, 'cbg_orig', distance_bins)
    # LODES 2019 & SafeGraph JUN 2019
    spssim, results = calc_global_spssim(lodes_probs_matrix, sg6_probs_matrix, weights_matrix, r8csv, 'cbg_orig', distance_bins)
    # LODES 2019 & SafeGraph JUL 2019
    spssim, results = calc_global_spssim(lodes_probs_matrix, sg7_probs_matrix, weights_matrix, r9csv, 'cbg_orig', distance_bins)
    # LODES 2019 & SafeGraph AUG 2019
    spssim, results = calc_global_spssim(lodes_probs_matrix, sg8_probs_matrix, weights_matrix, r10csv, 'cbg_orig', distance_bins)
    # LODES 2019 & SafeGraph SEP 2019
    spssim, results = calc_global_spssim(lodes_probs_matrix, sg9_probs_matrix, weights_matrix, r11csv, 'cbg_orig', distance_bins)
    # LODES 2019 & SafeGraph OCT 2019
    spssim, results = calc_global_spssim(lodes_probs_matrix, sg10_probs_matrix, weights_matrix, r12csv, 'cbg_orig', distance_bins)
    # LODES 2019 & SafeGraph NOV 2019
    spssim, results = calc_global_spssim(lodes_probs_matrix, sg11_probs_matrix, weights_matrix, r13csv, 'cbg_orig', distance_bins)
    # LODES 2019 & SafeGraph DEC 2019
    spssim, results = calc_global_spssim(lodes_probs_matrix, sg12_probs_matrix, weights_matrix, r14csv, 'cbg_orig', distance_bins)

    # SafeGraph Annual Avg & SafeGraph Monthly
    # SafeGraph 2019 & SafeGraph JAN 2019
    spssim, results = calc_global_spssim(sg_probs_matrix, sg1_probs_matrix, weights_matrix, r15csv, 'cbg_orig', distance_bins)
    # SafeGraph 2019 & SafeGraph FEB 2019
    spssim, results = calc_global_spssim(sg_probs_matrix, sg2_probs_matrix, weights_matrix, r16csv, 'cbg_orig', distance_bins)
    # SafeGraph 2019 & SafeGraph MAR 2019
    spssim, results = calc_global_spssim(sg_probs_matrix, sg3_probs_matrix, weights_matrix, r17csv, 'cbg_orig', distance_bins)
    # SafeGraph 2019 & SafeGraph APR 2019
    spssim, results = calc_global_spssim(sg_probs_matrix, sg4_probs_matrix, weights_matrix, r18csv, 'cbg_orig', distance_bins)
    # SafeGraph 2019 & SafeGraph MAY 2019
    spssim, results = calc_global_spssim(sg_probs_matrix, sg5_probs_matrix, weights_matrix, r19csv, 'cbg_orig', distance_bins)
    # SafeGraph 2019 & SafeGraph JUN 2019
    spssim, results = calc_global_spssim(sg_probs_matrix, sg6_probs_matrix, weights_matrix, r20csv, 'cbg_orig', distance_bins)
    # SafeGraph 2019 & SafeGraph JUL 2019
    spssim, results = calc_global_spssim(sg_probs_matrix, sg7_probs_matrix, weights_matrix, r21csv, 'cbg_orig', distance_bins)
    # SafeGraph 2019 & SafeGraph AUG 2019
    spssim, results = calc_global_spssim(sg_probs_matrix, sg8_probs_matrix, weights_matrix, r22csv, 'cbg_orig', distance_bins)
    # SafeGraph 2019 & SafeGraph SEP 2019
    spssim, results = calc_global_spssim(sg_probs_matrix, sg9_probs_matrix, weights_matrix, r23csv, 'cbg_orig', distance_bins)
    # SafeGraph 2019 & SafeGraph OCT 2019
    spssim, results = calc_global_spssim(sg_probs_matrix, sg10_probs_matrix, weights_matrix, r24csv, 'cbg_orig', distance_bins)
    # SafeGraph 2019 & SafeGraph NOV 2019
    spssim, results = calc_global_spssim(sg_probs_matrix, sg11_probs_matrix, weights_matrix, r25csv, 'cbg_orig', distance_bins)
    # SafeGraph 2019 & SafeGraph DEC 2019
    spssim, results = calc_global_spssim(sg_probs_matrix, sg12_probs_matrix, weights_matrix, r26csv, 'cbg_orig', distance_bins)


