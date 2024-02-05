#%%
import pandas as pd
import numpy as np
from numpy.random import default_rng

#%%
# Seed for reproducibility
rng = default_rng(42)

# Constants
N = 1000
DIAGNOSES = [
    "Alzheimer's Disease", "Parkinson's Disease", "Frontotemporal Dementia",
    "Lewy Body Dementia", "Corticobasal Degeneration",
    "Nonfluent Variant Primary Progressive Aphasia",
    "Semantic Variant Primary Progressive Aphasia",
    "Logopenic Variant Primary Progressive Aphasia", "Healthy Control"
]

# Cognitive domains and their influence on test scores by diagnosis
cognitive_domains = {
    "Global Cognition": ["Mini-Mental State Examination Total Score", "Global Cognition"],
    "Executive Function/Processing Speed": ["Trail Making Test", "Digit Task"],
    "Verbal Memory": ["Verbal Memory Recall (30-item)", "Verbal Memory Recall (10-item)"],
    "Attention": ["Attention"],
    "Visuospatial/Constructional": ["Rey-Osterrieth Complex Figure Test"],
    "Memory/Naming": ["Memory and Naming", "Boston Naming Test Correct"],
    "Working Memory": ["Digit Forward Correct", "Digit Backward"],
    "Language": ["Auditory Naming Correct"],
    "Visuospatial Memory": ["Rey-Osterrieth Complex Figure Test (10-min delay)", "Rey-Osterrieth Complex Figure Test Recognition"],
    "Depression": ["Geriatric Depression Scale Total Score"],
    "Dementia Severity": ["Clinical Dementia Rating Total Score"]
}

# Initialize the dataset with ID, Age, Gender, and Diagnosis
df = pd.DataFrame({
    'ID': np.arange(1, N + 1),
    'Age': rng.integers(50, 81, size=N),
    'Gender': ['Male', 'Female'] * (N // 2),
    'Diagnosis': rng.choice(DIAGNOSES, N)
})

# Function to generate scores based on diagnosis
def generate_score(domain, diagnosis):
    base_score = {
        "Healthy Control": 28,
        "Alzheimer's Disease": 22,
        "Parkinson's Disease": 25,
        "Frontotemporal Dementia": 20,
        "Lewy Body Dementia": 23,
        "Corticobasal Degeneration": 18,
        "Nonfluent Variant Primary Progressive Aphasia": 19,
        "Semantic Variant Primary Progressive Aphasia": 17,
        "Logopenic Variant Primary Progressive Aphasia": 21
    }
    
    # Adjust the base score for the domain based on the diagnosis
    score_adjustment = rng.normal(loc=0, scale=3)  # Small random adjustment
    domain_base_score = base_score.get(diagnosis, 25) + score_adjustment
    
    # Ensure the score is within 0-30 range
    return max(0, min(domain_base_score, 30))

# Generate scores for each test based on the cognitive domain and diagnosis
for domain, tests in cognitive_domains.items():
    for test in tests:
        df[test] = df['Diagnosis'].apply(lambda dx: generate_score(domain, dx))

# Reorder the columns to match the order provided
column_order = ['ID', 'Age', 'Gender', 'Diagnosis'] + [test for tests in cognitive_domains.values() for test in tests]
df = df[column_order]

#%% Round Mini-Mental State Examination Total Score to the nearest integer
df['Mini-Mental State Examination Total Score'] = df['Mini-Mental State Examination Total Score'].round()

#%% Save the dataframe to a CSV file
df.to_csv('simulated_cognitive_tests_dataset.csv', index=False)

# %%
