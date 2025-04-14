import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from linearmodels import PanelOLS
import statsmodels.api as sm
from linearmodels.panel import compare

df = pd.read_excel(r'fintech_listed.xlsx', sheet_name = 'Panel Data - FS')

#################################################################
### Impact of fintech services on banks performance 2014-2019 ###
#################################################################

### Creating the subset 2014-2019
df19 = df[df['year']<2020]

### Creating indepedent variables
df19['LSIZE'] = np.log(df19['SIZE'])
vars19 = ['FS', 'BS', 'ID', 'LSIZE', 'CAP', 'LOAN', 'LLP', 'NONIN',
        'GDP', 'INF', 'Z_SCORE']

### Cleaning data
df19.drop(['beta','FS1','SIZE'], axis = 1, inplace = True)
df19 = df19.dropna()

### Set up the panel data (entity and time index)
df19 = df19[['BANK', 'year','ROA', 'ROE', 'FS', 'BS', 'ID', 'LSIZE',
              'CAP', 'LOAN', 'LLP','NONIN', 'GDP', 'INF', 'Z_SCORE']]
df19 = df19.set_index(['BANK', 'year'])

### Descriptive statistics
descriptive19 = df19.describe()
descriptive19.drop('count', axis = 0, inplace = True)
#print(descriptive19)

corr19 = (df19.drop(['ROA', 'ROE'], axis = 1, inplace = False)).corr()
#print(corr19)
cm = sns.light_palette("green", as_cmap=True)
corr19 = corr19.style.format(precision = 3).background_gradient(cmap=cm)

### Run fixed effects model
indep19 = sm.add_constant(df19[vars19])
modROA19 = PanelOLS(df19.ROA, indep19, entity_effects = True)
modROE19 = PanelOLS(df19.ROE, indep19, entity_effects = True)
feROA19 = modROA19.fit(cov_type="clustered", cluster_entity=True)
feROE19 = modROE19.fit(cov_type="clustered", cluster_entity=True)

### Table for model with ROA as dependent variable
parROA19 = (feROA19.params).to_frame()
pROA19 = (feROA19.pvalues).to_frame()
stROA19 = (feROA19.std_errors).to_frame()
tableROA19 = pd.DataFrame(parROA19.drop('parameter', axis = 1),
                          columns=['Coefficient', 'Std_Error', 'P_value'])
tableROA19 = tableROA19.assign(Coefficient = parROA19).assign(Std_Error = stROA19).assign(P_value = pROA19)

### Table for model with ROE as dependent variable
parROE19 = (feROE19.params).to_frame()
pROE19 = (feROE19.pvalues).to_frame()
stROE19 = (feROE19.std_errors).to_frame()
tableROE19 = pd.DataFrame(parROE19.drop('parameter', axis = 1),
                          columns=['Coefficient', 'Std_Error', 'P_value'])
tableROE19 = tableROE19.assign(Coefficient = parROE19).assign(Std_Error = stROE19).assign(P_value = pROE19)

comp19 = compare((feROA19, feROE19), stars = True)
#print(comp19)

#################################################################
### Impact of fintech services on banks performance 2014-2021 ###
#################################################################

### Creating independent variables
df['DUMMY'] = df.year.map({2020:1, 2021:1, 2019:0, 2018:0, 2017:0,2016:0, 2015:0, 2014:0})
df['LSIZE'] = np.log(df['SIZE'])
vars = ['FS', 'DUMMY', 'BS', 'ID', 'LSIZE', 'CAP', 'LOAN', 'LLP', 'NONIN',
        'GDP', 'INF', 'Z_SCORE']

### Cleaning data
df.drop(['beta','FS1','SIZE'], axis = 1, inplace = True)
df = df.dropna()

### Set up the panel data (entity and time index)
df = df[['BANK', 'year','ROA', 'ROE', 'FS', 'DUMMY', 'BS', 'ID', 'LSIZE', 'CAP', 'LOAN', 
         'LLP','NONIN', 'GDP', 'INF', 'Z_SCORE']]
df = df.set_index(['BANK', 'year'])

### Descriptive statistics
descriptive = df.describe()
descriptive.drop('count', axis = 0, inplace = True)
#print(descriptive)

corr = (df.drop(['ROA', 'ROE'], axis = 1, inplace = False)).corr()
#print(corr)
cm = sns.light_palette("green", as_cmap=True)
corr = corr.style.format(precision = 3).background_gradient(cmap=cm)

### Run fixed effects model
indep = sm.add_constant(df[vars])
modROA = PanelOLS(df.ROA, indep, entity_effects = True)
modROE = PanelOLS(df.ROE, indep, entity_effects = True)
feROA = modROA.fit(cov_type="clustered", cluster_entity=True)
feROE = modROE.fit(cov_type="clustered", cluster_entity=True)

### Table for model with ROA as dependent variable
parROA = (feROA.params).to_frame() # coefficients
pROA = (feROA.pvalues).to_frame() # p_values
stROA = (feROA.std_errors).to_frame() # standard deviations
tableROA = pd.DataFrame(parROA.drop('parameter', axis = 1),
                        columns=['Coefficient', 'Std_Error', 'P_value'])
tableROA = tableROA.assign(Coefficient = parROA).assign(Std_Error = stROA).assign(P_value = pROA)

### Table for model with ROE as dependent variable
parROE = (feROE.params).to_frame() # coefficients
pROE = (feROE.pvalues).to_frame() # p_values
stROE = (feROE.std_errors).to_frame() # standard deviations
tableROE = pd.DataFrame(parROE.drop('parameter', axis = 1),
                        columns=['Coefficient', 'Std_Error', 'P_value'])
tableROE = tableROE.assign(Coefficient = parROE).assign(Std_Error = stROE).assign(P_value = pROE)

comp21 = compare((feROA, feROE), stars = True)
#print(comp21)
