Title: Effects of Urbanization on Gender Equality: Part 2
Date: 2015-09-27
Tags: data, dataviz, demographics, python, pandas
slug: urbanization_and_gender_first_analysis
Summary: A preliminary exploration of the data with Pandas

For my assignment in week 2 of Wesleyan's [Data Management and Visualization](https://www.coursera.org/learn/data-visualization) course, I created frequency distributions of my data using Python's Pandas, and the Spyder IDE.

I'll be posting this on Github as well, but for the convenience of my classmates, below is the code I used to create the frequency distributions.

```python
# -*- coding: utf-8 -*-
import pandas
import numpy

#low_memory = False: increases efficiency when running the file
data = pandas.read_csv('urbanization_education_data.csv', low_memory=False)

#upperCase all DataFrame column names
data.columns = map(str.upper, data.columns)

#bug fix for display formats to avoid runtime errors
pandas.set_option('display.float_format', lambda x:'%f'%x)

data['PER_URBAN_2010'] = data['PER_URBAN_2010'].convert_objects(convert_numeric=True)
data['GIRLS_IN_SCHOOL_RATIO'] = data['GIRLS_IN_SCHOOL_RATIO'].convert_objects(convert_numeric=True)
data['PRIMARY_SCHOOL_BOYS'] = data['PRIMARY_SCHOOL_BOYS'].convert_objects(convert_numeric=True)
data['PRIMARY_SCHOOL_GIRLS'] = data['PRIMARY_SCHOOL_GIRLS'].convert_objects(convert_numeric=True)
data['PRIMARY_SCHOOL_TOTAL'] = data['PRIMARY_SCHOOL_TOTAL'].convert_objects(convert_numeric=True)

sub_gis = data[(data['GIRLS_IN_SCHOOL_RATIO'] > 0)]
sub_primary_school = data[(data['PRIMARY_SCHOOL_TOTAL'] > 0)]

print(len(data))
print(len(data.columns))

print("Counts of percent of population living in an Urban Area in 2010")
ct_urban = data.groupby('PER_URBAN_2010').size()
print(ct_urban)

print("Distribution of percent of population living in an Urban Area in 2010")
pt_urban = data.groupby('PER_URBAN_2010').size() * 100 / len(data)
print(pt_urban)

print("Count of ratio of girls to boys in Primary and Secondary school")
ct_gis= sub_gis.groupby('GIRLS_IN_SCHOOL_RATIO').size()
print(ct_gis)

print("Percentage of ratio of girls to boys in Primary and Secondary school")
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

And here are the resulting frequency distributions:
```
Counts of percent of population living in an Urban Area in 2010
PER_URBAN_2010
10    14
20    19
30    28
40    22
50    25
60    32
70    24
80    23
90    23

Distribution of percent of population living in an Urban Area in 2010
PER_URBAN_2010
10    6.666667
20    9.047619
30   13.333333
40   10.476190
50   11.904762
60   15.238095
70   11.428571
80   10.952381
90   10.952381

Count of ratio of girls to boys in Primary and Secondary school
GIRLS_IN_SCHOOL_RATIO
63      1
65      1
75      1
78      3
79      1
80      1
81      1
85      1
87      1
88      2
89      2
90      2
93      3
94      2
95      4
96      2
97     13
98     22
99     13
100    14
101    15
102    13
103     7
104     4
105     1
106     3
107     2
108     2

Percentage of ratio of girls to boys in Primary and Secondary school
GIRLS_IN_SCHOOL_RATIO
63     0.729927
65     0.729927
75     0.729927
78     2.189781
79     0.729927
80     0.729927
81     0.729927
85     0.729927
87     0.729927
88     1.459854
89     1.459854
90     1.459854
93     2.189781
94     1.459854
95     2.919708
96     1.459854
97     9.489051
98    16.058394
99     9.489051
100   10.218978
101   10.948905
102    9.489051
103    5.109489
104    2.919708
105    0.729927
106    2.189781
107    1.459854
108    1.459854

Count of percent of boys completing primary school
PRIMARY_SCHOOL_BOYS
0       2
40      4
50      6
60      8
70     13
80     19
90     46
100    34

Distribution of percent of boys completing primary school
PRIMARY_SCHOOL_BOYS
0      1.515152
40     3.030303
50     4.545455
60     6.060606
70     9.848485
80    14.393939
90    34.848485
100   25.757576

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
90     47
100    36

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
90    35.606061
100   27.272727

Count of percent of girls & boys completing primary school
PRIMARY_SCHOOL_TOTAL
30      2
40      4
50      6
60     10
70      9
80     17
90     46
100    38

Distribution of percent of girls & boys completing primary school
PRIMARY_SCHOOL_TOTAL
30     1.515152
40     3.030303
50     4.545455
60     7.575758
70     6.818182
80    12.878788
90    34.848485
100   28.787879
```

For all variables except `GIRLS_IN_SCHOOL_RATIO`, the data represent the percentage of the population in question. The number listed as a category represents the lower range of a decile of the data distribution (so 90 represents 90%-100%, 80 represents 80%-89.99%, etc.). In some cases the ratio can exceed 100%, and so 100 is included as a category to include those cases. For detailed information on each of the variables used here, see my [Codebook](https://docs.google.com/spreadsheets/d/1zYf7P7lnjFMdVp6CCQV0t0TgFRBUfa7oz9TqIfaZSzY/edit?usp=sharing).

`GIRLS_IN_SCHOOL_RATIO` represents the Gender Parity Index of girls to boys in primary and secondary school. The important point to know for this analysis is that 100 indicates gender parity/equality in schooling, > 100 indicates gender inequality favoring females (more girls than boys in school), and < 100 indicates gender inequality favoring males (more boys than girls in school). That's a high level explanation, and I encourage you to look up 'Gender Parity' if you're intrested in knowing more.

Calculations for `GIRLS_IN_SCHOOL_RATIO` were created from a subset of the larger dataset which excludes countries missing data values for that field. Similarly, each of the the `PRIMARY_SCHOOL` calculations used a subset of data which excludes countries missing data in the `PRIMARY_SCHOOL_TOTAL` field.

Looking at the frequency distributions, we can see that urbanization rates are pretty evenly distributed, with the biggest distribution, ~15%, occuring in the 60 (60%-70%) category. Education levels for both boys and girls tend to be at a pretty high level, and the girls in school ratio distribution clusters around 100. At a global scale, boys and girls are enrolled in school at relatively even rates, and most are finishing primary and secondary school.

Regarding the original research question (Is there an association between a country's level of urbanization and female education levels?), there aren't any strong conclusions to be made at this point as we haven't looked at the per-country data in detail yet.