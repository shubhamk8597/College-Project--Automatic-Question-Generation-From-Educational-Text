# Automatic-Question-Generation-From-Techni-Text

## Overview
Questions are an important part of the learning process. A good question can deepen our knowledge about the subject further. They can help you think about a topic from a different point of view that you have never thought of before. They are the starting point of research work and asking the right questions leads us to the right answers.
As questions are an essential part of education and academia, it is a tedious task to automate such an essential part. In this project, we have tried to solve this challenging task. Even though automatic question generation works fine on Factual data like Wikipedia, less progress has been made on generating questions from the technical data.
This project investigates the current state of automatic question generation and how it performs with the technical data. We discover which types of questions can be generated automatically regarding the technical data. Then we continue how to generate question types like Gap-fill questions, Multiple choice questions, True or false questions and Match the Column questions.
In the evaluation, we discover key criteria and shortcomings that would further improve the performance of automatically generating questions from the technical text.


## Research Questions

1) What type of questions can be well automated for technical learning material?
2) How to implement the automation of these question types?
3) How to facilitate teachers in creating exam questions by suggesting them automated questions?
4) How to help students with self-learning and self-evaluation?

## Workflow of Implementation - Questions

I started with traditional question types of WH-Questions and Template Based Questions. The drawbacks in these types lead us to different question types which is explained below


![](https://github.com/shubhamk8597/College-Project-On-going---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/worrkflow.JPG)


## Workflow of Implementation - GUI

After we have the questions we follow the following flow to display them to teachers for scrutiny. These questions are then displayed to the Students for self evaluation


![](https://github.com/shubhamk8597/College-Project-On-going---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/workflowgui.JPG)


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


## QUESTION TYPES AND APPROACH

## 1) WH question type 

#### Steps to generate WH question type

iamges

#### Example of WH Question type


iamges


#### Evaluation

As WH questions are the most common types of questions that are widely known I started with this question type. 
Creating a WH question involved two steps. The first was to correctly POS tag a sentence. The second step was to define rules for each type of POS tags. This method works well on a factual data like Wikipedia. But it did not do perform good on technical data that our course has.
The reasons I did not continue with WH question type
1) No labeled technical data to train the model
2) Tedious task of defining very specific rules for every POS tag which takes away the goal of automation.


##  2) Template Based Questions and Ideas for further Questions.

Template based questions were the 2nd most common type after wh questions.It consists of two parts. The fixed part is the template which is user defined and the variable part are the POS tagged nouns proper nouns etc. 

iamge table ppt


#### Evaluation

As this apporach also relies on identifying the proper POS tagg, it under performed because it could not identify the technical terms.

The main take away from the template based approach was that the variable part represented the important word of the sentence. It can be defined as the **Keyword** of the sentence. This realization led the discovery of futhers question types.



## 3) 







