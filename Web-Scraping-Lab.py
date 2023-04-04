#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2022-01-01" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **Hands-on Lab : Web Scraping**
# 

# Estimated time needed: **30 to 45** minutes
# 

# ## Objectives
# 

# In this lab you will perform the following:
# 

# * Extract information from a given web site 
# * Write the scraped data into a csv file.
# 

# ## Extract information from the given web site
# You will extract the data from the below web site: <br> 
# 

# In[3]:


#this url contains the data you need to scrape
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"


# The data you need to scrape is the **name of the programming language** and **average annual salary**.<br> It is a good idea to open the url in your web broswer and study the contents of the web page before you start to scrape.
# 

# Import the required libraries
# 

# In[4]:


# Your code here
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page


# Download the webpage at the url
# 

# In[5]:


#your code goes here
# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text 


# Create a soup object
# 

# In[7]:


#your code goes here
soup = BeautifulSoup(data,'html.parser')  # create a soup object using the variable 'data'


# Scrape the `Language name` and `annual average salary`.
# 

# In[12]:


#your code goes here
#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>

#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    l_name = cols[1].getText() # store the value in column 1 as l_name
    l_salary = cols[3].getText() # store the value in column 3 as l_salary
    print("{}--->{}".format(l_name,l_salary))


# Save the scrapped data into a file named *popular-languages.csv*
# 

# In[18]:


# your code goes here
# create empty lists to hold the values for each column
l_name = []
l_salary = []

# Get all rows from the table
for row in table.find_all('tr'): 
    # Get all columns in each row.
    cols = row.find_all('td')
    # append the value in column 1 to l_name
    l_name.append(cols[1].getText()) 
    # append the value in column 3 to l_salary
    l_salary.append(cols[3].getText())

# create a new DataFrame with the two columns
df = pd.DataFrame({'Language name': l_name, 'Average Annual Salary': l_salary})

df.to_csv('popular-languages.csv', index=False)


# ## Authors
# 

# Ramesh Sannareddy
# 

# ### Other Contributors
# 

# Rav Ahuja
# 

# ## Change Log
# 

# |  Date (YYYY-MM-DD) |  Version | Changed By  |  Change Description |
# |---|---|---|---|
# | 2020-10-17  | 0.1  | Ramesh Sannareddy  |  Created initial version of the lab |
# 

#  Copyright &copy; 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2022-01-01).
# 
