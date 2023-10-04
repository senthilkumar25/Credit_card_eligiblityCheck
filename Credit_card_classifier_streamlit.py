#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import pandas as pd
import pickle
import base64


# In[3]:


st.title("Credit Card Customer Eligiblity test")


# In[4]:


st.write("### Give the input data like this below CSV format ")


# In[39]:


def onehot_encode(train_df,test_df):
    categorical_columns=['Type_Income', 'Type_Occupation', 'Housing_type', 'Marital_status', 'EDUCATION']
    # Combine the training and testing DataFrames into one DataFrame
    combined_df = pd.concat([train_df, test_df], axis=0)
    # Perform one-hot encoding on the combined DataFrame for the categorical columns
    combined_df_encoded = pd.get_dummies(combined_df, columns=categorical_columns)
    # Split the combined DataFrame back into training and testing DataFrames
    train_df_encoded = combined_df_encoded[:len(train_df)]
    test_df_encoded = combined_df_encoded[len(train_df):]
    return test_df_encoded

def category_col(df):
    # Data Binary Encoding✅
    binary_columns = ["GENDER","Car_Owner","Propert_Owner"]

    for col in binary_columns:
        if not "GENDER" == col:
            df[col] = df[col].replace({"Y":1,"N":0})
        else: 
            df[col] = df[col].replace({"M":1,"F":0})
    return df
def age_count(df):
     # Birthday / Unemployed transform
    df["Age"] = df["Birthday_count"].apply(lambda x : abs(int(x))/365)
    df = df.drop("Birthday_count", axis=1)
    df= df.drop("Ind_ID", axis=1)
    return df


# In[47]:


def data_preprocesor(df2):
    df1=pd.read_csv("Credit_card.csv")
    t1=onehot_encode(df1,df2)
    t2=category_col(t1)
    t3=age_count(t2)
    return t3


# In[6]:
df1=pd.read_csv("Credit_card.csv")
df2=df1[~ df1.isnull().any(axis=1)].head()

st.subheader("the Dataset format to upload")
st.dataframe(df2)
st.write("You can download sample Dataset from this")
st.download_button('Download file',data=pd.DataFrame.to_csv(df2,index=False), mime="text/csv")





def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background(r'C:\Users\usar\Desktop\SSN\PROJECT - VIZ\ezgif.com-webp-to-png.png')

st.subheader("Upload The dataSet here To Know eligible for Credit Card")
data_file = st.file_uploader("Upload CSV",type=["csv"])
if st.button("Classify"):
    if data_file is not None:
        file_details = {"filename":data_file.name, "filetype":data_file.type,"filesize":data_file.size}
        st.write(file_details)
        st.write("the Dataset uploaded")
        df = pd.read_csv(data_file)
        id=df["Ind_ID"]
        st.dataframe(df)
        d1=data_preprocesor(df)
        
        with open('Credictcard.pkl','rb') as file:
            cls1=pickle.load(file)
        st.dataframe(d1)
        pr1=cls1.predict(d1)
        d2=pd.DataFrame({"Ind_ID":list(id),"Predicted labels":pr1})
        st.subheader("Customer Elifgible details by given id")
        st.dataframe(d2)
        st.write("You can download Predicted values with id from this")
        st.download_button('Download Predicted values',data=pd.DataFrame.to_csv(d2,index=False), mime="text/csv")
    else:
        st.write("No Files are uploaded")




def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_png_as_page_bg(png_file):
    bin_str = get_base64(png_file) 
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    background-attachment: scroll; # doesn't work
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg(r'C:\Users\usar\Desktop\SSN\PROJECT - VIZ\ezgif.com-webp-to-png.png')
# df2=df1[~ df1.isnull().any(axis=1)].head()

# df2.drop(['Ind_ID'],axis=1,inplace=True)

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




