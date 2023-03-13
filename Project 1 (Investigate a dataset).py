#!/usr/bin/env python
# coding: utf-8

# # Project: No-show Medical Appointment Data Analysis
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# This project analyzes medical appointment data collected from over 100k patients in Brazil. The primary focus will be whether a patient shows up for their appointment. Additionally, variables from the dataset, such as scholarship, hypertension, diabetes, alcoholism, and handicap, will be analyzed to better understand the dataset.

# **Dependent Variable**
# * No Show

# **Independent Variables**
# * Age
# * Gender

# **Question of Analysis**
# * What is the interpretation of all variables
# * What are the major variable influencing patient presence for their appointment.

# In[405]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# ### General Properties

# In[406]:


df = pd.read_csv('no_show_appointments.csv')
df.head()


# In[407]:


df.shape


# In[408]:


df.describe()


# ## Data Cleaning

# In[409]:


df = df.rename(columns = {'No-show':'No_show', 'Handcap':'Handicap', 'Hipertension': 'Hypertension'})


# In[410]:


df.info()


# In[411]:


df.drop([ 'AppointmentID', 'ScheduledDay', 'AppointmentDay'], axis = 1, inplace = True)


# In[412]:


df.head()


# In[413]:


# Unique values in each column
print('Gender:', df.Gender.unique())
print('Neighbourhood: ', df.Neighbourhood.unique())
print('Scholarship: ', df.Scholarship.unique());
print('Hypertension: ', df.Hypertension.unique());
print('Diabetes: ', df.Diabetes.unique())
print('Alcoholism: ', df.Alcoholism.unique())
print('Handicap: ', df.Handicap.unique())
print('SMS_received: ', df.SMS_received.unique())
print('No_show: ', df.No_show.unique())


# In[414]:


df[df.duplicated() == True].count()


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# 

# **1) What is the interpretation of all variables**

# In[415]:


df.hist(figsize=(14,10));


# * Discussion: 
# The histogram plot for hypertensive and diabetes patients shows that the number of hypertensive patients is much compared to diabetes. The histogram showing the number of patients that received an SMS shows that most patients did not receive an SMS regarding their appointment. It can also be observed from the histogram plot for alcohol patients that only a few amounts of patients consume alcohol. Most patients are between the age group of 0–10, and the age distribution is skewed to the right, implying that the mean and median are both less than the mode. Compared to the total 110527 patients investigated, about 100,000 are not on scholarship. Finally, most patients are not handicapped, and only a minute of them are labelled 1.

# **2) What are the major variable influencing patient presence for their appointment.**

# **Determining the percentage of patients that showed up for their appointment**

# In[416]:


ValueCount = df['No_show'].value_counts()
ValueCount


# In[417]:


TotalCount = df['No_show'].count()
TotalCount


# In[418]:


def percentage(par1,par2):
    percent = (par1/par2)*100
    return percent


# In[419]:


percentage(ValueCount,TotalCount)


# * Discussion: It can be observed that approximately 80% of the patients that booked an appointment showed up, whereas approximately 20% did not show up for their appointments. 

# **Determining why 20% of the patients did not show up for their appointments**

# * **Age**

# *Grouping the ages into five categories (Children, Early working age, Prime working age, Mature working age, and Elderly)*

# In[420]:


bins = [0, 14, 24, 54, 64, 115] 
labels = ['Children', 'Early working age', 'Prime working age', 'Mature working age','Elderly']
df['AgeGroup'] = pd.cut(df['Age'], bins, labels=labels)
df.head()


# In[421]:


df.groupby(['AgeGroup'])['No_show'].count()


# In[422]:


df.groupby(['AgeGroup'])['No_show'].count()
df.groupby('AgeGroup')['No_show'].value_counts().unstack().plot(kind='bar',figsize=(10,8))
plt.title('No show based on age group')
plt.xlabel('Age Group')
plt.ylabel('Number of Patients');
plt.show()


# * Discussion: It can be observed form the bar chart that most of the patients who showed and did not show-up for their appointment were about 34500 and 9500, repectively, and they all fall in the prime working age.

# * **Gender**

# In[423]:


GenderCount = df.groupby(['Gender'])['No_show'].count()
GenderCount


# In[424]:


TotalGender = df['Gender'].count()
TotalGender


# In[425]:


percentage(GenderCount,TotalGender)


# In[426]:


df.groupby('Gender')['No_show'].value_counts().unstack().plot(kind='bar',figsize=(8,6))
plt.title('No show based on gender')
plt.xlabel('Gender')
plt.ylabel('Number of Patients');
plt.show()


# * Discussion: It can be observed that based on the number of patients who showed and did not show-up for their appointments, 65%  are female while 35% are male. Additionally, of the 65% of the females, about 58000 patients showed-up whereas about 13000 patients did not show up.

# * **SMS_recieved**

# In[427]:


SMSReceivedCount = df.groupby(['SMS_received'])['No_show'].count()
SMSReceivedCount


# In[428]:


TotalSMSReceived = df['SMS_received'].count()
TotalSMSReceived


# In[429]:


percentage(SMSReceivedCount,TotalSMSReceived)


# In[430]:


df.groupby('SMS_received')['No_show'].value_counts().unstack().plot(kind='bar',figsize=(8,6))
plt.title('No show based on SMS_received')
plt.xlabel('SMS_received')
plt.ylabel('Number of Patients');
plt.show()


# * Discussion : It can be observed that about 68% of the patients did not recieve SMS regarding their apppointment while 32% did. Additionally, of the 68% of patients that did not receive an SMS, about 62000 patients showed up for their appointment while about 12000 did not.  

# <a id='conclusions'></a>
# ## Conclusions
# 
# This project analyzes medical appointment data collected from over 100k patients in Brazil. Variables such as gender, age, scholarship,	hypertension, diabetes, alcoholism, handicap, SMS_received, and No_show were analyzed. The following conclusion can be made as follows:
# * About 80% of patients who booked an appointement showed-up for their appiontments
# * Most of the patients who showed-up for their appointment fall in the prime working age, i.e., between age 24 and 54
# * Most of the patients who showed and did not show-up for their appointments are females, which are about 65%. Additionally, of the 65% of the females, about 58000 patients showed-up whereas about 13000 patients did not show up.
# * Most patients did not receive an SMS regarding their appointments; however, they still showed-up for their appointment. 

# ## Limitation

# The main limitation in this project is the inconsistent SMS reminders sent to patients for their appointments, which undoubtedly contributed to the patients' absences.
