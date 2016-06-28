
# coding: utf-8

# # Homework 09
# ### Zhizhou Wang
# ### Jun 20, 2016

# In[7]:

import pandas as pd


# In[14]:

earthquakes_df = pd.read_csv("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.csv")


# In[13]:

eq.head(2)


# In[15]:

earthquakes = earthquakes_df.to_dict('records')


# ### Small functions

# In[18]:

def depth_to_words(dep):
    if dep <= 70:
        return ("shallow")
    elif 70< dep <= 300:
        return ("intermediate")
    elif 300 < dep <= 700:
        return ("deep")


# In[19]:

def magnitude_to_words(mag):
    if 0<= mag <= 4:
        return("easily ignored",mag)
    elif 4 < mag <= 6:
        return("major",mag)
    elif 6 < mag <= 7:
        return('huge',mag)
    elif 7< mag <= 9:
        return("very destructive",mag)
    else:
        return("incredible desaster",mag)


# In[21]:

get_ipython().system('pip install dateutils')


# In[53]:

import dateutil.parser
timestring = '2014-06-04T11:58:58.200Z'
yourdate = dateutil.parser.parse(timestring)
print("The hour is", yourdate.hour)
print("We can do things with strftime like", print(yourdate.strftime("%b %d")))
print(yourdate.strftime('%A'))


# In[35]:

def day_in_words(day):
    return day.strftime('%A')


# In[57]:

def date_in_words(date):
    return date.strftime('%b %d')


# In[46]:

def time_in_words(time):
    if 6<= int(time.strftime('%H')) <= 12:
        return('morning')
    elif 12< int(time.strftime('%H')) < 18:
        return("afternoon")
    elif 18<= int(time.strftime('%H')) <= 20:
        return("evening")
    else:
        return("night")


# In[55]:

def eq_to_sentence(eq):
    print("A",depth_to_words(eq['depth']),",",magnitude_to_words(eq['mag']),eq['mag'],"magnitude earthquake was reported",day_in_words(date),time_in_words(date),"on",date_in_words(date),eq['place'],".")


# In[64]:

for eq in earthquakes:      
    date = dateutil.parser.parse(eq['time'])
    if eq['type'] == 'earthquake':
        if eq['mag'] >= 4.0:
            eq_to_sentence(eq)
    else:
        print('There was also a magnitude',eq['mag'],eq['type'],eq['place'])


# In[ ]:



