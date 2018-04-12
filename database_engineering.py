
# coding: utf-8

# In[49]:


#Dependencies
import csv
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Text, Float


# In[50]:


#the files to read
csvfileone="Resources/clean_measurements_hawaii.csv"
csvfiletwo="Resources/clean_stations_hawaii.csv"


# In[51]:


#creating dataframes for the files
measurements_df=pd.read_csv(csvfileone, dtype=object)
stations_df=pd.read_csv(csvfiletwo, dtype=object)


# In[52]:


measurements_df.head()


# In[53]:


stations_df.head()


# In[54]:


#create an engine
engine=create_engine("sqlite:///hawaii.sqlite")


# In[55]:


conn= engine.connect()


# In[56]:


Base = declarative_base()

class Measurement(Base):
    __tablename__ = "measurements"
    
    id = Column(Integer, primary_key = True)
    station = Column(Text)
    date=Column(Text)
    prcp=Column(Float)
    tobs=Column(Integer)


# In[57]:


class Station(Base):
    __tablename__= "stations"
    id = Column(Integer, primary_key = True)
    station = Column(Text)
    name = Column(Text)
    latitude=Column(Float)
    longitude=Column(Float)
    elevation=Column(Integer)


# In[58]:


Base.metadata.create_all(engine)


# In[59]:


new_measure_df=pd.read_csv("Resources/clean_measurements_hawaii.csv")


# In[60]:


measure_data=new_measure_df.to_dict(orient='records')


# In[61]:


print(measure_data[:5])


# In[62]:


metadata= MetaData(bind=engine)
metadata.reflect()


# In[63]:


table = sqlalchemy.Table('measurements', metadata, autoload=True)


# In[64]:


conn.execute(table.delete())


# In[65]:


conn.execute(table.insert(), measure_data)


# In[66]:


new_station_df=pd.read_csv("Resources/clean_stations_hawaii.csv")


# In[67]:


station_data=new_station_df.to_dict(orient='records')


# In[68]:


print(station_data[:5])


# In[69]:


metadata_station=MetaData(bind=engine)
metadata_station.reflect()


# In[70]:


table_station= sqlalchemy.Table('stations', metadata_station, autoload=True)


# In[71]:


conn.execute(table_station.delete())


# In[72]:


conn.execute(table_station.insert(), station_data)

