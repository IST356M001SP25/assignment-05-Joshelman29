# Reflection

Student Name:  josh elman
Sudent Email:  jdelman@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

In this project, we split the work across several script files following the ETL process. In pandaslib.py, we created helper functions to clean and format data, like extracting years, standardizing country names, converting currency strings to numbers, and normalizing salaries for cost of living. In extract.py, we downloaded the raw survey data, state abbreviation mappings, and cost of living data by year, then saved them locally in the cache folder. In transform.py, we loaded the cached data, cleaned and joined it, converted full state names to abbreviations, matched cities to their cost of living values, adjusted salaries accordingly, and generated two summary reports one by age and one by education level and saved them back to the cache. Finally, in load.py, we uploaded the engineered dataset and both reports to AWS bucket, making them available for use in dashboards.
