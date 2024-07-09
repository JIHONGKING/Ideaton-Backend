import pandas as pd
import numpy as np

# Sample data creation for 500 entries with experience, acceptance rate, and company name
np.random.seed(42)  # For reproducibility

# Generating data
experience_years = np.random.uniform(0, 15, 500)
acceptance_rate = np.random.uniform(0, 100, 500)
companies = ['Company A', 'Company B', 'Company C', 'Company D', 'Company E']

# Creating DataFrame
data = []
for exp, acc in zip(experience_years, acceptance_rate):
    primary_company = np.random.choice(companies)
    other_companies = np.random.choice([c for c in companies if c != primary_company], size=np.random.randint(0, 3), replace=False)
    data.append({'Experience': exp, 'Acceptance Rate': acc, 'Primary Company': primary_company, 'Other Companies': ', '.join(other_companies)})

df = pd.DataFrame(data)

# Save the updated CSV file
updated_file_path = '/Users/jihong/Desktop/아이디어톤/Acceptance Rate by Experience( JOB SEEKER)/sample_experience_acceptance_improved.csv'
df.to_csv(updated_file_path, index=False)
