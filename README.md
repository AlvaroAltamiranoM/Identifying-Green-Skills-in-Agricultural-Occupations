# Identifying Green Skills in Agricultural Occupations

An NLP pipeline that identifies "green" skills within agricultural occupations by matching occupational skill descriptions against the ESCO skills taxonomy. Built as the skills-assessment component of a GGGI study on the employment impacts of climate-smart agriculture in Colombia and Ethiopia.

## Problem

Estimating the workforce implications of scaling climate-smart agriculture (CSA) requires identifying which skills within agricultural occupations are environmentally relevant ("green"). Manual coding of that skill content does not scale across many occupations and countries. This project automates the identification using a standardized green-skills reference.

## Data

- Occupational skill descriptions for agricultural value chains in Colombia and Ethiopia
- The ESCO (European Skills, Competences, Qualifications and Occupations) taxonomy as the reference set for green skills

## Method

- Semantic and string-similarity matching between occupational skill text and ESCO green-skill entries
- spaCy language model for vectorized comparison
- Scoring and thresholding to flag occupations by green-skill content

## Result

An occupation-level mapping of green-skill intensity that informed the report's assessment of the human capital needed to accelerate CSA adoption in the two countries.

## Publication

This work supported *Employment Impacts of Deploying Climate-Smart Agriculture Practices* (GGGI Technical Report No. 37, June 2025), which estimates the economy-wide, full-time-equivalent employment impacts of meeting Colombia's and Ethiopia's NDC agricultural targets over 2024-2034.

Report: https://gggi.org/report/employment-impacts-of-deploying-climate-smart-agriculture-practices/

