import pandas as pd
import statistics
import csv

df=pd.read_csv("data.csv")
height_list=df["Height(Inches)"].tolist()
weight_list=df["Weight(Pounds)"].tolist()

height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)

height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)

height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)

std_deviation=statistics.stdev(height_list)
std_deviation=statistics.stdev(weight_list)

print("The mean of height is: ",height_mean)
print("The mean of weight is: ",weight_mean)
print("The median of height is: ",height_median)
print("The median of weight is: ",weight_median)
print("The mode of height is: ",height_mode)
print("The mode of weight is: ",weight_mode)

height_first_std_deviation_start, height_first_std_deviation_end = height_mean-std_deviation, height_mean+std_deviation
weight_first_std_deviation_start, weight_first_std_deviation_end = weight_mean-std_deviation, weight_mean+std_deviation

height_second_std_deviation_start, height_second_std_deviation_end = height_mean-(2*std_deviation), height_mean+(2*std_deviation)
weight_second_std_deviation_start, weight_second_std_deviation_end = weight_mean-(2*std_deviation), weight_mean+(2*std_deviation)

height_third_std_deviation_start, height_third_std_deviation_end = height_mean-(3*std_deviation), height_mean+(3*std_deviation)
weight_third_std_deviation_start, weight_third_std_deviation_end = weight_mean-(3*std_deviation), weight_mean+(3*std_deviation)

height_list_of_data_within_1_std_deviation = [result for result in height_list if result > height_first_std_deviation_start and result < height_first_std_deviation_end]
weight_list_of_data_within_1_std_deviation = [result for result in weight_list if result > weight_first_std_deviation_start and result < weight_first_std_deviation_end]

height_list_of_data_within_2_std_deviation = [result for result in height_list if result > height_second_std_deviation_start and result < height_second_std_deviation_end]
weight_list_of_data_within_2_std_deviation = [result for result in weight_list if result > weight_second_std_deviation_start and result < weight_second_std_deviation_end]

height_list_of_data_within_3_std_deviation = [result for result in height_list if result > height_third_std_deviation_start and result < height_third_std_deviation_end]
weight_list_of_data_within_3_std_deviation = [result for result in weight_list if result > weight_third_std_deviation_start and result < weight_third_std_deviation_end]

print("{}% of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(height_list)))
print("{}% of data for weight lies within 1 standard deviation".format(len(weight_list_of_data_within_1_std_deviation)*100.0/len(weight_list)))

print("{}% of data for height lies within 2 standard deviation".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(height_list)))
print("{}% of data for weight lies within 2 standard deviation".format(len(weight_list_of_data_within_2_std_deviation)*100.0/len(weight_list)))

print("{}% of data for height lies within 3 standard deviation".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(height_list)))
print("{}% of data for weight lies within 3 standard deviation".format(len(weight_list_of_data_within_3_std_deviation)*100.0/len(weight_list)))