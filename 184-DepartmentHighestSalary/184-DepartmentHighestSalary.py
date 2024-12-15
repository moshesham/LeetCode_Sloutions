import pandas as pd

def department_highest_salary(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(left=df1,right=df2,left_on='departmentId',right_on='id',how='left')
    bf = df.groupby('departmentId').max()
    pf = pd.merge(left=df,right=bf,on=['salary','name_y'])
    return pf[['name_y','name_x_x','salary']].rename(columns={'name_y':'Department','name_x_x':'Employee','salary':'Salary'})