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

![](https://github.com/shubhamk8597/College-Project-On-going---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/1_wh_q_step.JPG)

#### Example of WH Question type

![](https://github.com/shubhamk8597/College-Project-On-going---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/2_example_wh.JPG)

#### Evaluation

As WH questions are the most common types of questions that are widely known I started with this question type. 
Creating a WH question involved two steps. The first was to correctly POS tag a sentence. The second step was to define rules for each type of POS tags. This method works well on a factual data like Wikipedia. But it did not do perform good on technical data that our course has.
The reasons I did not continue with WH question type
1) No labeled technical data to train the model
2) Tedious task of defining very specific rules for every POS tag which takes away the goal of automation.


##  2) Template Based Questions and Ideas for further Questions.

Template based questions were the 2nd most common type after wh questions.It consists of two parts. The fixed part is the template which is user defined and the variable part are the POS tagged nouns proper nouns etc. 

![](https://github.com/shubhamk8597/College-Project-On-going---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/3_temp_ex.JPG)


#### Evaluation

As this apporach also relies on identifying the proper POS tagg, it under performed because it could not identify the technical terms.

The main take away from the template based approach was that the variable part represented the important word of the sentence. It can be defined as the **Keyword** of the sentence. This realization led the discovery of futhers question types.


## 3) Gap Fill Questions Using Keyword Extraction

As we understand the previous two failures did give some important outputs, I became searching for ways to use this information. 
The approach was simple. To identify the keyword and then to eleminate it.

#### Steps

![](https://github.com/shubhamk8597/College-Project-On-going---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/4_gap_fill_step.JPG)

In this the main part was the keyword that we were going to eliminate. For extracting the most important words in a text I used  pke – Python keyword extraction library. The library consisted of various algorithms from statistical models like TfIdf to Graph-Based models like TextRank.

Testing with the available algorithms the MultipartiteRank model seemed to work well with the technical data as it was correctly able to identify technical concepts like Current, Voltage, Sensors, meter etc as keywords. 

![](https://github.com/shubhamk8597/College-Project-On-going---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/5_gap_fill_ex.JPG)

#### Evaluation

The major error in the text was the incorrect sentence breaking. As we converted a pdf slide in a text file, there was a lot of formatting errors which resulted in uneven sentences. Because of these even though sentences were without any special characters and looked fine they were just a part of a bigger sentence that was cut out due to formatting

## 4) Multiple Choice Questions by using Gap Fill Questions.

With the generation of gap filled questions I came to realize that sometimes the questions are too difficult and vague to answer. Going through the previous question papers of different subjects Multiple Choice questions were asked in many of the exams This prompted the idea of generating multiple choices for the gap filled questions.

![](https://github.com/shubhamk8597/College-Project-On-going---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/6_mcq_modify.JPG)


So, basically multiple-choice questions have some correct choices and some incorrect choices, but the incorrect choices are not that different from the correct ones. This presented a unique challenge.

#### Steps

![](https://github.com/shubhamk8597/College-Project-On-going---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/7_mcq_steps.JPG)

Using gensims glove2word2vec library that uses Glove, we get top similar words that are close to our answer or keyword. These become the distractors for our Multiple choice questions. 


#### Evaluation 

![](https://github.com/shubhamk8597/College-Project-On-going---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/8_mcq_eval.JPG)

As Multiple-choice questions follow gap fill questions strengths. Same goes to the weaknesses. Apart from these the main issue was because our way of finding the distractors. We found the distractors that were similar and close to our given keywords. Hence the distractors had words with similar meaning and could be potential answers.

- Evaluation Criteria\n
1)Perfect Distractors -Questions that did not need any edits in distractors\n
2)Distractors Needed editing -Adding, editing or removing the generated distractors\n
3)Distractors did not make sense \n

![](https://github.com/shubhamk8597/College-Project-On-going---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/table_mcq_evalve1.JPG)


## 5)True or False Questions and negating a sentence

True or false question type is a well-known question type. Surprisingly, none of the papers had tackled this type. I searched for more research papers for a starting point, but I did not find any literature for converting a true statement to a false one.

The main task was negating a sentence. We can negate a sentence in many ways like by just simply introducing a negative word, but this would be easily spotted by the student and there would not be any learning. The true negation happens when we change an important word or falsify a concept.

![](https://github.com/shubhamk8597/College-Project-On-going---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/9_tf_Steps.JPG)

My first approach was to just negate nouns, but I realized that not all nouns have a opposite word. That’s why I included verbs adjectives to the list of tags for which I wanted to find an antonym. The first step was to tag the sentence appropriately. The next step was to change one tag with the opposite word. We did this to all the tags. In this way we got many false sentences from a single sentence. 

This is the new question type that was not covered anywhere else. It helps students build confidence over the concepts that they know.

#### Evaluation 

The main drawback was that we just changed a single word in a sentence. Because of this most of the time the sentence did not make a proper sense.

![](https://github.com/shubhamk8597/College-Project-On-going---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/10_tf_gui.JPG)

The second was that a literal antonym was used most of the time which also is not a natural way of negating a sentence.

- Evaluation Criteria\n
1)Perfect Questions	- Questions that did not need any edits in false sentence \n
2)False sentence needed editing -Adding, editing or removing the generated fasle sentence\n
3)False sentence did not make sense \n

![](https://github.com/shubhamk8597/College-Project-On-going---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/table_tf.JPG)

## 6) Match the Column

Match the columns is a very popular and is used to evaluate different concepts in a single question. They present a unique challenge when we think of how to generate them automatically.

My first approach was to extract the key phrases. After doing that I would split the key phrases into two parts. The first half would go in the first column and the second half in the second column. Then I would randomize the second column and the student would match the first half with the second half. The drawback of this method was it was too easy to guess the answer because of the middle split.

As said earlier that gap filled questions alone do not provide much of the learning and that’s why I decided to use them in match the columns. The question contains two columns. The first column has the question sentences with a gap and then the second column contains the answers, but they are randomized. The student must match the gaps with the correct answers.

![](https://github.com/shubhamk8597/College-Project-On-going---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/11_mtc_valve.JPG)

#### Evaluation 

This approach proved that we could use the core of one question type to create other question types to increase the learning and self-evaluation of the students.

As Match the column question type uses gap fill question type as basis we can evaluate them together.

- Evaluation Criteria\n
1)Well Formed Questions	-Questions that did not need any edits\n
2)Questions with no sense -Errors due to imporper cleaning,Questions without context \n

![](https://github.com/shubhamk8597/College-Project-On-going---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/table_mcq_evalve.JPG)

## GUI(Graphical User Interface) and Human in the Loop

![](https://github.com/shubhamk8597/College-Project-On-going---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/12_gui.JPG)

## GUI for Teachers 

The GUI for Teachers served 3 main purposes 

- Factor of Human in the loop
- Reviewing of error in automatically generated questions
- Suggesting questions to teachers 

With so many questions that are generated automatically generated there were questions that did not make any sense or that had some errors or random characters.

This made it important to include the human in the loop. In this case the human can be the teacher who is going to set exams for the students. Our generated questions facilitate two things at a time. First it can be used as a suggestion to the examiner. With so many different questions which cover variety of topics it can provide a helping hand when forming questions for the exams. The second is to just eliminate the unwanted questions from the suggested questions and present it directly to students.

In both methods because there is a human involved who is familiar with the subject at hand, the scrutiny makes the result much better.

To make the work of the teacher as easy as possible I designed a simple User Interface that helps the examiner to choose, edit or delete the automatic questions generated as easy as possible. I used pyqt5 library to accomplish the task.

![](https://github.com/shubhamk8597/College-Project-On-going---Automatic-Question-Generation-From-Educational-Text/blob/main/Images/13_gui_teacher.JPG)

## GUI for Students - Self Evaluation

The students are presented with three types of questions. True False, MCQ and Match Columns. In all the three question types the question is presented first. The student has to guess the answers. After he is sure with his answers, he clicks the show answer button to reveal the answers.

When the student sees the answer, he can self-evaluate. He can mark the current question correct and next. This will make the current question correct and this question will not be repeated. He can make the question wrong, and the question stays and will be repeated when and he can go back to the previous question he got wrong.

In this way the questions will be repeated until all the questions are correctly answered. With this method of self-evaluation students can easily better their concepts until they get everything right.


## Conclusion and Future Work

We started of with taking the slides of a course material. But if a department has to generate questions for exam. It can provide the data in a clean manner. This can solve the problem of incorrect formatting and the need to convert pdf or ppt slipped to text. This can exponentially improve the sentence breaking. We will get correct sentences and hence the automated generated questions

When I was searching for a better way to POS tag technical data or a data set of labeled technical data to train my POS tagger, I came across the startup ROKIN. They are actively doing a task of labeling the technical data. They needed me to work on their task if they I wanted to use their data. So, it can be a good starting point for someone with the time to collaborate.

As we use the human in the loop, we can store the changes made to the questions and use this data to train our models further. This will help us use the time that a teacher spends in editing the automatically generated questions

To continue further we can use the previous questions that were asked in the respective exams. This can be a very valuable data. We can either reframe them or for some numerical questions we can change the numeric data to form a new question. With many past question papers, we can easily make a new question paper just by randomly selecting questions from the past.


## Bibliography

Aldabe er al, I. a. (2010). Automatic Distractor Generation for Domain Specific Texts. Advances in Natural Language Processing, 7th International Conference on NLP. Reykjavik.
Boudin, F. (2016). pke: an open source python-based keyphrase extraction toolkit. Proceedings of COLING 2016, the 26th International Conference on Computational Linguistics: System Demonstrations, 69-73.
Chin-Yew el at, L. (2008). Automatic Question Generation from Queries.
Fellbaum, C. (1998). WordNet A Lexical Database for English. Retrieved from princeton.edu: https://wordnet.princeton.edu/
Ghader et al, K. ,.-E. (2019). A Systematic Review of Automatic Question Generation for Educational Purposes. International Journal of Artificial Intelligence in Education.
Husain et al, M. S. (2015). Automatic Question Generation from Text. International Journal for Innovations in Engineering, Science and Management.
Khullar et al, P. a. (2018). Automatic Question Generation using Relative Pronouns and Adverbs. Proceedings of {ACL} 2018, Student Research Workshop.
Kumar et al, S. a. (2017). Automatic generation of multiple choice questions for e-assessment. International Journal of Signal and Imaging Systems Engineering.
Kunichika et al, H. a. (2004). Automated question generation methods for intelligent English learning systems and its evaluation.
Le et al, N.-T. a. (2014). Automatic Question Generation for Educational Applications – The State of Art. Advances in Intelligent Systems and Computing.
Liu et al, M. a. (2012). G-Asks: An Intelligent Automatic Question Generation System for Academic Writing Support. Dialogue and Discourse.
Miller, D. (2019). Leveraging BERT for Extractive Text Summarization on Lectures.
Mostow et al, J. a. (2009). Generating Instruction Automatically for the Reading Strategy of Self-Questioning. Frontiers in Artificial Intelligence and Applications.
Pennington et al, R. S. (2014). GloVe: Global Vectors for Word Representation.
Singh et al, B. A. (2013). Automatic Generation of Multiple Choice Questions Using Wikipedia. Pattern Recognition and Machine Intelligence.
Soni et al, S. a. (2019). Automatic Question Generation: A Systematic Review. International Conference on Advances in Engineering Science Management & Technology.
Xu et al, Y. a. (2009). Automatic Question Generation and Answer Judging: A Q&A Game for Language Learning.
Xuchen et al, Y. a. (2012). Semantics-based Question Generation and Implementation. Dialogue Discourse.
Zhou et al, Q. Z. (2017). Neural Question Generation from Text: A Preliminary Study. arXiv e-prints.
