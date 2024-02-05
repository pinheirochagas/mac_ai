### Coding Homework: Analysis Library for Dementia Patient Data

#### Overview
In this assignment, you are tasked with developing a Python library called `DementiaAnalysis` designed to analyze a simulated dataset containing neuropsychological assessments and basic demographics of a cohort of patients with dementia. This library will help you practice data manipulation, visualization, and statistical analysis using Python. Your library will consist of three modules: `importer`, `viz`, and `stats`. Each module will have specific functions to import data, visualize it, and perform statistical analyses, respectively.

#### Dataset Description
The dataset is a simulated collection of neuropsychological assessments for patients with dementia, including basic demographic information. The data is stored in CSV format and contains the following columns:

- Patient ID
- Age
- Gender
- Diagnosis (e.g., type of dementia)
- Cognitive Test Scores (various metrics)

#### Modules and Functions

##### 1. Importer Module
- **Objective:** Create a function to import CSV files into a pandas DataFrame.
- **Function Name:** `load_data`
- **Input:** File path to the CSV file.
- **Output:** pandas DataFrame containing the dataset.
- **Requirements:** The function should handle exceptions (e.g., file not found) and provide informative error messages.

##### 2. Viz Module
- **Objective:** Develop functions to plot data distribution and visualize group differences and correlations.
- **Function Names and Descriptions:**
  - `plot_distribution`: Plots the distribution of a specified column (e.g., age, test scores).
  - `plot_boxplot`: Creates boxplots to visualize group differences based on a specified categorical variable (e.g., gender, diagnosis).
  - `plot_correlation_matrix`: Generates a correlation matrix plot to visualize correlations between continuous variables.
  - `scatter_plot`: Plots a scatter plot to visualize the relationship between two continuous variables.
- **Inputs:** pandas DataFrame, column names for plotting, and any other relevant parameters for customization.
- **Output:** Visualization plots.
- **Requirements:** Each function should include parameters for plot customization (e.g., figure size, labels).

##### 3. Stats Module
- **Objective:** Implement functions to easily handle group comparisons and analyze relationships between variables.
- **Function Names and Descriptions:**
  - `perform_ttest`: Conducts a T-test for comparing the means of two groups.
  - `perform_anova`: Performs ANOVA to compare means across multiple groups.
  - `calculate_correlation`: Calculates correlation coefficients between two continuous variables.
  - `perform_regression`: Conducts a linear regression analysis to explore relationships between variables.
- **Inputs:** pandas DataFrame, column names for variables involved in the analysis, and any additional parameters required for the analysis.
- **Output:** Statistical analysis results, including test statistics, p-values, and summary statistics.
- **Requirements:** Functions should check for assumptions where applicable (e.g., normality for T-test) and handle exceptions gracefully.

#### Submission Guidelines
- Include a README.md file with installation instructions and examples of how to use each function.
- Document your code thoroughly, including docstrings for each function describing its purpose, inputs, outputs, and any exceptions handled.
- Test your code with a subset of the dataset to ensure functionality.

#### Evaluation Criteria
- **Functionality:** The library functions perform as described.
- **Code Quality:** The code is well-organized, commented, and follows Python best practices.
- **Documentation:** The README.md and docstrings provide clear instructions and descriptions.
- **Error Handling:** The code gracefully handles errors and provides informative error messages.

#### Deadline
Please submit your completed assignment via the learning management system by [Insert Deadline Here].

This assignment will test your ability to manipulate, visualize, and analyze data using Python. It will also give you the opportunity to develop a project that could be included in your portfolio. Good luck!
