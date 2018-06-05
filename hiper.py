import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


x_Systolic = np.arange(0, 300, 1)
x_Diastolic = np.arange(0, 300, 1)
x_BP_levels  = np.arange(0, 100, 1)

#Inputs of the FLC

#Membership functions of systolic
Systolic_Low = fuzz.trapmf(x_Systolic,[20,44.07,67,94])
Systolic_LowNormal = fuzz.trapmf(x_Systolic, [86.3 ,92.96, 112 ,122])
Systolic_Normal = fuzz.trapmf(x_Systolic, [118 ,120.4 ,130 ,131])
Systolic_HighNormal = fuzz.trapmf(x_Systolic, [128 ,134 ,140 ,141])
Systolic_High= fuzz.trapmf(x_Systolic, [138 ,146, 157, 161])
Systolic_VeryHigh = fuzz.trapmf(x_Systolic, [158, 167, 180 ,183])
Systolic_tooHigh = fuzz.trapmf(x_Systolic, [179 ,207, 274 ,300])

#Membership functions of Diastolic
Diastolic_Low = fuzz.trapmf(x_Diastolic, [20, 29.7, 46.3, 62])
Diastolic_LowNormal=fuzz.trapmf(x_Diastolic, [60, 63.8, 73.11, 80])
Diastolic_Normal=fuzz.trapmf(x_Diastolic, [78, 78.35, 83.3, 86])
Diastolic_HighNormal=fuzz.trapmf(x_Diastolic, [83.9, 85.62, 89.1, 90.9])
Diastolic_High=fuzz.trapmf(x_Diastolic, [88.53, 91.9, 97.3, 101])
Diastolic_VeryHigh=fuzz.trapmf(x_Diastolic, [98.4, 102, 106.9, 111])
Diastolic_tooHigh=fuzz.trapmf(x_Diastolic, [108, 114, 123.7, 130])


#Output of the FLC
#Membership functions of BP Levels
Hipotension=fuzz.trapmf(x_BP_levels, [0, 5.69, 12.3, 18.5])
Optimal = fuzz.trapmf(x_BP_levels, [16.1, 23.41, 32.9, 41.6])
Normal = fuzz.trapmf(x_BP_levels, [39.9, 41.14, 46.2, 49.1])
High_Normal= fuzz.trapmf(x_BP_levels, [47.7, 50.4, 53.3, 55.6])
ISH1= fuzz.trapmf(x_BP_levels, [53.7, 56.22, 59.9, 60.5] )
Grade1=fuzz.trapmf(x_BP_levels, [58.5, 62.3, 66.27, 67.8])
ISH2=fuzz.trapmf(x_BP_levels, [66.4, 68.39, 71.8, 72])
Grade2= fuzz.trapmf(x_BP_levels, [70.7, 74.21, 77.4, 79.2])
ISH3= fuzz.trapmf(x_BP_levels, [77.7, 80.6, 84.5, 84.7])
Grade3 = fuzz.trapmf(x_BP_levels, [83, 87.7, 95.9, 100])

# Visualize these universes and membership functions
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(x_Systolic,Systolic_Low , 'b', linewidth=1.5, label='Systolic_Low')
ax0.plot(x_Systolic, Systolic_LowNormal, 'g', linewidth=1.5, label='Systolic_LowNormal')
ax0.plot(x_Systolic, Systolic_Normal, 'r', linewidth=1.5, label='Systolic_Normal')
ax0.plot(x_Systolic, Systolic_HighNormal, 'g', linewidth=1.5, label='Systolic_HighNormal')
ax0.plot(x_Systolic, Systolic_High, 'r', linewidth=1.5, label='Systolic_High')
ax0.plot(x_Systolic, Systolic_VeryHigh, 'g', linewidth=1.5, label='Systolic_VeryHigh')
ax0.plot(x_Systolic, Systolic_tooHigh, 'r', linewidth=1.5, label='Systolic_tooHigh')
ax0.set_title('systolic')
ax0.legend()

ax1.plot(x_Diastolic, Diastolic_Low, 'b', linewidth=1.5, label='Diastolic_Low')
ax1.plot(x_Diastolic, Diastolic_LowNormal, 'g', linewidth=1.5, label='Diastolic_LowNormal')
ax1.plot(x_Diastolic, Diastolic_Normal, 'r', linewidth=1.5, label='Diastolic_Normal')
ax1.plot(x_Diastolic, Diastolic_HighNormal, 'g', linewidth=1.5, label='Diastolic_HighNormal')
ax1.plot(x_Diastolic, Diastolic_High, 'r', linewidth=1.5, label='Diastolic_High')
ax1.plot(x_Diastolic, Diastolic_VeryHigh, 'g', linewidth=1.5, label='Diastolic_VeryHigh')
ax1.plot(x_Diastolic, Diastolic_tooHigh, 'r', linewidth=1.5, label='Diastolic_tooHigh')
ax1.set_title('Diastolic')
ax1.legend()

ax2.plot(x_BP_levels,Hipotension , 'b', linewidth=1.5, label='Hipotension')
ax2.plot(x_BP_levels, Optimal, 'g', linewidth=1.5, label='Optimal')
ax2.plot(x_BP_levels,Normal , 'r', linewidth=1.5, label='Normal')
ax2.plot(x_BP_levels,High_Normal , 'g', linewidth=1.5, label='High_Normal')
ax2.plot(x_BP_levels, ISH1, 'r', linewidth=1.5, label='ISH1')
ax2.plot(x_BP_levels,Grade1 , 'g', linewidth=1.5, label='Grade1')
ax2.plot(x_BP_levels, ISH2, 'r', linewidth=1.5, label='ISH2')
ax2.plot(x_BP_levels,Grade2 , 'g', linewidth=1.5, label='Grade2')
ax2.plot(x_BP_levels,ISH3 , 'g', linewidth=1.5, label='ISH3')
ax2.plot(x_BP_levels,Grade3 , 'r', linewidth=1.5, label='Grade3')

ax2.set_title('BP Levels')
ax2.legend()

# Turn off top/right axes
for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.show()
