import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

Systolic = ctrl.Antecedent(np.arange(20, 300, 1), "Systolic")
Systolic["Low"] = fuzz.trapmf(Systolic.universe, [20, 44.0741, 67, 94])
Systolic["Normal"] = fuzz.trapmf(Systolic.universe, [118, 120.3704, 130, 131])
Systolic["High"] = fuzz.trapmf(Systolic.universe, [138, 146, 157, 161])
Systolic["Very_high"] = fuzz.trapmf(Systolic.universe, [158, 167, 180, 183])
Systolic["Low_Normal"] = fuzz.trapmf(Systolic.universe, [86.3, 92.963, 112, 122])
Systolic["High_Normal"] = fuzz.trapmf(Systolic.universe, [128, 134, 140, 141])
Systolic["too_high"] = fuzz.trapmf(Systolic.universe, [179, 207, 274, 300])
Diastolic = ctrl.Antecedent(np.arange(20, 130, 1), "Diastolic")
Diastolic["Low"] = fuzz.trapmf(Diastolic.universe, [20, 29.7, 46.3, 62])
Diastolic["Low_Normal"] = fuzz.trapmf(Diastolic.universe, [60, 63.8, 73.1085, 80])
Diastolic["High_Normal"] = fuzz.trapmf(Diastolic.universe, [83.9, 85.6217, 89.1, 90.9])
Diastolic["Very_High"] = fuzz.trapmf(Diastolic.universe, [98.4, 102, 106.8651, 111])
Diastolic["Too_High"] = fuzz.trapmf(Diastolic.universe, [108, 114, 123.7434, 130])
Diastolic["Normal"] = fuzz.trapmf(Diastolic.universe, [78, 78.3466, 83.3, 86])
Diastolic["High"] = fuzz.trapmf(Diastolic.universe, [88.5317, 91.9, 97.3, 101])
BP_Levels = ctrl.Consequent(np.arange(0, 100, 1), "BP_Levels")
BP_Levels["Hipotension"] = fuzz.trapmf(BP_Levels.universe, [0, 5.69, 12.3016, 18.5])
BP_Levels["Optimal"] = fuzz.trapmf(BP_Levels.universe, [16.1, 23.4127, 32.9, 41.6])
BP_Levels["Normal"] = fuzz.trapmf(BP_Levels.universe, [39.9, 41.1376, 46.2, 49.1])
BP_Levels["High_Normal"] = fuzz.trapmf(BP_Levels.universe, [47.7, 50.3968, 53.3, 55.6])
BP_Levels["Grade_1"] = fuzz.trapmf(BP_Levels.universe, [58.5, 62.3, 66.2698, 67.8])
BP_Levels["Grade_2"] = fuzz.trapmf(BP_Levels.universe, [70.7, 74.2063, 77.4, 79.2])
BP_Levels["Grade_3"] = fuzz.trapmf(BP_Levels.universe, [83, 87.7, 95.8995, 100])
BP_Levels["ISH1"] = fuzz.trapmf(BP_Levels.universe, [53.7, 56.2169, 59.9, 60.5])
BP_Levels["ISH2"] = fuzz.trapmf(BP_Levels.universe, [66.4, 68.3862, 71.8, 72])
BP_Levels["ISH3"] = fuzz.trapmf(BP_Levels.universe, [77.7, 80.6, 84.5, 84.7])

rule1 = ctrl.Rule(Systolic["Low"] & Diastolic["Low"], BP_Levels["Hipotension"])
rule2 = ctrl.Rule(Systolic["Low_Normal"] & Diastolic["Low_Normal"], BP_Levels["Optimal"])
rule3 = ctrl.Rule(Systolic["Normal"] & Diastolic["Normal"], BP_Levels["Normal"])
rule4 = ctrl.Rule(Systolic["High_Normal"] & Diastolic["High_Normal"], BP_Levels["High_Normal"])
rule5 = ctrl.Rule(Systolic["High"] & Diastolic["High"], BP_Levels["High_Normal"])
rule6 = ctrl.Rule(Systolic["Very_high"] & Diastolic["Very_High"], BP_Levels["Grade_2"])
rule7 = ctrl.Rule(Systolic["too_high"] & Diastolic["Too_High"], BP_Levels["Grade_3"])
rule8 = ctrl.Rule(Systolic["Very_high"] & Diastolic["High"], BP_Levels["Grade_2"])
rule9 = ctrl.Rule(Systolic["too_high"] & Diastolic["Very_High"], BP_Levels["Grade_3"])
rule10 = ctrl.Rule(Systolic["too_high"] & Diastolic["High"], BP_Levels["Grade_3"])
rule11 = ctrl.Rule(Systolic["High"] & Diastolic["Very_High"], BP_Levels["Grade_2"])
rule12 = ctrl.Rule(Systolic["High"] & Diastolic["Too_High"], BP_Levels["Grade_3"])
rule13 = ctrl.Rule(Systolic["Very_high"] & Diastolic["Too_High"], BP_Levels["Grade_3"])
rule14 = ctrl.Rule(Systolic["High"] & Diastolic["Normal"], BP_Levels["ISH1"])
rule15 = ctrl.Rule(Systolic["High"] & Diastolic["High_Normal"], BP_Levels["ISH1"])
rule16 = ctrl.Rule(Systolic["Very_high"] & Diastolic["Normal"], BP_Levels["ISH2"])
rule17 = ctrl.Rule(Systolic["Very_high"] & Diastolic["High_Normal"], BP_Levels["ISH2"])
rule18 = ctrl.Rule(Systolic["too_high"] & Diastolic["Normal"], BP_Levels["ISH3"])
rule19 = ctrl.Rule(Systolic["too_high"] & Diastolic["High_Normal"], BP_Levels["ISH3"])
rule20 = ctrl.Rule(Systolic["Normal"] & Diastolic["High"], BP_Levels["Grade_1"])
rule21 = ctrl.Rule(Systolic["High"] & Diastolic["Low_Normal"], BP_Levels["ISH1"])
rule22 = ctrl.Rule(Systolic["Very_high"] & Diastolic["Low_Normal"], BP_Levels["ISH2"])
rule23 = ctrl.Rule(Systolic["too_high"] & Diastolic["Low_Normal"], BP_Levels["ISH3"])
rule24 = ctrl.Rule(Systolic["Normal"] & Diastolic["Low_Normal"], BP_Levels["Normal"])
rule25 = ctrl.Rule(Systolic["Low_Normal"] & Diastolic["Low"], BP_Levels["Optimal"])

rule1.view()

tipping_ctrl = ctrl.ControlSystem(
    [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15,
     rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['Systolic'] = 211
tipping.input['Diastolic'] = 101
# Crunch the numbers
tipping.compute()

print(tipping.output['BP_Levels'])

#BP_Levels.view(sim=tipping)
