# -*- coding: utf-8 -*-
"""Project .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1euLgTSOz6cX167smQCHU7RBuO26CFMQd

Employee satisfaction index

Objective of Study : Check their salary and other objectives to check they are satisfied or not

Importing libraries
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

"""# Dataset"""

df=pd.read_csv("/content/drive/MyDrive/Data science project/Employee Satisfaction Index.csv")
df

df.head(15)

df.shape

"""Observation : Here the dataset has 500 rows and 14 columns"""

df.dtypes

df.info()

"""Observation :

* emp_id has no null values and datatype is object
* age has no null values and datatype is integer
* department has no null values and datatype is object
* location has no null values and datatype is object
* education has no null values and datatype is object
* recruitment type has no null values and datatype is object
* job level has no null values and datatype is integer
* rating has no null values and datatype is integer
* certifications has no null values and datatype is integer
* satisfied has no null values and datatype is integer

etc..

"""

df.describe()

"""Observation :

* The avaerage level of satisfaction is 0.52
* The average  salary is 50416
* Minimum salary is 24076
* max salary is 86750
"""

df['Dept'].value_counts()

"""Obseration :

here we can see that what are the deparments people working and how many of them are working
"""

df['satisfied'].value_counts()

df['salary'].value_counts()

df.isnull().any()

"""Observation :

Here the dataset doesn't contain any null values
"""

df.isnull().sum()

"""Observation :

Through this we can find the sum of null values if there exist any null values
"""

df['salary']=(df['salary'].astype('int64'))
df['salary']

"""Usage :

used to remove the decimal values

# DATA VISUALIZATION
"""

plt.bar(df['Dept'],df['age'])
plt.title('Age v/s Dept')
plt.xlabel('Dept')
plt.ylabel('Age')
plt.legend('loc=lower left')

"""Observation :

Here we can understand that more than 50 years old people are working in all departments
"""

plt.bar(df['education'],df['job_level'])
plt.title('education v/s job level')
plt.xlabel('education')
plt.ylabel('level of job')
plt.legend('best')

"""observation :

here we can understand that people who completed either PG  or UG got the same position in their job
"""

plt.bar(df['recruitment_type'],df['salary'])
plt.title('type of recruitment v/s salary')
plt.xlabel('recruitment_type')
plt.ylabel('salary')
plt.legend('best')

plt.barh(df['satisfied'],df['salary'])
plt.title('satisfied v/s salary')
plt.xlabel('salary')
plt.ylabel('satisfied')
plt.legend()

"""#Lmplot"""

sns.lmplot(x='age',y='salary',data=df,hue='satisfied')

sns.lmplot(x='satisfied',y='salary',data=df,col='education')

sns.lmplot(x='satisfied',y='salary',data=df,col='education',hue='Dept',markers='d')

sns.lmplot(x='satisfied',y='salary',data=df,col='education',hue='Dept',markers='d',row='recruitment_type',fit_reg='False')

"""# Pair plot"""

sns.pairplot(df)

sns.pairplot(df,hue='Dept')

sns.kdeplot(df['salary'])

"""#Pieplot"""

plt.figure(figsize=(10,10))
df['salary'].value_counts().plot(kind='pie',autopct='%1.3f',explode=(0,.5,.6,0,0),colors=['r','g','b'])
plt.title('salary distribution')
plt.show()

plt.figure(figsize=(10,10))
df['Dept'].value_counts().plot(kind='pie',autopct='%1.3f',colors=['r','g','b'])
plt.title('Departments')
plt.show()

plt.figure(figsize=(10,10))
df['satisfied'].value_counts().plot(kind='pie',autopct='%1.3f',colors=['r','g','b'])
plt.title('Satisfaction')
plt.show()

plt.figure(figsize=(10,10))
df['certifications'].value_counts().plot(kind='pie',autopct='%1.3f',colors=['r','g','b'])
plt.title('Certified workers')
plt.show()

plt.figure(figsize=(10,10))
df['education'].value_counts().plot(kind='pie',autopct='%1.3f',colors=['r','g','b'])
plt.title('Degree level')
plt.show()

"""#Boxplot"""

sns.boxplot(df['salary'])

sns.boxplot(df['satisfied'])

"""# Conclusion of the study

* Nearly half of the people were satisfied with their job
* Both UG and PG graduates are getting same range of salary
* when we go through the department most of the people working in thr fied of purchasing
* The least no.of people working in the field of the sales
* When we go through their salary package most of them get salary in between 40k-60k
* Among them PG and UG got bigh salary in the Dept of HR through Referal
* Throug walkin PG and UG got high salry in the field of sales
* Through oncampus UG got high salry in the field of sales and PG got in the field of purchasing
* Through the agency UG got high salry in the field of purchasing and PG got in the field of sales
"""