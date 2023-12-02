# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 22:31:17 2022
@author: Alvaro Altamirano Montoya
"""

#I. Dependencies
import pandas as pd
import spacy

# II. Loading CEDEFOP's Conventional and Green Skills collections
green =  pd.read_csv('greenSkillsCollection_en.csv')['preferredLabel'].to_list() #Green skills dataset 
matrix =  pd.read_excel('Skills_occupations_matrix_tables.xlsx', sheet_name = 'Matrix 3.0') #Conventional skills dataset
skills = (matrix.iloc[0].reset_index())[0][2:].rename('skills')

#II. string similarity Matching
# Importing Spacy's Model
nlp = spacy.load("en_core_web_md", disable = ['ner', 'tagger', 'parser'])
green_nlp = [nlp(x) for x in green]
skills_nlp = [nlp(x) for x in skills]
similarityMatrix = [[x.similarity(y) for x in green_nlp] for y in skills_nlp]

dicto = pd.DataFrame(dict(zip(skills, similarityMatrix)), index=green)
dicto.to_csv('skills-to-green-jobs2.csv')

# III. Green skills analysis
#Load 'skills to green skills' dataset
df = pd.read_csv("skills-to-green-jobs2.csv")
# Extract the row and column names from the DataFrame
row_names = df.index.tolist()
column_names = df.columns.tolist()
# Convert the DataFrame to a numpy array for easier manipulation
matrix = df.to_numpy()
# Get the dyads with values greater than 0.8 and their corresponding row and column names
dyads = []
for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        if isinstance(value, (int, float)) and value > 0.8:
            dyad = (row_names[i], column_names[j], value)
            dyads.append(dyad)
# Extract the second elements (column names) into a list
set_to_find = list(set([dyad[1] for dyad in dyads[1:]]))
#Load agricultural occupations dataset
agri_occupations=  pd.read_csv('agri_ocup.csv')
#Subset an occupation for analytical example
agri_occupations = agri_occupations[['skills', 'Agricultural Engineer']] #Subset
green_in_isco = agri_occupations['skills'].isin(set_to_find) #Identify conventional skills as green skills
agri_occupations = agri_occupations.loc[~ (agri_occupations.select_dtypes(include=['number']) == 0).all(axis='columns'), :]  #Create green skill percentage
agri_occupations['green'] = green_in_isco.astype(int)

