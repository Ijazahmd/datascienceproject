# -*- coding: utf-8 -*-
"""Stress level .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Stg-VUTMAwnhk7A72XbnSDcVur9zoPTv

# Students Stress Level
* In this dataset we can discuss about the stress level of students
* The stress level is measured on the basis of anxiety level,self esteem,depression,headache,blood pressure etc.
"""

import pandas as pd
import numpy as np

data=pd.read_csv("/content/drive/MyDrive/Data science project/project-2,ML/StressLevelDataset.csv")
data.head()

data.shape



data.isna().any()

data.dtypes

data.duplicated().sum()

import seaborn as sns
import matplotlib.pyplot as plt

data['noise_level'].unique()

data['stress_level'].unique()

data.info()

sns.barplot(x="sleep_quality",y="stress_level",data=data)

numerical_features=['anxiety_level','self_esteem', 'mental_health_history','depression',  'headache','blood_pressure','sleep_quality', 'breathing_problem','noise_level','living_conditions','safety','basic_needs','academic_performance','study_load','teacher_student_relationship','future_career_concerns',  'social_support','peer_pressure','extracurricular_activities','bullying', 'stress_level']

plt.figure(figsize=(15,15))
correlation_matrix = data[numerical_features].corr()
sns.heatmap(correlation_matrix,annot=True,cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

x=data['peer_pressure']
y=data['stress_level']
sns.barplot(x='peer_pressure',y='stress_level',data=data)
plt.show()

col=['anxiety_level', 'self_esteem', 'mental_health_history', 'depression',
        'blood_pressure', 'sleep_quality', 'breathing_problem',
        'safety',
       'academic_performance', 'study_load', 'teacher_student_relationship',
       'future_career_concerns', 'social_support', 'peer_pressure',
        'bullying']

for i in col:

    plt.figure(figsize=(10,10))
    sns.barplot(data=data, x=i, y='stress_level')
    plt.title('Distribution of {}'.format(col))
    plt.xlabel(i)
    plt.ylabel('stress_level')
    plt.xticks(rotation=0)
    plt.show()

data.columns

"""#**Data Preprocessing**"""

#splitting data in to input and output
x=data.drop(['stress_level'],axis=1)
y=data['stress_level']

x.head()

y.head()

"""#**Standard scalar**"""

from sklearn.preprocessing import StandardScaler
std= StandardScaler()

x = std.fit_transform(x)
x

x.shape

"""#**Splitting the datas for training and testing**"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.20,random_state=0)

x_train.shape

x_test.shape

"""#**MODEL BUILDING**

**Classification Algorithm**
1. **K-Nearest Neighbor (KNN)**

2. **Naive-Bayes**

3. **Support Vector Machine**

4. **Decision Tree**

5. **Random Forest**

6. **Ada Boost**

7. **XG Boost**

8. **Logistic regression**

Classification Algorithms
1. K-NEAREST NEIGHBOR (KNN)

K-Nearest Neighbour is one of the simplest Machine Learning algorithms based on Supervised Learning technique.It is used for classification and regression.
K-NN algorithm stores all the available data and classifies a new data point based on the similarity. This means when new data appears then it can be easily classified into a well suite category by using K-NN algorithm.
2. GAUSSIAN NAIVE BAYES

* This type of Naive Bayes is used when variables are continuous in nature.

* It assumes that all the variables have a normal distribution. So if you have some variables which do not have this property, you might want to transform them to the features having distribution normal.

* Normal distribution also known as the Gaussian distribution is a probability distribution that is symmetric about the mean, showing that data near the mean are more frequent in occurence than data far from the mean.
3. BERNOULLI NAIVE BAYES

* This is used when features are binary. So instead of using the frequency of the word, if you have discrete features in 1s and 0s that represent the presence or absence of a feature. In that case, the features will be binary and will use Bernoulli Naive Bayes.
4. SUPPORT VECTOR MACHINE

* Support Vector Machine or SVM is one of the most popular Supervised Learning algorithms, which is used for Classification as well as Regression problems.
The goal of the SVM algorithm is to create the best line or decision boundary that can segregate n-dimensional space into classes so it is easy to put the new data point in the correct category in the future. This best decision boundary is called a hyperplane.
5. DECISION TREE

* A decision tree is one of the most powerful tools of supervised learning algorithms used for both classification and regression tasks.
It builds a flowchart-like tree structure where each internal node denotes a test on an attribute, each branch represents an outcome of the test, and each leaf node (terminal node) holds a class label.
6. RANDOM FOREST

* Random forests or random decision forests is an ensemble learning method for classification, regression and other tasks that operates by constructing a multitude of decision trees at training time.
For classification tasks, the output of the random forest is the class selected by most trees.
7. ADA BOOST

* Ada Boost is an ensemble learning method. We use boosting for combining weak learners with high bias. Boosting aims to produce a model with a lower bias than that of the individual models.
8. XG BOOST

* XG Boost is an ensemble learning method. We use boosting for combining weak learners with high bias. Boosting aims to produce a model with a lower bias than that of the individual models.
9. LOGISTIC REGRESSION

* Logistic Regression is one of the most popular Machine Learning algorithms, which comes under the Supervised Learning technique. It is used for predicting the categorical dependent variable using a given set of independent variables.
Logistic regression predicts the output of a categorical dependent variable. Therefore the outcome must be a categorical or discrete value. It can be either Yes or No, 0 or 1, true or False, etc. but instead of giving the exact value as 0 and 1, it gives the probabilistic values which lie between 0 and 1.

PERFORMANCE EVALUATION
* Accuracy performance metrics can be decisive when dealing with imbalanced data. In this blog, we will learn about the Confusion matrix and its associated terms, which looks confusing but are trivial. The confusion matrix, precision, recall, and F1 score gives better intuition of prediction results as compared to accuracy.

Confusion Matrix:
* It is a matrix of size 2×2 for binary classification with actual values on one axis and predicted on another.

Accuracy Score:
* Accuracy is the measure of correct predictions made by our model. It is equal to the number of correct predictions made upon total number of predictions made by the model.

Precision Score:

* It is defined as the ratio of true positives to the sum of true and false positives. It is also known as Positive Predictive Value (PPV).

Recall Score:
* It is defined as the ratio of true positives to the sum of true positives and false negatives. It is also called True Positive Rate (TPR) or sensitivity.

F1 score:
* It is the weighted harmonic mean of precision and recall. The closer the value of the F1 score is to 1.0 , the better the expected performance of the model is.
"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC
from sklearn.tree import  DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression

"""**1. KNN**
* K-Nearest Neighbour is one of the simplest Machine Learning algorithms based on Supervised Learning technique.It is used for classification and regression. K-NN algorithm stores all the available data and classifies a new data point based on the similarity. This means when new data appears then it can be easily classified into a well suite category by using K-NN algorithm.
"""

model= KNeighborsClassifier(n_neighbors=5)

model.fit(x_train,y_train)

y_pred1=model.predict(x_test)

y_pred1

#confusion matrix
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
result = confusion_matrix(y_test,y_pred1)
print(result)
labels=[0,1,2]
cmd = ConfusionMatrixDisplay(result,display_labels=labels)

cmd.plot()

# Accuracy score and classification report

from sklearn.metrics import accuracy_score,classification_report
print('Accuracy: ',accuracy_score(y_test,y_pred1)*100,'\n')
print(classification_report(y_test,y_pred1))

training_score= model.score(x_train,y_train)
training_score

testing_score= model.score(x_test,y_test)
testing_score

"""**2) Naive Bayes : GaussianNB**
* his type of Naive Bayes is used when variables are continuous in nature.

* It assumes that all the variables have a normal distribution. So if you have some variables which do not have this property, you might want to transform them to the features having distribution normal.

* Normal distribution also known as the Gaussian distribution is a probability distribution that is symmetric about the mean, showing that data near the mean are more frequent in occurence than data far from the mean.


"""

nb = GaussianNB()
nb.fit(x_train,y_train)
y_pred2=nb.predict(x_test)

y_pred2

from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
result = confusion_matrix(y_test,y_pred2)
print(result)
labels=[0,1,2]
cmd = ConfusionMatrixDisplay(result,display_labels=labels)

cmd.plot()

#Accuracy score and classification report
from sklearn.metrics import accuracy_score,classification_report
print('Accuracy: ',accuracy_score(y_test,y_pred2)*100,'\n')
print(classification_report(y_test,y_pred2))

training_score= nb.score(x_train,y_train)
training_score

testing_score= nb.score(x_test,y_test)
testing_score

"""**Naive Bayes : BernoulliNB**
* This is used when features are binary. So instead of using the frequency of the word, if you have discrete features in 1s and 0s that represent the presence or absence of a feature. In that case, the features will be binary and will use Bernoulli Naive Bayes.
"""

nb_model2=BernoulliNB()
nb_model2.fit(x_train,y_train)
y_pred3=nb_model2.predict(x_test)
y_pred3

#confusion matrix

from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
result = confusion_matrix(y_test,y_pred3)
print(result)
labels=[0,1,2]
cmd = ConfusionMatrixDisplay(result,display_labels=labels)

# Accuracy score and classification report

from sklearn.metrics import accuracy_score,classification_report
print('Accuracy: ',accuracy_score(y_test,y_pred3)*100,'\n')

print(classification_report(y_test,y_pred3))

training_score= nb_model2.score(x_train,y_train)
training_score

testing_score= nb_model2.score(x_test,y_test)
testing_score

"""**3) Support Vector Machine Algorithm(SVM)**
* Support Vector Machine or SVM is one of the most popular Supervised Learning algorithms, which is used for Classification as well as Regression problems. The goal of the SVM algorithm is to create the best line or decision boundary that can segregate n-dimensional space into classes so it is easy to put the new data point in the correct category in the future. This best decision boundary is called a hyperplane
"""

svc=SVC()
svc.fit(x_train,y_train)
y_pred4=svc.predict(x_test)

y_pred4

#confusion matrix

from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
result = confusion_matrix(y_test,y_pred4)
print(result)
labels=[0,1,2]
cmd = ConfusionMatrixDisplay(result,display_labels=labels)

cmd.plot()

# Accuracy score and classification report

from sklearn.metrics import accuracy_score,classification_report
print('Accuracy: ',accuracy_score(y_test,y_pred4)*100,'\n')

print(classification_report(y_test,y_pred4))

training_score= svc.score(x_train,y_train)
training_score

testing_score= svc.score(x_test,y_test)
testing_score

"""**4) Decision tree**
* A decision tree is one of the most powerful tools of supervised learning algorithms used for both classification and regression tasks. It builds a flowchart-like tree structure where each internal node denotes a test on an attribute, each branch represents an outcome of the test, and each leaf node (terminal node) holds a class label.
"""

dt=DecisionTreeClassifier()
dt.fit(x_train,y_train)

y_pred5 = dt.predict(x_test)
y_pred5

#confusion matrix

from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
result = confusion_matrix(y_test,y_pred5)
print(result)
labels=[0,1,2]
cmd = ConfusionMatrixDisplay(result,display_labels=labels)

# Accuracy score and classification report

from sklearn.metrics import accuracy_score,classification_report
print('Accuracy: ',accuracy_score(y_test,y_pred5)*100,'\n')

print(classification_report(y_test,y_pred5))

training_score= dt.score(x_train,y_train)
training_score

testing_score= dt.score(x_test,y_test)
testing_score

"""**5) Random Forest**
* Random forests or random decision forests is an ensemble learning method for classification, regression and other tasks that operates by constructing a multitude of decision trees at training time. For classification tasks, the output of the random forest is the class selected by most trees
"""

rfc = RandomForestClassifier(n_estimators=20,criterion='gini',max_depth=5,max_features=5)
rfc.fit(x_train,y_train)
y_pred6 = rfc.predict(x_test)
y_pred6

#confusion matrix

from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
result = confusion_matrix(y_test,y_pred6)
print(result)
labels=[0,1,2]
cmd = ConfusionMatrixDisplay(result,display_labels=labels)

cmd.plot()

# Accuracy score and classification report

from sklearn.metrics import accuracy_score,classification_report
print('Accuracy: ',accuracy_score(y_test,y_pred6)*100,'\n')

print(classification_report(y_test,y_pred6))

training_score= rfc.score(x_train,y_train)
training_score

testing_score= rfc.score(x_test,y_test)
testing_score

"""6) **Ada Boost**
* Ada Boost is an ensemble learning method. We use boosting for combining weak learners with high bias. Boosting aims to produce a model with a lower bias than that of the individual models
"""

abc_model = AdaBoostClassifier(n_estimators=10,learning_rate=1.0)
abc_model.fit(x_train,y_train)
y_pred7=abc_model.predict(x_test)
y_pred7

#confusion matrix

from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
result=confusion_matrix(y_test,y_pred7)
print(result)
labels=[0,1,2]
cmd=ConfusionMatrixDisplay(result,display_labels=labels)

#accuracy score and classification report

from sklearn.metrics import accuracy_score,classification_report
print('Accuracy',accuracy_score(y_test,y_pred7)*100,'\n')
print(classification_report(y_test,y_pred7))

training_score = abc_model.score(x_train,y_train)
training_score

testing_score = abc_model.score(x_test,y_test)
testing_score

"""**7) XG Boost**
* XG Boost is an ensemble learning method. We use boosting for combining weak learners with high bias. Boosting aims to produce a model with a lower bias than that of the individual models.
"""

xgb_model = XGBClassifier()
xgb_model.fit(x_train,y_train)

y_pred8 = xgb_model.predict(x_test)
y_pred8

#confusion matrix

from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
result=confusion_matrix(y_test,y_pred8)
print(result)
labels=[0,1,2]
cmd=ConfusionMatrixDisplay(result,display_labels=labels)

#accuracy score and classification report

from sklearn.metrics import accuracy_score,classification_report
print('Accuracy',accuracy_score(y_test,y_pred8)*100,'\n')
print(classification_report(y_test,y_pred8))

training_score = xgb_model.score(x_train,y_train)
training_score

testing_score = xgb_model.score(x_test,y_test)
testing_score

"""**8) Logistic Regression**
* Logistic Regression is one of the most popular Machine Learning algorithms, which comes under the Supervised Learning technique. It is used for predicting the categorical dependent variable using a given set of independent variables. Logistic regression predicts the output of a categorical dependent variable. Therefore the outcome must be a categorical or discrete value. It can be either Yes or No, 0 or 1, true or False, etc. but instead of giving the exact value as 0 and 1, it gives the probabilistic values which lie between 0 and 1.
"""

lr_model = LogisticRegression()
lr_model.fit(x_train,y_train)

y_pred9 = lr_model.predict(x_test)
y_pred9

#confusion matrix

from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
result=confusion_matrix(y_test,y_pred9)
print(result)
labels=[0,1,2]
cmd=ConfusionMatrixDisplay(result,display_labels=labels)

#accuracy score and classification report

from sklearn.metrics import accuracy_score,classification_report
print('Accuracy',accuracy_score(y_test,y_pred9)*100,'\n')
print(classification_report(y_test,y_pred9))

training_score = lr_model.score(x_train,y_train)
training_score

testing_score = lr_model.score(x_test,y_test)
testing_score

"""#**Observation**

* From the above models we can see that svm algorithm got the highest accuracy score.
* accuracy score = 89.54
* f1.score - 0.89,0.93,0.83
* training score = 0.9727
* testing score = 0.8954

#**HYPER PARAMETER TUNING**
* Hyperparameters are adjustable parameters used to obtain an optimum model.
* Hyper parameter tuning refers to thr process of choosing the optimum set of hyper parameters for a machine learning model.
* Here we use the RandomSearchCV as the hyper parameter
* In randon search cv the machine select the random combinations of parameters to build the model and select the best parameter combination from it.
"""

from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint as sp_randint
svc=SVC()

help(svc)

param_dist = {'gamma':  'auto', 'kernel': 'rbf'}

randomCV = RandomizedSearchCV(svc, param_distributions=param_dist,cv=5)
randomCV.fit(x_train, y_train)

randomCV.best_params_

svc_model = SVC(gamma='auto', kernel='rbf')

svc_model.fit(x_train,y_train)

y_pred_ = svc_model.predict(x_test)

y_pred_

#accuracy score and classification report

from sklearn.metrics import accuracy_score,classification_report

print('Accuracy',accuracy_score(y_test,y_pred_)*100,'\n')
print(classification_report(y_test,y_pred_))

training_score = svc_model.score(x_train,y_train)
training_score

testing_score = svc_model.score(x_test,y_test)
testing_score

"""#**Prediction with new values :**"""

input_values =[[1,2,3,1,2,3,1,2,4,1,2,3,4,1,2,3,4,5,1,2]]

input_array = np.array(input_values).reshape(1, -1)
svc_model.predict(input_values)

"""#**Conclusion**

So, in conclusion we studied the dataset on the topic student stress level. Here we analysed features of the dataset that depends the stress level. And with the various machine learning algorithm we checked the accuracy score and selected a algorithm which gives more accuracy, here it is the support vector machine with a accuracy score of 89.54
"""