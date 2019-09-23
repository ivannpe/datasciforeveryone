#!/usr/bin/env python
# coding: utf-8

# -  Ivanna Pena
# -  In this assignment, I will locate a dataset of something I am interested in and analyze it in table form and visualizations

# # Pre-step: I am generally interested in:
# -   Describe broadly what topic you’re interested in.
#      -  I am very interested in topics of social justice, specifically the way marginalized communities are treated disproportionatly, and unjustly in America.
# -  Share why you’re interested in that topic.
#     -  I care about that topic because institutionalized racism has led to unjust practices, loopholes in legislation, and unnacountability for the actions of people of certain demographics. This is specifically because of the inception of the #BlackLivesMatter movement following the shooting of Michael Brown, and all of the other lives that were unjustly ended, and continue to end due to police brutality, and the lack of accountability for the officers that commit these crimes.
# -  Describe specifically what you’d like to discover.
#     -  I would like to discover the correlation between police brutality in America and characteristics of the victims. 

# # Dataset
# -  Describe the type of data you'd like
#       -   I would like a data set that includes data about police brutality in America in the last few years, that also includes demographic information about the victims of that brutality.
# -  Describe what process of looking for it was like
#       -  Looking for a dataset that matched topics I was interested was difficult. I had to end up narrowing my topic based on data available. Finding datasets that had enough variables, and covered a long enough time frame to be able to properly deduce a conclusion, and that were publicly available was a difficult tast.
# -  Describe the dataset you ultimately chose and why. Include a link to the dataset.
#       -  I ended up choosing a database compiled by The Washington Post that includes every fatal shooting in the US (4463) by a police officer from 2015 to 2019. It also includes information, descriptions and other important data about the victim. I chose this data set because of how much information there was, both the number of shootings documented, as well as the amount of information about each victim. 
#    
# -  https://github.com/washingtonpost/data-police-shootings/blob/master/fatal-police-shootings-data.csv
# -  https://raw.githubusercontent.com/washingtonpost/data-police-shootings/master/fatal-police-shootings-data.csv
# -  https://www.washingtonpost.com/graphics/2019/national/police-shootings-2019/?utm_term=.4cd1ae1dfc61

# In[42]:


from datascience import *
import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plots
import numpy as np
data = 'https://raw.githubusercontent.com/washingtonpost/data-police-shootings/master/fatal-police-shootings-data.csv'
policeshootings = Table.read_table(data)
print("Number of Observations: " , policeshootings.num_rows)
print("Number of Variables: " , policeshootings.num_columns)


# # Features of the dataset
# -  How was it collected?
#    -  The Washington Post collects this data by "culling local news reports, law enforcement websites and social media and by monitoring independent databases such as Killed by Police and Fatal Encounters." The data set only includes "shootings in which a police officer, in the line of duty, shot and killed a civilian...The Post is not tracking deaths of people in police custody, fatal shootings by off-duty officers or non-shooting deaths."
# -  Who was it collected by and for what?
#     -  It is collected by The Washington Post because many data sets, even of the FBI on this topic are incomplete, and after the "2014 killing of Michael Brown in Ferguson, Mo., which began the protest movement culminating in Black Lives Matter and an increased focus on police accountability nationwide"
# -  What do the rows and columns represent in the context of this dataset?
#     -  The rows in this data set are victims of these fatal police shooting, and the columns are different characteristics of the shooting such as whether or not the victim was armed, their age, gender, race, location of shooting, signs of mental illness, threat level, whether or not the victim was fleeing, and whether the police officer had a body camera.
# -  How many observations and variables are there?
#     -  There are 4054 observations and 14 columns.
# -  What do you think are some weaknesses of the dataset?
#     -  Some weaknesses of this dataset include the fact that it is limited to a specific type of police brutality, and even the fact that it is limited to a specific kind of police shooting. I think the lack of specificity of where the data comes from, and the inability to verify the data is also a weakness

# # Analysis : Tables
# -  Construct three tables showing features of the dataset that are illuminating of your original question(s).
# -  They can generally be anything you like as long as they’re useful for you.
# -  The only rules are: (1) at least one table must include a new variable you construct, and (2) you have to do something to it (e.g., you can’t just show the dataset).
# -  For each, discuss why you chose that manipulation and what you learned from the result.

# In[78]:


#name, date, manner_of_death, armed(unarmed), age(under 18),
#gender(M, F), race, signs_of_mental_illness(True , False)
#threat_level(attack, other, undetermined), flee(Not fleeing, Car, Foot)

policeshootings = policeshootings.select('name','date','race',
                                         'city','state',
                                         'armed','age',
                                         'gender','race',
                                         'signs_of_mental_illness',
                                         'threat_level','flee')
blackunarmed = (policeshootings.where('race',are.equal_to('B'))
                               .where('armed',are.not_equal_to('armed')))
pctblackunarmed = (blackunarmed.num_rows / policeshootings.num_rows)*100
nonwhite = policeshootings.where('race',are.not_equal_to('W'))
pctnonwhite = (nonwhite.num_rows /policeshootings.num_rows)*100
under18 = policeshootings.where('age',are.below_or_equal_to(18))
pctunder18 = (under18.num_rows / policeshootings.num_rows)*100 
nonwhitevictims = (
    Table().with_columns("Number of Shootings", policeshootings.num_rows,
                         "Percent Non-White Victims", pctnonwhite, 
                         "Percent Black Unarmed Victims",pctblackunarmed,
                          "Percent Under 18",pctunder18 ))
nonwhitevictims
# important statistics derived from data


# -  Above I included information about the percentage of non-white victims, the percentage of black unarmed victims, and the percentage of victims under the age of 18 because I feel like these are all factors that are important to look at when looking at this data set, and how some groups might be affected.

# In[74]:


nyshootings = (policeshootings.where('city',are.equal_to('New York'))
                             .where('state',are.equal_to('NY')))
ny = nyshootings.select('name','date','race','age','gender')
ny
#fatal police shootings in new york


# -  Above I included the names of the victims of fatal shootings by police in New York, New York. I think it is important to be aware of what might be happening where you live.

# In[81]:


whywheretheyshot = (policeshootings.where('armed',are.equal_to('unarmed'))
                    .where('threat_level',are.not_equal_to('attack'))
                    .where('flee',are.equal_to('Not fleeing')))
whywheretheyshot = whywheretheyshot.select('name','race',
                        'armed','age','gender',
                        'threat_level','flee')
whywheretheyshot
#List of victims that were unarmed, not seen as a threat, and not fleeing from police


# -  Above I included a table of people who were unarmed, not a threat, and not fleeing the police officers when they were shot. I though this was a moment where more information could be valuable like the context of the shooting. It is difficult to make certain conclusions from data without context. 

# # Analysis : Visualizations
# -  Construct two visualizations showing features of the dataset using graphs we learned in class.
# -  These can be any two, but they must be different (e.g., you can’t do two bar charts).
# -  They can illuminate the same point as the tables, or different ones.
# -  For each, discuss why you chose that visualization and what you learned.

# In[77]:


alaska = policeshootings.where('state',are.equal_to('AK'))
newmexico = policeshootings.where('state',are.equal_to('NM'))
tennessee = policeshootings.where('state',are.equal_to('TN'))
louisiana = policeshootings.where('state',are.equal_to('LA'))
nevada = policeshootings.where('state',are.equal_to('NV'))
arkansas = policeshootings.where('state',are.equal_to('AR'))
missouri = policeshootings.where('state',are.equal_to('MO'))
alabama = policeshootings.where('state',are.equal_to('AL'))
arizona = policeshootings.where('state',are.equal_to('AZ'))
southcarolina = policeshootings.where('state',are.equal_to('SC'))
states = make_array('Alaska', 'New Mexico', 'Tennessee', 
                    'Louisiana', 'Nevada', 'Arkansas', 
                    'Missouri', 'Alabama', 'Arizona',
                    'South Carolina')
numshootings = make_array(alaska.num_rows,newmexico.num_rows,
                          tennessee.num_rows,louisiana.num_rows,
                          nevada.num_rows,arkansas.num_rows,
                          missouri.num_rows,alabama.num_rows,
                          arizona.num_rows,southcarolina.num_rows)
mostdangerousstates = Table().with_columns('Name',states,
                                           'Number of Shootings',numshootings)
mostdangerousstates.barh('Name','Number of Shootings')


# -  Above I have included the top 10 most dangerous states according to Wall St.'s review of the FBI's violent crime rate for all 50 states from the FBI’s Uniform Crime Reporting Program. It is interesting to see how crime is measured in states and the difference between police shooting amounts, and non-police shootings amounts.

# In[79]:


year2015 = policeshootings.where('date',are.below_or_equal_to('2015-12-31'))
#year2016 = policeshootings.where('date',are.below_or_equal_to('2016-12-31'))
#year2017 = policeshootings.where('date',are.below_or_equal_to('2017-12-31'))
#year2018 = policeshootings.where('date',are.below_or_equal_to('2018-12-31'))
#year2019 = policeshootings.where('date',are.below_or_equal_to('2019-12-31'))
year2016 = policeshootings.where('date',
                                 are.strictly_between('2015-12-31','2016-12-31'))
year2017 = policeshootings.where('date',
                                 are.strictly_between('2016-12-31','2017-12-31'))
year2018 = policeshootings.where('date',
                                 are.strictly_between('2017-12-31','2018-12-31'))
year2019 = policeshootings.where('date',
                                 are.strictly_between('2018-12-31','2019-12-31'))
years = make_array('2015','2016','2017','2018')
shootings = make_array(year2015.num_rows,
                       year2016.num_rows,year2017.num_rows,
                       year2018.num_rows)
shootings15to19 = Table().with_columns('Year',years,'Shootings',shootings)
shootings15to19.plot('Year','Shootings')


# -  Above I have included a line graph to visualize the number of police shootings by year. It is from numbered from 960 shootings per year to 1000. I thought it would be interesting to visualize how much these numbers change through the years. I stopped at 2018 because the data for 2019 makes it a lot harder to properly visualize the dips since the year just started

# # Upon reflection, do you feel this dataset was helpful for improving your understanding of the issue of interest?
# -  Describe why or why not
#     -  I thought this dataset was truly enlightening in the way that it allowed me to visualize and manipulate this data to understand more about police shootings and those who are victims of it. At the same time I felt like most of the interpretation was open ended because of the lack of context of these shootings. It felt wrong to try and make conclusions from data I didn't fully understand.

# # What would a better version of this dataset look like?
# -  This may include more variables, variables collected differently, more observations, or anything else
#     -  I think this dataset would be better if it included information such as why the police officer was in that situation, and if it was an act of misconduct. I think it would provide more context to the data, and allow more conclusions to be reached. Although the data information states "The Post is documenting only those shootings in which a police officer, in the line of duty, shot and killed a civilian — the circumstances that most closely parallel the 2014 killing of Michael Brown in Ferguson, Mo.", it is difficult to fully understand to what extent this is applicable for each of these vi
