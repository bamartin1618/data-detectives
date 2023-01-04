#importing general objects
import pandas as pd
import plotly.express as px
import numpy as np
import streamlit as st

# '''
# Accessing your dashboard: after running "streamlit run streamlit_app.py", you'll want to access your website!
# If your URL looks like this: https://coding.ai-camp.dev/projects/ad938e8d-2c1b-480b-b393-94673d3d4628/files/WC22-Data-Science/.....
# Your dashboard will be at: https://coding.ai-camp.dev/ad938e8d-2c1b-480b-b393-94673d3d4628/port/8501
# Notice how there is no more "/projects/" and no more "files/...". Make those changes to get your site running!

# Instructors: if you are having issues, go to /examples/ and copy the contents of the config.toml file to a new file in the location "~/.streamlit/config.toml"
# '''


#Some basic commands in streamlit -- you can find an amazing cheat sheet here: https://docs.streamlit.io/library/cheatsheet
st.title('Analyzing Student Performances and Contributing Factors')

###### INTRODUCTION #########
#there are many factors that could impact a students performance
#teachers, parents, and students could all benefit by knowing what features affect performance

st.write('Students across the globe work hard to achieve top scoring grades, however, many are unable to reach that expectation due to external conditions. According to the Yale Child Study Center, nearly 75% of students reported having negative feelings related to school. Without a doubt, school is difficult. We find it necessary to research factors that contribute to academic success. From our experiment, we hope to inform teachers, parents, and students as to the many different factors that impact student performance, and help them understand the overall relationships.')

st.markdown("""---""")

###### DATA EXPLANATION ######
copy_dataframe = pd.read_csv("student_data.csv")
mean_g3_scores = copy_dataframe['G3'].mean()

copy_dataframe["G3_Bin"] = copy_dataframe['G3'].apply(lambda x: "Above 50th Percentile" if x > mean_g3_scores else "Below 50th Percentile")

#show off a bit of your data
st.header('The Data')
col1, col2 = st.columns(2) #here is how you can use columns in streamlit. 
col1.dataframe(copy_dataframe.head())
col2.markdown("\n") #add a line of empty space.
col2.markdown('In this data set, we can see data from nearly 400 students, with 30 feature variables. This information has been collected all throughout the 2014 school year and was taken from students who attended Gabriel Pereira or Mousinho da Silveira high schools in Portugal. The data lists many features that impact student performance. The most important features in terms of our research are study time, failures, school support, and absences. Although G1 and G2 are significant aspects of the study, they are dependent with G3 final grades. For that reason we are excluding those features from our research.') #you can add multiple items to each column.
st.markdown("""---""")

###### HYPOTHESIS ########
st.header('Hypothesis')
st.markdown("Excluding the G1 and G2 features, we believe that the highest correlated features with G3 are failures, study time, extra educational support, and absences. We believe that these features have the highest statistical significance in regards to our target variable G3.")
###### FINDINGS #########
st.markdown("""---""")

#visual 1 #box plot --> G3 distribution
st.plotly_chart(px.box(copy_dataframe, y="G3", title="Distribution of G3 Final Grades"))
st.markdown("This visual is representing the distribution of G3 final grades in our data set. We chose a box plot because it clearly shows the viewer where each quartile of the data lies and what the median value is. From this visual we can see that scores from 0 up to 8 but not including 8 are in the first quartile. The second quartile of scores range from 8 up to 11. The third quartile of scores range from 11 up to 14. And the upper quartile of scores range from 14 to 20.")

#visual 2 -=--> pie chart failure distribution
st.image('failure_piechart.png')
st.markdown("For this visualization, we chose to use a pie chart to depict the frequency of students failures and how it relates to their G3 final grades. Most students had 0 failures, and a pie chart would best depict the frequency distribution. As shown from the data, students with more failures are more likely to score in the lower 50th percentile of the G3 scores.")

#visual 3 #scatter plot absences vs G3
st.plotly_chart(px.scatter(copy_dataframe, x = 'absences', y = 'G3', color= 'G3_Bin', title="Relationship between Absences and Final grades"))
st.markdown("This is a Scatter plot that visualizes the relationship between a student's final grade and their number of absences. This was used to help show how absences would affect students' grades. Plots colored in dark blue represent students below the 50th percentile, whilst students in light blue represent students above the 50th percentile. However, as seen by the plot, the relevancy of absences does not entirely have an impact on final grades.")

#visual 4 bar chart comparing study time to G3
st.plotly_chart(px.histogram(copy_dataframe, x="studytime", color="G3_Bin", title="Barchart of Student Study Times"))
st.markdown("For this visualization, we decided on a histogram to demonstrate a discrete statistic of the time students put into studying, and how it might affect their G3 final grade. Again, Stats in light blue demonstrate students who achieve above the 50% percentile whereas the dark blue represents those receiving below 50%. We are unable to conclude that study time has a significant effect on a G3 final grade.")

#visual 5 bar chart comparing extra educational support with G3
st.plotly_chart(px.histogram(copy_dataframe, x = 'schoolsup', color='G3_Bin', title = 'Number of Students Recieving Extra Educational Support '))
st.markdown("This visualization is a histogram that represents the number of students who use extra educational support and whether or not their final G3 grades are in the lower or upper 50th percentile. As shown in the graph, our hypothesis was not supported as students are equally as likely to achieve grades in the upper/lower 50th percentile regardless of whether or not they receive extra educational support.")

#heatmap
import plotly.figure_factory as ff
import numpy as np
columns_to_drop = ['G1', 'G2', 'G3_Bin']
copy_dataframe.drop(columns_to_drop, axis = 1, inplace = False)
copy2_dataframe = copy_dataframe.drop(columns_to_drop, axis = 1, inplace = False)
corr = copy2_dataframe.corr()
x = list(corr.columns)
y = list(corr.index)
z = np.array(corr)

st.plotly_chart(ff.create_annotated_heatmap(
    z,
    x = x,
    y = y ,
    annotation_text = np.around(z, decimals=2),
    hoverinfo='z',
    colorscale='tealrose'
    ))
st.markdown("")


###### CONCLUSION
st.header('Conclusions')
st.markdown("From our correlation heat map, we can conclude that the first four most important features (excluding G1 and G2) are failures, mother's education, age, and father's education. This mostly disproves our hypothesis because study time, extra educational support, and absences have a weak correlation between a student's G3 final score. Although our dataset includes meaningful metrics for measuring academic performance, our dataset can not capture all of the contributing factors that  affects ones performance academically.")
st.markdown('Created by Data Detectives')
            
####### ABOUT US #########
# st.markdown('- Elian Ahmar .....')
st.markdown(' - Ryan Flynn - 11th grade - I got into Data Science because I run a cyber security competition team at my school, and learning about Data Science will expand my overall ability and knowledge to help my team. - Fun fact about me, I play the violin')
st.markdown("- Sahana Radhakrishnan, 11th grade, I got into Data Science because it was an aspect of computer science that I haven't explored. I've participated in web & game development courses in previous years, so I was encouraged to join the data science track at AI camp. A fun fact about me is that I love to sing. ")
st.markdown("- Vanessa Luo, 10th grade, I attended a coding program over the summer which helped pique my interest on AI and machine learning. There I heard about libraries such as pandas and numpy, and AI camp gave me the opportunity to learn about them. A fun fact about me is that I enjoy playing video games.")
st.markdown(' - Diya Laha - 11th grade - My computer science teacher told me about this camp and said I might be interested in it, so here I am. I have previously not had any expierence with data science. However, I attended a conference about data science and that was interesting, that encouraged me to join AI camp. I think a fun fact about me is that I am really into reading! My favourite books include "The Bell Jar", "Perks of being a Wallflower", and "The Catcher in the Rye". ')
                
                
                