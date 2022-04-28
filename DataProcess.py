from cmath import isnan
import pandas as pd
import os
import math

sheet = "Anex"
sheet1 = "Anex"
def isNaN(a,b):
    if(isinstance(a,str)):
        return a!=a
    return math.isnan(a) and isnan(b)
def loadData(filename,filename1,sheet,sheet1):
    df  = pd.read_excel(os.path.join(os.path.dirname(__file__),"templates",filename),sheet_name=sheet)
    df1 = pd.read_excel(os.path.join(os.path.dirname(__file__),"templates",filename1),sheet_name=sheet1)
    return df,df1
    # print(df.head())
def cleanData(df:pd.DataFrame)->pd.DataFrame:
    df.rename(columns=df.iloc[2,:],inplace=True)
    df = df.drop(index=[0,1,2],axis=0,inplace=False)
    df = df.reset_index()
    return df
def Process(df:pd.DataFrame,df1:pd.DataFrame)->list:
    ls = []
    for i in df.index:  
        item_df = df.iloc[i,:]
        item_df1 = df1.iloc[i,:]
        flag = False
        for a,b in zip(item_df,item_df1):
            if isNaN(a,b)==False and a!=b:
                flag = True
                break
                # print(type(a),end="!=")
                # print(b,end="     ")
        # print()
        if flag:
            ls.append(i)
    return ls
def writeOutput(ls:list,df:pd.DataFrame):
    try:
        f = open(os.path.join(os.path.dirname(__file__),"templates","output.txt"),"w+")
        for i in ls:
            f.write("index no {} exel index {} \n ".format(i,df.iloc[i,0]))
        f.close()
    except Exception as e:
        print(e)


# if __name__ == "__main__":
    # df,df1 = loadData("GST_2A_2020-21.xlsx","GST_2A_2020-21_PURCHASW.xlsx")
    # df  = cleanData(df)
    # df1 = cleanData(df1)
    # # print(df.head())
    # ls = (Process(df,df1))
    # print(ls)
    

    # print(df.iloc[527:,6])
    # print(df1.iloc[527:,6])
