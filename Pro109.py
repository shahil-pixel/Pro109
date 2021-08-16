import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics
import random
import csv

df = pd.read_csv("perfomance109.csv")

math = df["math score"].to_list()
reading = df["reading score"].to_list()
writing = df["writing score"].to_list()

#Mean for maths,reading and writing
maths_mean = statistics.mean(math)
reading_mean = statistics.mean(reading)
writing_mean = statistics.mean(writing)

#Median for maths,reading and writing
maths_median = statistics.median(math)
reading_median = statistics.median(reading)
writing_median = statistics.median(writing)

#Mode for maths,reading and writing
maths_mode = statistics.mode(math)
reading_mode = statistics.mode(reading)
writing_mode = statistics.mode(writing)

#Printing mean, median and mode to validate
print("Mean, Median and Mode of maths is {}, {} and {} respectively".format(maths_mean, maths_median, maths_mode))
print("Mean, Median and Mode of reading is {}, {} and {} respectively".format(reading_mean, reading_median, reading_mode))
print("Mean, Median and Mode of writing is {}, {} and {} respectively".format(writing_mean, writing_median, writing_mode))

#Standard deviation for maths,reading and writing
maths_std_deviation = statistics.stdev(math)
reading_std_deviation = statistics.stdev(reading)
writing_std_deviation = statistics.stdev(writing)

#1, 2 and 3 Standard Deviations for reading
reading_first_std_deviation_start, reading_first_std_deviation_end = reading_mean-reading_std_deviation, reading_mean+reading_std_deviation
reading_second_std_deviation_start, reading_second_std_deviation_end = reading_mean-(2*reading_std_deviation), reading_mean+(2*reading_std_deviation)
reading_third_std_deviation_start, reading_third_std_deviation_end = reading_mean-(3*reading_std_deviation), reading_mean+(3*reading_std_deviation)

#1, 2 and 3 Standard Deviations for maths
maths_first_std_deviation_start, maths_first_std_deviation_end = maths_mean-maths_std_deviation, maths_mean+maths_std_deviation
maths_second_std_deviation_start, maths_second_std_deviation_end = maths_mean-(2*maths_std_deviation), maths_mean+(2*maths_std_deviation)
maths_third_std_deviation_start, maths_third_std_deviation_end = maths_mean-(3*maths_std_deviation), maths_mean+(3*maths_std_deviation)

#1, 2 and 3 Standard Deviations for writing
writing_first_std_deviation_start, writing_first_std_deviation_end = writing_mean-writing_std_deviation, writing_mean+writing_std_deviation
writing_second_std_deviation_start, writing_second_std_deviation_end = writing_mean-(2*writing_std_deviation), writing_mean+(2*writing_std_deviation)
writing_third_std_deviation_start, writing_third_std_deviation_end = writing_mean-(3*writing_std_deviation), writing_mean+(3*writing_std_deviation)

#Percentage of data within 1, 2 and 3 Standard Deviations for maths
maths_list_of_data_within_1_std_deviation = [result for result in math if result > maths_first_std_deviation_start and result < maths_first_std_deviation_end]
maths_list_of_data_within_2_std_deviation = [result for result in math  if result > maths_second_std_deviation_start and result < maths_second_std_deviation_end]
maths_list_of_data_within_3_std_deviation = [result for result in math  if result > maths_third_std_deviation_start and result < maths_third_std_deviation_end]

#Percentage of data within 1, 2 and 3 Standard Deviations for reading
reading_list_of_data_within_1_std_deviation = [result for result in reading if result > reading_first_std_deviation_start and result < reading_first_std_deviation_end]
reading_list_of_data_within_2_std_deviation = [result for result in reading if result > reading_second_std_deviation_start and result < reading_second_std_deviation_end]
reading_list_of_data_within_3_std_deviation = [result for result in reading if result > reading_third_std_deviation_start and result < reading_third_std_deviation_end]

#Percentage of data within 1, 2 and 3 Standard Deviations for writing
writing_list_of_data_within_1_std_deviation = [result for result in writing if result > writing_first_std_deviation_start and result < writing_first_std_deviation_end]
writing_list_of_data_within_2_std_deviation = [result for result in writing if result > writing_second_std_deviation_start and result < writing_second_std_deviation_end]
writing_list_of_data_within_3_std_deviation = [result for result in writing if result > writing_third_std_deviation_start and result < writing_third_std_deviation_end]

#Printing data for maths,reading and writing(Standard Deviation)
print("{}% of data for maths lies within 1 standard deviation".format(len(maths_list_of_data_within_1_std_deviation)*100.0/len(math)))
print("{}% of data for maths lies within 2 standard deviations".format(len(maths_list_of_data_within_2_std_deviation)*100.0/len(math)))
print("{}% of data for maths lies within 3 standard deviations".format(len(maths_list_of_data_within_3_std_deviation)*100.0/len(math)))

print("{}% of data for reading lies within 1 standard deviation".format(len(reading_list_of_data_within_1_std_deviation)*100.0/len(reading)))
print("{}% of data for reading lies within 2 standard deviations".format(len(reading_list_of_data_within_2_std_deviation)*100.0/len(reading)))
print("{}% of data for reading lies within 3 standard deviations".format(len(reading_list_of_data_within_3_std_deviation)*100.0/len(reading)))

print("{}% of data for writing lies within 1 standard deviation".format(len(writing_list_of_data_within_1_std_deviation)*100.0/len(writing)))
print("{}% of data for writing lies within 2 standard deviations".format(len(writing_list_of_data_within_2_std_deviation)*100.0/len(writing)))
print("{}% of data for writing lies within 3 standard deviations".format(len(writing_list_of_data_within_3_std_deviation)*100.0/len(writing)))
