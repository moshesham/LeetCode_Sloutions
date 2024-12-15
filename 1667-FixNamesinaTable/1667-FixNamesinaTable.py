import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    email_regex = r"^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\.com$"
    valid_emails = users[users['mail'].str.match(email_regex)]

    return valid_emails



    