# Restaurant-Rating-Controller
In this project, we have created a fuzzy control system on python which models how one might rate the restaurant based on factors like food, ambience and the expenses.
INTRODUCTION
Fuzzy Inference System is the primary unit of a Fuzzy Logic System having decision making as its primary work. It uses the “IF…THEN” rules along with connectors “OR” or “AND” for drawing essential rules.
The flow of a fuzzy logic controller is as follows:
     1. Defining Inputs and Outputs 
     2. Making “IF..THEN” rules based on the inputs and outputs.
     3. Computing outputs with respect to given inputs.
     4. Defuzzification of the Fuzzy output into a crisp result. 
Our Fuzzy System helps one to determine the rating of the restaurant on basis of factors like food, ambience, and prices.  We formulated this problem as:
![image](https://user-images.githubusercontent.com/75019003/202105241-98d0f1b3-eab7-41bb-87b5-9f450bb1b9f9.png)
Proposed Algorithm
A. Inputs
1. Food
 Universe (crisp value range): How good was the food, on a scale of 0 to 10?
 Fuzzy Set (fuzzy value range): poor, average, good
2. Ambience
Universe (crisp value range): How good was the ambience, on a scale of 0 to 10?
Fuzzy Set (fuzzy value range): poor, average, good
3. Prices
Universe (crisp value range): Range of prices on a scale of Rs.0 to Rs.4000
Fuzzy Set (fuzzy value range): cheap, affordable, expensive
B. Outputs
Rating
Universe: What should be the rating on a scale of 0 to 5?
Fuzzy set: Low, medium, High
C. Rules
IF the food was poor, ambience was poor, prices were expensive, THEN rating will be low.
IF the food was poor, ambience was average, prices were expensive, THEN rating will be low.
IF the food was average, ambience was average, prices were expensive, THEN rating will be medium.
IF the food was average, ambience was good, prices were expensive, THEN rating will be medium.
IF the food was good, ambience was good, prices were expensive, THEN rating will be high.
IF the food was good, ambience was good, prices were affordable, THEN rating will be high.
IF the food was good, ambience was average prices were cheap, THEN rating will be high.
IF the food was good, ambience was average prices were cheap, THEN rating will be medium.
IF the food was average, ambience was poor, prices were cheap, THEN rating will be medium.
