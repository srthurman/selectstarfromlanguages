Title: Effects of Urbanization on Gender Equality: Part 3
Date: 2015-10-04
Tags: data, dataviz, demographics, python, pandas
slug: urbanization_and_gender_data_management
Summary: Part 2 Redux, but with Pandas

It appears I jumped ahead in my assignment for week 2 of Wesleyan's [Data Management and Visualization](https://www.coursera.org/learn/data-visualization) course when I re-grouped some of the data. But I still have an update for week 3 by doing the same thing, but this time with Python/Pandas.

I'll be posting this on Github as well, but for the convenience of my classmates, here is the code for this weeks results.

```python
# -*- coding: utf-8 -*-
import pandas
import numpy

#low_memory = False: increases efficiency when running the file
data = pandas.read_csv('urbanization_education_data_raw.csv', low_memory=False)

#upperCase all DatFrame column names
data.columns = map(str.upper, data.columns)

#bug fix for display formats to avoid runtime errors
pandas.set_option('display.float_format', lambda x:'%f'%x)

data['PER_URBAN_2011'] = data['PER_URBAN_2011'].convert_objects(convert_numeric=True)
data['GIRLS_IN_SCHOOL_RATIO'] = data['GIRLS_IN_SCHOOL_RATIO'].convert_objects(convert_numeric=False)
data['PRIMARY_SCHOOL_BOYS'] = data['PRIMARY_SCHOOL_BOYS'].convert_objects(convert_numeric=True)
data['PRIMARY_SCHOOL_GIRLS'] = data['PRIMARY_SCHOOL_GIRLS'].convert_objects(convert_numeric=True)
data['PRIMARY_SCHOOL_TOTAL'] = data['PRIMARY_SCHOOL_TOTAL'].convert_objects(convert_numeric=True)

##create data subsets
sub_gis = data[(data['GIRLS_IN_SCHOOL_RATIO'].notnull())]
sub_primary_school = data[(data['PRIMARY_SCHOOL_TOTAL'].notnull())]

#Function to group data from percents into groups
def GROUP_BY_TENS(row, variable):
    return 100 if row[variable] >= 100 else \
    90 if row[variable] >= 90 else \
    80 if row[variable] >= 80 else \
    70 if row[variable] >= 70 else \
    60 if row[variable] >= 60 else \
    50 if row[variable] >= 50 else \
    40 if row[variable] >= 40 else \
    30 if row[variable] >= 30 else \
    20 if row[variable] >= 20 else \
    10 if row[variable] >= 10 else \
    0

#Add new PER_URBAN variable
data['PER_URBAN'] = data.apply (lambda row: GROUP_BY_TENS(row,'PER_URBAN_2011'),axis=1)

#Recalculate PRIMART_SCHOOL variables
sub_primary_school['PRIMARY_SCHOOL_TOTAL'] = sub_primary_school.apply(lambda row: GROUP_BY_TENS(row,'PRIMARY_SCHOOL_TOTAL'),axis=1)
sub_primary_school['PRIMARY_SCHOOL_GIRLS'] = sub_primary_school.apply(lambda row: GROUP_BY_TENS(row,'PRIMARY_SCHOOL_GIRLS'),axis=1)
sub_primary_school['PRIMARY_SCHOOL_BOYS'] = sub_primary_school.apply(lambda row: GROUP_BY_TENS(row,'PRIMARY_SCHOOL_BOYS'),axis=1)

print("Counts of percent of population living in an Urban Area in 2011")
ct_urban = data.groupby('PER_URBAN').size()
print(ct_urban)

print("Distribution of percent of population living in an Urban Area in 2011")
pt_urban = data.groupby('PER_URBAN').size() * 100 / len(data)
print(pt_urban)

print("Count of ratio of girls to boys in Primary and Secondary school")
ct_gis= sub_gis.groupby('GIRLS_IN_SCHOOL_RATIO').size()
print(ct_gis)

print("Distribution of ratio of girls to boys in Primary and Secondary school")
pt_gis = sub_gis.groupby('GIRLS_IN_SCHOOL_RATIO').size() * 100 / len(sub_gis)
print(pt_gis)

print("Count of percent of boys completing primary school")
ct_school_boys = sub_primary_school.groupby('PRIMARY_SCHOOL_BOYS').size()
print(ct_school_boys)

print("Distribution of percent of boys completing primary school")
pt_school_boys = sub_primary_school.groupby('PRIMARY_SCHOOL_BOYS').size() * 100 / len(sub_primary_school)
print(pt_school_boys)

print("Count of percent of girls completing primary school")
ct_school_girls = sub_primary_school.groupby('PRIMARY_SCHOOL_GIRLS').size()
print(ct_school_girls)

print("Distribution of percent of girls completing primary school")
pt_school_girls = sub_primary_school.groupby('PRIMARY_SCHOOL_GIRLS').size() * 100 / len(sub_primary_school)
print(pt_school_girls)

print("Count of percent of girls & boys completing primary school")
ct_school_total = sub_primary_school.groupby('PRIMARY_SCHOOL_TOTAL').size()
print(ct_school_total)

print("Distribution of percent of girls & boys completing primary school")
pt_school_total = sub_primary_school.groupby('PRIMARY_SCHOOL_TOTAL').size() * 100 / len(sub_primary_school)
print(pt_school_total)
```

If you're not familiar with the syntax I'm using in the `GROUP_BY_TENS` function, see this StackOverflow question on [Python and ternary conditional operators](http://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator).

And the frequency distributions:
```
Counts of percent of population living in an Urban Area in 2011
PER_URBAN
10     14
20     19
30     28
40     22
50     25
60     32
70     24
80     23
90     17
100     6
dtype: int64
Distribution of percent of population living in an Urban Area in 2011
PER_URBAN
10     6.666667
20     9.047619
30    13.333333
40    10.476190
50    11.904762
60    15.238095
70    11.428571
80    10.952381
90     8.095238
100    2.857143
dtype: float64
Count of ratio of girls to boys in Primary and Secondary school
GIRLS_IN_SCHOOL_RATIO
64.000000      1
66.000000      1
75.000000      1
79.000000      3
80.000000      2
82.000000      1
86.000000      1
88.000000      1
89.000000      2
90.000000      4
94.000000      4
95.000000      3
96.000000      3
97.000000      8
98.000000     16
99.000000     19
100.000000    16
101.000000    12
102.000000    17
103.000000     5
104.000000     8
105.000000     1
106.000000     3
107.000000     2
108.000000     2
109.000000     1
dtype: int64
Distribution of ratio of girls to boys in Primary and Secondary school
GIRLS_IN_SCHOOL_RATIO
64.000000     0.729927
66.000000     0.729927
75.000000     0.729927
79.000000     2.189781
80.000000     1.459854
82.000000     0.729927
86.000000     0.729927
88.000000     0.729927
89.000000     1.459854
90.000000     2.919708
94.000000     2.919708
95.000000     2.189781
96.000000     2.189781
97.000000     5.839416
98.000000    11.678832
99.000000    13.868613
100.000000   11.678832
101.000000    8.759124
102.000000   12.408759
103.000000    3.649635
104.000000    5.839416
105.000000    0.729927
106.000000    2.189781
107.000000    1.459854
108.000000    1.459854
109.000000    0.729927
dtype: float64
Count of percent of boys completing primary school
PRIMARY_SCHOOL_BOYS
0       2
40      4
50      6
60      8
70     13
80     19
90     45
100    35
dtype: int64
Distribution of percent of boys completing primary school
PRIMARY_SCHOOL_BOYS
0      1.515152
40     3.030303
50     4.545455
60     6.060606
70     9.848485
80    14.393939
90    34.090909
100   26.515152
dtype: float64
Count of percent of girls completing primary school
PRIMARY_SCHOOL_GIRLS
0       2
20      1
30      3
40      3
50      9
60      7
70      8
80     16
90     46
100    37
dtype: int64
Distribution of percent of girls completing primary school
PRIMARY_SCHOOL_GIRLS
0      1.515152
20     0.757576
30     2.272727
40     2.272727
50     6.818182
60     5.303030
70     6.060606
80    12.121212
90    34.848485
100   28.030303
dtype: float64
Count of percent of girls & boys completing primary school
PRIMARY_SCHOOL_TOTAL
30      2
40      4
50      6
60     10
70      9
80     17
90     45
100    39
dtype: int64
Distribution of percent of girls & boys completing primary school
PRIMARY_SCHOOL_TOTAL
30     1.515152
40     3.030303
50     4.545455
60     7.575758
70     6.818182
80    12.878788
90    34.090909
100   29.545455
dtype: float64
```

Here's my analysis from my [Week 2 blog post](/urbanization_and_gender_first_analysis.html):

> For all variables except `GIRLS_IN_SCHOOL_RATIO`, the data represent the percentage of the population in question. The number listed as a category represents the lower range of a decile of the data distribution (so 90 represents 90%-100%, 80 represents 80%-89.99%, etc.). In some cases the ratio can exceed 100%, and so 100 is included as a category to include those cases. For detailed information on each of the variables used here, see my [Codebook](https://docs.google.com/spreadsheets/d/1zYf7P7lnjFMdVp6CCQV0t0TgFRBUfa7oz9TqIfaZSzY/edit?usp=sharing).

> `GIRLS_IN_SCHOOL_RATIO` represents the Gender Parity Index of girls to boys in primary and secondary school. The important point to know for this analysis is that 100 indicates gender parity/equality in schooling, > 100 indicates gender inequality favoring females (more girls than boys in school), and < 100 indicates gender inequality favoring males (more boys than girls in school). That's a high level explanation, and I encourage you to look up 'Gender Parity' if you're intrested in knowing more.

> Calculations for `GIRLS_IN_SCHOOL_RATIO` were created from a subset of the larger dataset which excludes countries missing data values for that field. Similarly, each of the the `PRIMARY_SCHOOL` calculations used a subset of data which excludes countries missing data in the `PRIMARY_SCHOOL_TOTAL` field.

> Looking at the frequency distributions, we can see that urbanization rates are pretty evenly distributed, with the biggest distribution, ~15%, occuring in the 60 (60%-70%) category. Education levels for both boys and girls tend to be at a pretty high level, and the girls in school ratio distribution clusters around 100. At a global scale, boys and girls are enrolled in school at relatively even rates, and most are finishing primary and secondary school.

I know that was lazy, but...things look the same as during my analysis last week. The one difference you may note is in the counts for the 90 and 100 categories for the three `PRIMARY_SCHOOL` categories. The categorizing I did in my initial data management and that done with Pandas was a little different.