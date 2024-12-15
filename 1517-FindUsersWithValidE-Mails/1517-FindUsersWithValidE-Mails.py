import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].apply(is_valid)]

def is_valid(content: str) -> bool:
    return any([x.startswith('DIAB1') for x in content.split()])