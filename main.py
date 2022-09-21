# Jessica Embury, San Diego State University, Fall 2022
# Distance-Based SpSSIM analysis of LODES and SafeGraph flow data

from matrixes import *
from spssim_distbased_analysis import *

##################################
# IN/OUT PATHS FOR FLOW MATRIXES #
##################################
main_path = './data/'
bg_csv = '{}source_data/cbgs_2019.csv'.format(main_path)
lodes_csv_in = '{}source_data/lodes_od_2019.csv'.format(main_path)
lodes_raw_matrix = '{}spssim_distance_based/raw_matrix/sd_lodes_2019_raw_matrix.csv'.format(main_path)
lodes_probs_matrix = '{}spssim_distance_based/flow_probabilities/sd_lodes_2019_flow_probabilities_matrix.csv'.format(main_path)

sg_csv_in = '{}source_data/sg_od_2019.csv'.format(main_path)
sg_raw_matrix = '{}spssim_distance_based/raw_matrix/sd_sg_2019_raw_matrix.csv'.format(main_path)
sg_probs_matrix = '{}spssim_distance_based/flow_probabilities/sd_sg_2019_flow_probabilities_matrix.csv'.format(main_path)

# monthly flows
yyyymm = ['201901', '201902', '201903', '201904', '201905', '201906', '201907', '201908', '201909', '201910', '201911', '201912']
sg1_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[0])
sg1_raw_matrix = '{}spssim_distance_based/raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[0])
sg1_probs_matrix = '{}spssim_distance_based/flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[0])

sg2_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[1])
sg2_raw_matrix = '{}spssim_distance_based/raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[1])
sg2_probs_matrix = '{}spssim_distance_based/flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[1])

sg3_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[2])
sg3_raw_matrix = '{}spssim_distance_based/raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[2])
sg3_probs_matrix = '{}spssim_distance_based/flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[2])

sg4_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[3])
sg4_raw_matrix = '{}spssim_distance_based/raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[3])
sg4_probs_matrix = '{}spssim_distance_based/flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[3])

sg5_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[4])
sg5_raw_matrix = '{}spssim_distance_based/raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[4])
sg5_probs_matrix = '{}spssim_distance_based/flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[4])

sg6_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[5])
sg6_raw_matrix = '{}spssim_distance_based/raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[5])
sg6_probs_matrix = '{}spssim_distance_based/flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[5])

sg7_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[6])
sg7_raw_matrix = '{}spssim_distance_based/raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[6])
sg7_probs_matrix = '{}spssim_distance_based/flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[6])

sg8_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[7])
sg8_raw_matrix = '{}spssim_distance_based/raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[7])
sg8_probs_matrix = '{}spssim_distance_based/flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[7])

sg9_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[8])
sg9_raw_matrix = '{}spssim_distance_based/raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[8])
sg9_probs_matrix = '{}spssim_distance_based/flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[8])

sg10_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[9])
sg10_raw_matrix = '{}spssim_distance_based/raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[9])
sg10_probs_matrix = '{}spssim_distance_based/flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[9])

sg11_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[10])
sg11_raw_matrix = '{}spssim_distance_based/raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[10])
sg11_probs_matrix = '{}spssim_distance_based/flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[10])

sg12_csv_in = '{}source_data/sod_od_{}.csv'.format(main_path, yyyymm[11])
sg12_raw_matrix = '{}spssim_distance_based/raw_matrix/sg_raw_matrix_{}.csv'.format(main_path, yyyymm[11])
sg12_probs_matrix = '{}spssim_distance_based/flow_probabilities/sg_flow_probabilities_matrix_{}.csv'.format(main_path, yyyymm[11])

# flows by day of the week
sg_dow00_csv_in = '{}source_data/sg_od_2019_dow00.csv'.format(main_path)
sg_dow00_raw_matrix = '{}spssim_distance_based/raw_matrix/sg_raw_matrix_dow00.csv'.format(main_path)
sg_dow00_probs_matrix = '{}spssim_distance_based/flow_probabilities/sg_flow_probabilities_matrix_dow00.csv'.format(main_path)

sg_dow01_csv_in = '{}source_data/sg_od_2019_dow01.csv'.format(main_path)
sg_dow01_raw_matrix = '{}spssim_distance_based/raw_matrix/sg_raw_matrix_dow01.csv'.format(main_path)
sg_dow01_probs_matrix = '{}spssim_distance_based/flow_probabilities/sg_flow_probabilities_matrix_dow01.csv'.format(main_path)

sg_dow02_csv_in = '{}source_data/sg_od_2019_dow02.csv'.format(main_path)
sg_dow02_raw_matrix = '{}spssim_distance_based/raw_matrix/sg_raw_matrix_dow02.csv'.format(main_path)
sg_dow02_probs_matrix = '{}spssim_distance_based/flow_probabilities/sg_flow_probabilities_matrix_dow02.csv'.format(main_path)

sg_dow03_csv_in = '{}source_data/sg_od_2019_dow03.csv'.format(main_path)
sg_dow03_raw_matrix = '{}spssim_distance_based/raw_matrix/sg_raw_matrix_dow03.csv'.format(main_path)
sg_dow03_probs_matrix = '{}spssim_distance_based/flow_probabilities/sg_flow_probabilities_matrix_dow03.csv'.format(main_path)

sg_dow04_csv_in = '{}source_data/sg_od_2019_dow04.csv'.format(main_path)
sg_dow04_raw_matrix = '{}spssim_distance_based/raw_matrix/sg_raw_matrix_dow04.csv'.format(main_path)
sg_dow04_probs_matrix = '{}spssim_distance_based/flow_probabilities/sg_flow_probabilities_matrix_dow04.csv'.format(main_path)

sg_dow05_csv_in = '{}source_data/sg_od_2019_dow05.csv'.format(main_path)
sg_dow05_raw_matrix = '{}spssim_distance_based/raw_matrix/sg_raw_matrix_dow05.csv'.format(main_path)
sg_dow05_probs_matrix = '{}spssim_distance_based/flow_probabilities/sg_flow_probabilities_matrix_dow05.csv'.format(main_path)

sg_dow06_csv_in = '{}source_data/sg_od_2019_dow06.csv'.format(main_path)
sg_dow06_raw_matrix = '{}spssim_distance_based/raw_matrix/sg_raw_matrix_dow06.csv'.format(main_path)
sg_dow06_probs_matrix = '{}spssim_distance_based/flow_probabilities/sg_flow_probabilities_matrix_dow06.csv'.format(main_path)

sg_dow_wds_csv_in = '{}source_data/sg_od_2019_dow_wds.csv'.format(main_path)
sg_dow_wds_raw_matrix = '{}spssim_distance_based/raw_matrix/sg_raw_matrix_dow_wds.csv'.format(main_path)
sg_dow_wds_probs_matrix = '{}spssim_distance_based/flow_probabilities/sg_flow_probabilities_matrix_dow_wds.csv'.format(main_path)

sg_dow_wes_csv_in = '{}source_data/sg_od_2019_dow_wes.csv'.format(main_path)
sg_dow_wes_raw_matrix = '{}spssim_distance_based/raw_matrix/sg_raw_matrix_dow_wes.csv'.format(main_path)
sg_dow_wes_probs_matrix = '{}spssim_distance_based/flow_probabilities/sg_flow_probabilities_matrix_dow_wes.csv'.format(main_path)
####################################
# IN/OUT PATHS FOR DISTANCE MATRIX #
####################################
bg_shp = '{}source_data/CENSUS_BLOCKGROUPTIGER2010/CENSUS_BLOCKGROUPTIGER2010.shp'.format(main_path)
dist_matrix = '{}cbg_distance_matrix.csv'.format(main_path)  # max distance = 123.1km

#####################################
# IN/OUT PATHS FOR WEIGHTS MATRIXES #
#####################################
# weights_matrix = './data/weights_10km_bins/weights_matrix_{}km_{}km.csv'
weights_matrix = './data/weights_05km_bins/weights_matrix_{}km_{}km.csv'

############################
# SpSSIM VARIABLES & PATHS #
############################
# distance_bins = [(0, 10), (10, 20), (20, 30), (30, 40), (40, 50), (50, 60), (60, 70), (70, 80), (80, 90), (90, 100), (100, 110), (110, 120), (120, 130)]
# dist_bin_size = '10'

distance_bins = [(0, 5), (5, 10), (10, 15), (15, 20), (20, 25), (25, 30), (30, 35), (35, 40), (40, 45), (45, 50), (50, 55), (55, 60), (60, 65), (65, 70), (70, 75), (75, 80), (80, 85), (85, 90), (90, 95), (95, 100), (100, 105), (105, 110), (110, 115), (115, 120), (120, 125)]
dist_bin_size = '05'

r1csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_lodes2019_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r2csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg2019_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r3csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg201901_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r4csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg201902_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r5csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg201903_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r6csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg201904_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r7csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg201905_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r8csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg201906_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r9csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg201907_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r10csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg201908_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r11csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg201909_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r12csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg201910_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r13csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg201911_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r14csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg201912_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r15csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg2019_dow00_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r16csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg2019_dow01_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r17csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg2019_dow02_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r18csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg2019_dow03_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r19csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg2019_dow04_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r20csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg2019_dow05_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r21csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg2019_dow06_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r22csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg2019_dow_weekdays_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)
r23csv = '{}spssim_distance_based/spssim_results/spssim_results_{}km_bins/lodes2019_sg2019_dow_weekends_{}kmbins.csv'.format(main_path, dist_bin_size, dist_bin_size)

###############################
# CONSTANTS VARIABLES & PATHS #
###############################
# Using c1=0 and c2=2.55093291502342e-16, the minimum distance-based SpSSIM=-3.727811409356615e-22
results_directory_05kmbins = '{}spssim_distance_based/spssim_results/spssim_results_05km_bins/'.format(main_path)
results_directory_10kmbins = '{}spssim_distance_based/spssim_results/spssim_results_10km_bins/'.format(main_path)
results_directory_main = [results_directory_05kmbins, results_directory_10kmbins]
constant1 = 0  # -2.5509321224232315e-16
constant2 = 2.55093291502342e-16

########################
# SPSSIM SUMMARY PATHS #
########################
globsumm05km_csv = '{}spssim_distance_based/spssim_results_summary_global_05kmbins.csv'.format(main_path)
distbasedsumm05km_csv = '{}spssim_distance_based/spssim_results_summary_distbased_05kmbins.csv'.format(main_path)
globsumm10km_csv = '{}spssim_distance_based/spssim_results_summary_global_10kmbins.csv'.format(main_path)
distbasedsumm10km_csv = '{}spssim_distance_based/spssim_results_summary_distbased_10kmbins.csv'.format(main_path)

########
# MAIN #
########
if __name__ == '__main__':
    # Only need to run first two sections once. No need to rerun for different distance bins or SpSSIM matrix pairings.
    ##############################################
    # Create distance matrix from CBG shapefile. #
    ##############################################
    dist = create_distance_matrix(bg_shp, lodes_raw_matrix, dist_matrix)
    
    ###############################################################################
    # Use input O-D tables to create flow matrixes and probability flow matrixes. #
    ###############################################################################
    lodesa = odtable2matrix(lodes_csv_in, lodes_raw_matrix, 'cbg_orig', 'cbg_dest', 'num_jobs')
    lodesb = create_distbased_probability_matrix(lodes_raw_matrix, lodes_probs_matrix, 'cbg_orig')
    sga = odtable2matrix(sg_csv_in, sg_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sgb = create_distbased_probability_matrix(sg_raw_matrix, sg_probs_matrix, 'cbg_orig')
    sg1a = odtable2matrix(sg1_csv_in, sg1_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg1b = create_distbased_probability_matrix(sg1_raw_matrix, sg1_probs_matrix, 'cbg_orig')
    sg2a = odtable2matrix(sg2_csv_in, sg2_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg2b = create_distbased_probability_matrix(sg2_raw_matrix, sg2_probs_matrix, 'cbg_orig')
    sg3a = odtable2matrix(sg3_csv_in, sg3_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg3b = create_distbased_probability_matrix(sg3_raw_matrix, sg3_probs_matrix, 'cbg_orig')
    sg4a = odtable2matrix(sg4_csv_in, sg4_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg4b = create_distbased_probability_matrix(sg4_raw_matrix, sg4_probs_matrix, 'cbg_orig')
    sg5a = odtable2matrix(sg5_csv_in, sg5_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg5b = create_distbased_probability_matrix(sg5_raw_matrix, sg5_probs_matrix, 'cbg_orig')
    sg6a = odtable2matrix(sg6_csv_in, sg6_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg6b = create_distbased_probability_matrix(sg6_raw_matrix, sg6_probs_matrix, 'cbg_orig')
    sg7a = odtable2matrix(sg7_csv_in, sg7_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg7b = create_distbased_probability_matrix(sg7_raw_matrix, sg7_probs_matrix, 'cbg_orig')
    sg8a = odtable2matrix(sg8_csv_in, sg8_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg8b = create_distbased_probability_matrix(sg8_raw_matrix, sg8_probs_matrix, 'cbg_orig')
    sg9a = odtable2matrix(sg9_csv_in, sg9_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg9b = create_distbased_probability_matrix(sg9_raw_matrix, sg9_probs_matrix, 'cbg_orig')
    sg10a = odtable2matrix(sg10_csv_in, sg10_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg10b = create_distbased_probability_matrix(sg10_raw_matrix, sg10_probs_matrix, 'cbg_orig')
    sg11a = odtable2matrix(sg11_csv_in, sg11_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg11b = create_distbased_probability_matrix(sg11_raw_matrix, sg11_probs_matrix, 'cbg_orig')
    sg12a = odtable2matrix(sg12_csv_in, sg12_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg12b = create_distbased_probability_matrix(sg12_raw_matrix, sg12_probs_matrix, 'cbg_orig')
    sg_dow00a = odtable2matrix(sg_dow00_csv_in, sg_dow00_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg_dow00b = create_distbased_probability_matrix(sg_dow00_raw_matrix, sg_dow00_probs_matrix, 'cbg_orig')
    sg_dow01a = odtable2matrix(sg_dow01_csv_in, sg_dow01_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg_dow01b = create_distbased_probability_matrix(sg_dow01_raw_matrix, sg_dow01_probs_matrix, 'cbg_orig')
    sg_dow02a = odtable2matrix(sg_dow02_csv_in, sg_dow02_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg_dow02b = create_distbased_probability_matrix(sg_dow02_raw_matrix, sg_dow02_probs_matrix, 'cbg_orig')
    sg_dow03a = odtable2matrix(sg_dow03_csv_in, sg_dow03_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg_dow03b = create_distbased_probability_matrix(sg_dow03_raw_matrix, sg_dow03_probs_matrix, 'cbg_orig')
    sg_dow04a = odtable2matrix(sg_dow04_csv_in, sg_dow04_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg_dow04b = create_distbased_probability_matrix(sg_dow04_raw_matrix, sg_dow04_probs_matrix, 'cbg_orig')
    sg_dow05a = odtable2matrix(sg_dow05_csv_in, sg_dow05_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg_dow05b = create_distbased_probability_matrix(sg_dow05_raw_matrix, sg_dow05_probs_matrix, 'cbg_orig')
    sg_dow06a = odtable2matrix(sg_dow06_csv_in, sg_dow06_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg_dow06b = create_distbased_probability_matrix(sg_dow06_raw_matrix, sg_dow06_probs_matrix, 'cbg_orig')
    sg_dow_wdsa = odtable2matrix(sg_dow_wds_csv_in, sg_dow_wds_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg_dow_wdsb = create_distbased_probability_matrix(sg_dow_wds_raw_matrix, sg_dow_wds_probs_matrix, 'cbg_orig')
    sg_dow_wesa = odtable2matrix(sg_dow_wes_csv_in, sg_dow_wes_raw_matrix, 'cbg_orig', 'cbg_dest', 'dev_count')
    sg_dow_wesb = create_distbased_probability_matrix(sg_dow_wes_raw_matrix, sg_dow_wes_probs_matrix, 'cbg_orig')
    
    ########################################################
    # Create weights matrixes according to specified bins. #
    ########################################################
    for b in distance_bins:
        df = create_weights_matrix(dist_matrix, weights_matrix, b)


    #####################
    # Calculate SpSSIM. #
    #####################
    # CHECK: Same flows matrix produces SpSSIM = 1
    # spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, lodes_probs_matrix, weights_matrix, r1csv, 'cbg_orig', distance_bins, constant1, constant2)

    # LODES & SafeGraph
    # LODES 2019 & SafeGraph 2019 (Annual)
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg_probs_matrix, weights_matrix, r2csv, 'cbg_orig', distance_bins, constant1, constant2)

    # LODES 2019 & SafeGraph 2019 (Monthly)
    # LODES 2019 & SafeGraph JAN 2019
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg1_probs_matrix, weights_matrix, r3csv, 'cbg_orig', distance_bins, constant1, constant2)
    # LODES 2019 & SafeGraph FEB 2019
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg2_probs_matrix, weights_matrix, r4csv, 'cbg_orig', distance_bins, constant1, constant2)
    # LODES 2019 & SafeGraph MAR 2019
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg3_probs_matrix, weights_matrix, r5csv, 'cbg_orig', distance_bins, constant1, constant2)
    # LODES 2019 & SafeGraph APR 2019
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg4_probs_matrix, weights_matrix, r6csv, 'cbg_orig', distance_bins, constant1, constant2)
    # LODES 2019 & SafeGraph MAY 2019
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg5_probs_matrix, weights_matrix, r7csv, 'cbg_orig', distance_bins, constant1, constant2)
    # LODES 2019 & SafeGraph JUN 2019
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg6_probs_matrix, weights_matrix, r8csv, 'cbg_orig', distance_bins, constant1, constant2)
    # LODES 2019 & SafeGraph JUL 2019
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg7_probs_matrix, weights_matrix, r9csv, 'cbg_orig', distance_bins, constant1, constant2)
    # LODES 2019 & SafeGraph AUG 2019
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg8_probs_matrix, weights_matrix, r10csv, 'cbg_orig', distance_bins, constant1, constant2)
    # LODES 2019 & SafeGraph SEP 2019
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg9_probs_matrix, weights_matrix, r11csv, 'cbg_orig', distance_bins, constant1, constant2)
    # LODES 2019 & SafeGraph OCT 2019
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg10_probs_matrix, weights_matrix, r12csv, 'cbg_orig', distance_bins, constant1, constant2)
    # LODES 2019 & SafeGraph NOV 2019
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg11_probs_matrix, weights_matrix, r13csv, 'cbg_orig', distance_bins, constant1, constant2)
    # LODES 2019 & SafeGraph DEC 2019
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg12_probs_matrix, weights_matrix, r14csv, 'cbg_orig', distance_bins, constant1, constant2)

    # LODES 2019 & SafeGraph 2019 (Day of Week)
    # LODES 2019 & SafeGraph DOW00 (SUNDAY)
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg_dow00_probs_matrix, weights_matrix, r15csv, 'cbg_orig', distance_bins, constant1, constant2)
    # LODES 2019 & SafeGraph DOW01
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg_dow01_probs_matrix, weights_matrix, r16csv, 'cbg_orig', distance_bins, constant1, constant2)
    # LODES 2019 & SafeGraph DOW02
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg_dow02_probs_matrix, weights_matrix, r17csv, 'cbg_orig', distance_bins, constant1, constant2)
    # LODES 2019 & SafeGraph DOW03
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg_dow03_probs_matrix, weights_matrix, r18csv, 'cbg_orig', distance_bins, constant1, constant2)
    # LODES 2019 & SafeGraph DOW04
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg_dow04_probs_matrix, weights_matrix, r19csv, 'cbg_orig', distance_bins, constant1, constant2)
    # LODES 2019 & SafeGraph DOW05
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg_dow05_probs_matrix, weights_matrix, r20csv, 'cbg_orig', distance_bins, constant1, constant2)
    # LODES 2019 & SafeGraph DOW06
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg_dow06_probs_matrix, weights_matrix, r21csv, 'cbg_orig', distance_bins, constant1, constant2)
    # LODES 2019 & SafeGraph DOW WEEKDAYS
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg_dow_wds_probs_matrix, weights_matrix, r22csv, 'cbg_orig', distance_bins, constant1, constant2)
    # LODES 2019 & SafeGraph DOW WEEKENDS
    spssim, results = calc_global_distbased_spssim(lodes_probs_matrix, sg_dow_wes_probs_matrix, weights_matrix, r23csv, 'cbg_orig', distance_bins, constant1, constant2)

    #######################
    # CALCULATE CONSTANTS #
    #######################
    # After first calculation of SpSSIM, calculate constants so that all SpSSIMs > 0 (and least similar SpSSIM = 0)
    constant1, constant2 = calc_distbased_spssim_constants(results_dir_list=results_directory_main)
    print(constant1, constant2)

    ##############################
    # GENERATE RESULTS SUMMARIES #
    ##############################
    glob05km, distbased05km = calc_distbased_results_summaries(results_directory_05kmbins, globsumm05km_csv, distbasedsumm05km_csv)
    glob10km, distbased10km = calc_distbased_results_summaries(results_directory_10kmbins, globsumm10km_csv, distbasedsumm10km_csv)
