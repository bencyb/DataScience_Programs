# Hypothesis Testing (t-test)

import numpy as np
from scipy.stats import ttest_ind

#data
group1 = [75, 80, 85, 90, 95]
group2 = [65, 70, 75, 80, 85]

# Perform t-test
t_stat, p_value = ttest_ind(group1, group2)

print("Group 1:", group1)

# Output::Group 1: [75, 80, 85, 90, 95]

print("Group 2:", group2)

# Output::Group 2: [65, 70, 75, 80, 85]

print("t-statistic:", t_stat)

# Output::t-statistic: 2.0

print("p-value:", p_value)

# Output::p-value: 0.08051623795726257