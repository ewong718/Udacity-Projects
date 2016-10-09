#!/usr/bin/python

import sys, os
import pickle
import numpy as np


sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import test_classifier, dump_classifier_and_data

from sklearn.feature_selection import SelectKBest
from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.grid_search import GridSearchCV

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi','salary','total_payments','bonus',
                 'total_stock_value', 'expenses',
                 'exercised_stock_options','other',
                 'restricted_stock','to_messages','from_poi_to_this_person',
                 'from_messages','from_this_person_to_poi','shared_receipt_with_poi']

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers
del data_dict['THE TRAVEL AGENCY IN THE PARK']
del data_dict['TOTAL']
del data_dict['LOCKHART EUGENE E']

# impute values using median to features in list
for feature in features_list[1:]:
    feature_values = [r[feature] for r in data_dict.values() if r[feature] != 'NaN']
    median = np.median(feature_values)
    for key in data_dict:
        if data_dict[key][feature] == 'NaN':
            data_dict[key][feature] = median


			
### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
new_features = ['ratio_from_poi_email', 'ratio_to_poi_email']
features_list = features_list + new_features
for key in data_dict:
    data_dict[key]['ratio_from_poi_email'] = np.true_divide(data_dict[key]['from_poi_to_this_person'],data_dict[key]['to_messages'])
    data_dict[key]['ratio_to_poi_email'] = np.true_divide(data_dict[key]['from_this_person_to_poi'],data_dict[key]['from_messages'])

my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

#Feature Selection
trimmed_features_list = ['poi']
k = 5
select = SelectKBest(k=k)
select = select.fit(features,labels)
features = select.transform(features)
top_scores = np.sort(select.scores_)[-k:]

for i in range(len(features_list[1:])):
    if select.scores_[i] in top_scores:
        trimmed_features_list.append(features_list[1:][i])
features_list = trimmed_features_list

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

clf = GaussianNB()
#clf = SVC()

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
#from sklearn.cross_validation import train_test_split
#features_train, features_test, labels_train, labels_test = \
#    train_test_split(features, labels, test_size=0.3, random_state=42)

pipeline = make_pipeline(select, MinMaxScaler(), clf)
cv = StratifiedShuffleSplit(labels)

params = dict()
classifier_name = str(clf).split('(')[0]
   
if classifier_name == 'SVC':
    params['svc__kernel'] = ['linear']
    params['svc__C'] = [0.015625, 0.125, 1, 8, 64, 512, 4096]
    params['svc__gamma'] = [0.015625, 0.125, 1, 8, 64, 512, 4096]
	
grid_search = GridSearchCV(pipeline, param_grid=params, n_jobs=1, cv=cv)
grid_search.fit(features, labels)
clf = grid_search.best_estimator_
test_classifier(clf, my_dataset, features_list)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)