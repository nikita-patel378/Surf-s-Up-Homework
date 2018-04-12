
# coding: utf-8

# In[11]:


#Dependencies
import csv
import pandas as pd


# In[12]:


#Find the files to clean
csvfileone="Resources/hawaii_measurements.csv"
csvfiletwo="Resources/hawaii_stations.csv"


# In[13]:


#create dataframes for the files
measurements_df=pd.read_csv(csvfileone, dtype=object)
stations_df=pd.read_csv(csvfiletwo, dtype=object)


# In[14]:


#view first file
measurements_df


# In[15]:


#drop the rows that have missing values
measurements_clean_df=measurements_df.dropna(axis=0)


# In[16]:


measurements_clean_df.reset_index()


# In[17]:


#view cleaned dataframe
measurements_clean_df.reset_index().drop(['index'],axis=1)


# In[18]:


#view dataframe
stations_df


# In[19]:


#make new file for cleaned df for measurements
cleaned_data_measurements="Resources/clean_measurements_hawaii.csv"
measurements_clean_df.to_csv(cleaned_data_measurements, index=False)


# In[20]:


#I know stations didn't have any missing values, I just did this anyway
cleaned_station_data="Resources/clean_stations_hawaii.csv"
stations_df.to_csv(cleaned_station_data, index=False)

