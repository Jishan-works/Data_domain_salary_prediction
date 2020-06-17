# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:11:44 2020

@author: Jishan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load data
df = pd.read_csv("C:\\ML\\Analytics\\data_science_proj/glassdoor_jobs.csv")

#salary
df['hourly'] = df['Salary Estimate'].apply(lambda x : 1 if 'Per Hour' in x else 0 )
df['employer_provided'] = df['Salary Estimate'].apply(lambda x : 1 if 'Employer Provided Salary' in x else 0)

df=df[df["Salary Estimate"] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
salary_clean = salary.apply(lambda x: x.replace('$','').replace('K',''))

#avg_salary is our dependent variable
perhr_employer_removed = salary_clean.apply(lambda x : x.replace('Per Hour','').replace('Employer Provided Salary:',''))

df['min_salary'] = perhr_employer_removed.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = perhr_employer_removed.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2

#company
df['comp'] = df['Company Name'].apply(lambda x: x[:-3])

df['job_state'] = df['Location'].apply(lambda x : x.split(',')[1])
df['loc_hq_same'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis=1)

#age
df['age'] = df.Founded.apply(lambda x: 2020-x)

#using employee size of company
size_crct = df.Size.apply(lambda x: x.replace('to','-'))
df['size_crct'] = size_crct.apply(lambda x: x.split(' ')[:-1])
df['size_crct'] = df.size_crct.apply(lambda x: ' '.join([str(elem) for elem in x]))

df_out = df.drop(['Unnamed: 0'], axis=1)

df_out.to_csv('df_out.csv', index = False)





















































