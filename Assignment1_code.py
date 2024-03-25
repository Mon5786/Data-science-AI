# This python file takes an csv file about population
# as input It calculates the dependency ratio and the 
# fraction of different age groups over the years and 
# creates some nice plots

# Import necessary packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read in the csv file
filename = \
  'swedish_population_by_year_and_sex_1860-2022.csv'
df = pd.read_csv(filename)

# Remove plus sign for each element (if any), then 
# convert into integer
df['age'] = \
  df['age'].apply(lambda x: int(x.replace('+', '')))

# In order to calculate the dependency ratio for each 
# year, it is necessary to devide the population for 
# each year into three groups: the 0 to 14 year old, 
# the 15 to 64 year olds and the 65+ year olds. 
# Gender doesn't matter in this case.
children = df[(df['age'] < 15)].sum()
working_pop = \
    df[(df['age'] > 14) & (df['age'] < 65)].sum()
elderly = df[(df['age'] > 64)].sum()

# Ignore the first two rows (int of age and sex, 
# these sums don't make any sense
children = children[2:]
working_pop = working_pop[2:]
elderly = elderly[2:]

# Calculate the dependency ratio
dependency_ratio = \
    100 * ((children+elderly)/working_pop)

# Extract years and convert them and the dependency 
# ratio in np.arrays
years = np.array(dependency_ratio.keys())
years_array = years.astype('int')
dep_array = np.array(dependency_ratio)

# Plot the dependency ratio over the years
fig, ax = plt.subplots()
ax.plot(years_array, dep_array, 
        label='Dependency ratio')
plt.title('Dependecy ratio in Sweden ' 
          'from 1860 to 2022')
plt.xlabel('Year')
plt.ylabel('Ratio (%)')
plt.legend()

# Save the plot
plt.savefig('Dependency ratio Sweden.pdf')

# Calculate the fraction of the children and the 
# elderly for each year.
# Therefore divide the number through the whole 
# population (not just working force as for the 
# dependency ratio)
children_frac = \
    100 * (children/(children+working_pop+elderly))
elderly_frac = \
    100 * (elderly/(children+working_pop+elderly))

# Convert the fractions into np.arrays
children_frac_array = np.array(children_frac)
elderly_frac_array = np.array(elderly_frac)

# Plot the dependency ratio with the fractions of the 
# children and the elderly
fig, ax = plt.subplots()
lines = [[dep_array, 'Dependency ratio'], 
         [children_frac_array, 'Fraction children'], 
         [elderly_frac_array, 'Fraction elderly']]
for line in lines:
    ax.plot(years_array, line[0], label=line[1])

plt.title('Dependecy ratio and age fractions in ' 
          'Sweden from 1860 to 2022')
plt.xlabel('Year')
plt.ylabel('Ratio (%)')
plt.legend()

# Save the plot
plt.savefig('Dependency ratio and ' 
            'fractions Sweden.pdf')