# Project-Ongoing---Automatic-Question-Generation-From-Educational-Text

## Overview
Questions are an important part of the learning process. A good question can deepen our knowledge about the subject further. They can help you think about a topic from a different point of view that you have never thought of before. They are the starting point of research work and asking the right questions leads us to the right answers.
As questions are an essential part of education and academia, it is a tedious task to automate such an essential part. In this project, we have tried to solve this challenging task. Even though automatic question generation works fine on Factual data like Wikipedia, less progress has been made on generating questions from the technical data.
This project investigates the current state of automatic question generation and how it performs with the technical data. We discover which types of questions can be generated automatically regarding the technical data. Then we continue how to generate question types like Gap-fill questions, Multiple choice questions, True or false questions and Match the Column questions.
In the evaluation, we discover key criteria and shortcomings that would further improve the performance of automatically generating questions from the technical text.


## 1) Data Extraction and Cleaning 

##### Approach 1 – Using pdf to text library in python (PyPDF2)

![](https://github.com/shubhamk8597/College-Project-On-going---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/PYPDF2.JPG)

Using this approach there was less manual intervention but the output contained a lot of gibberish text. The library could not correctly identify and convert the header and footer symbols and did not ignore them. This resulted in a lot of random gibberish text in the output which further increased the manual job of cleaning later.

##### Approach 2 – Using Microsoft Word to convert pdf to text

![](https://github.com/shubhamk8597/College-Project-On-going---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/WORD.PNG)

Microsoft word does an excellent job of correctly identifying headers and footers. Moreover, it correctly identifies most of the scientific symbols which are important to us. This is a manual step, and one requires Microsoft Word as an extra tool, it saves a lot of time in data cleaning compared to the first approach.


## 2) Summarization 

After cleaning the data, we notice that the number of sentences of little importance is very high, and we do not want to process all the sentences as it is very process heavy and time consuming. One way to sort important sentences is by summarizing the text. This way we get the most important text that we should work on neglecting common or less important texts that do not add much to the context.
Here we use Bert-extractive-summarizer library which is based on the paper ‘Leveraging BERT for Extractive Text Summarization on Lectures’. It uses BERT model for text embeddings and KMeans clustering to identify sentences close to the centroid for summary selection. (Miller, 2019).
In this model we have the options to set the minimum and maximum length of the summary we want. We can also define the ratio of the summary length with respect to the input. For example., if the length is 10000 characters and we set the ratio attribute as ratio= 0.6 then the summary will have 6000 characters.

## 3) Failure ofWH question type

As WH questions are the most common types of questions that are widely known I started with this question type. The approach that was widely used in (Husain et al, 2015) and (Le et al, 2014).
Creating a WH question involved two steps. The first was to correctly POS tag a sentence. The second step was to define rules for each type of POS tags. This method works well on a factual data like Wikipedia. But it did not do perform good on technical data that our course has.
The reasons I did not continue with WH question type
1) No labeled technical data to train the model
2) Tedious task of defining very specific rules for every POS tag which takes away the goal of automation.

## 

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
![](https://github.com/shubhamk8597/College-Project-Ongoing---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/2.PNG)
### Steps

**1 - Summarize the text**
      We use the BERT Extractive Summarizer to reduce the data and keep somewhat relevant sentences
      
**2 - Get Sentences for Filtered Keys**
      Then we extract sentences having these filtered keys form the summarized text
      
**3 - Split the sentences in half and add to dataframe**
      We use the pandas library to store the sentences in a dataframe 

**4 - Use sample command of pandas to generater question**
      We First use the sample command to finter out 5 sentences and then apply sample command on the second row to generate questions
      
            
## Problems and  Future tasks

1 - Generating different question types like odd man out, 

2 - Working on calculation based questions

3 - To extract keyphrases and make questions of descriptive type

4 -  Making the output aesthetic  

5 - In match the columns working on the words that split in between and give out the answers





