# Project-Ongoing---Automatic-Question-Generation-From-Educational-Text

## This is an on going project so the code and output are not well documented

## Overview
We all have good methods to transform simple factual texts into questions but there is an actual need to form questions in the educational field, espeically science and technology. This project is an attempt to form questions based on educational text.

## Data extraction

#### Importance of a clean organised data
Most of the   educational material is in the form of PDF, and we loose important data when converting pdf to text document. For us to work efficiently we need to have a clean source of data which can be directly obtained from the faculties. 
I did not have the text files and I used PDF extraction libraries which did not give results. At last I converted the pdf file into word and then exported into txt format which gave me great results and fairly clean data.

## MCQ Generation
![](https://github.com/shubhamk8597/College-Project-On-going---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/1.PNG)
### Steps
**1 - Summarize the text**
      We use the BERT Extractive Summarizer to reduce the data and keep somewhat relevant sentences
      
**2 - Extract Keywords**
      Python keyword extractor (PKE) library helps us extract keywords from the text. Here we can set how 
      many keywords do we want
      
**3 - Extract Filtered Keys**
      Now by searching the keywords extracted in summarized text we filter out only the keywords present in summarized text
      
**4 - Get Sentences for Filtered Keys**
      Then we extract sentences having these filtered keys form the summarized text
      
**5 - Generate Distractors**
      Using the gensim model and golve2word2vec we find similar words which can be wrong answers for each       filtered key.

**6 - Replaces Filtered Keys with Blank and add distractors**
      Presenting the sentence by eliminating the answer keyword and generating the questions

## Match the column
###Steps
**1 - Summarize the text**
      We use the BERT Extractive Summarizer to reduce the data and keep somewhat relevant sentences
      
**2 - Get Sentences for Filtered Keys**
      Then we extract sentences having these filtered keys form the summarized text
      
**3 - Split the sentences in half and add to dataframe**
      We use the pandas library to store the sentences in a dataframe 

**4 - Use sample command of pandas to generater question**
      We First use the sample command to finter out 5 sentences and then apply sample command on the second row to generate questions
      
      


      

## Next tasks
1 - Generating different question types like odd man out, Match the columns.

2 - Working on calculation based questions

2 - To extract keyphrases and make questions of descriptive type

