import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
#Defining Inputs and Outputs
food = ctrl.Antecedent(np.arange(0, 11, 1), 'food')
ambience = ctrl.Antecedent(np.arange(0, 11, 1), 'ambience')
prices = ctrl.Antecedent(np.arange(0, 4001, 1), 'prices')
rating = ctrl.Consequent(np.arange(0, 6, 1), 'rating')

#Creating Fuzzy Sets for Inputs and Outputs
food['poor'] = fuzz.trimf(food.universe, [0, 0, 5])
food['average'] = fuzz.trimf(food.universe, [0, 5, 10])
food['good'] = fuzz.trimf(food.universe, [5, 10, 10])

ambience['poor'] = fuzz.trimf(ambience.universe, [0, 0, 5])
ambience['average'] = fuzz.trimf(ambience.universe, [0, 5, 10])
ambience['good'] = fuzz.trimf(ambience.universe, [5, 10, 10])

prices['cheap'] = fuzz.trimf(prices.universe, [0, 0, 1500])
prices['affordable'] = fuzz.trimf(prices.universe, [0, 1500, 4000])
prices['expensive'] = fuzz.trimf(prices.universe, [1500, 4000, 4000])

rating['low'] = fuzz.trimf(rating.universe, [0, 0, 3])
rating['medium'] = fuzz.trimf(rating.universe, [0, 3, 5])
rating['high'] = fuzz.trimf(rating.universe, [3, 5, 5])

#Displaying Input and Output Graphs
food.view()
ambience.view()
prices.view()
rating.view()

#Creating Rules
rule1 = ctrl.Rule(food['poor'] & ambience['poor'] & prices['expensive'], rating['low'])
rule2 = ctrl.Rule(food['poor'] & ambience['average'] & prices['expensive'], rating['low'])
rule3 = ctrl.Rule(food['average'] & ambience['average'] & prices['expensive'], rating['medium'])
rule4 = ctrl.Rule(food['average'] & ambience['good'] & prices['expensive'], rating['medium'])
rule5 = ctrl.Rule(food['good'] & ambience['good'] & prices['expensive'], rating['high'])
rule6 = ctrl.Rule(food['good'] & ambience['good'] & prices['affordable'], rating['high'])
rule7 = ctrl.Rule(food['good'] & ambience['average'] & prices['cheap'], rating['high'])
rule8 = ctrl.Rule(food['good'] & ambience['average'] & prices['cheap'], rating['medium'])
rule9 = ctrl.Rule(food['average'] & ambience['poor'] & prices['cheap'], rating['medium'])

#Control System Creation and Simulation
RestaurantRatings_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
RestaurantRatings = ctrl.ControlSystemSimulation(RestaurantRatings_ctrl)
#Giving input values to produce an output
RestaurantRatings.input['food'] = 6.0
RestaurantRatings.input['ambience'] = 1.5
RestaurantRatings.input['prices'] = 500.0
RestaurantRatings.compute()

print("The rating is:", RestaurantRatings.output['rating'])
rating.view(sim=RestaurantRatings)
