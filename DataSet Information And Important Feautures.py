import streamlit as st
import pandas as pd
import shap
from PIL import Image
import base64
st.write("### DataSet Format Information")

st.write("""
**Ind_ID**:  Client ID

**Gender**:  Gender information ['M','F']

**Car_owner**:  Having car or not ['Y','N']

**Propert_owner**:  Having property or not ['Y','N']

**Children**:  Count of children

**Annual_income**:  Annual income

**Type_Income**:  Income type ['Pensioner','Commercial associate','Working','State servant']

**Education**:  Education level ['Higher education','Secondary / secondary special','Lower secondary','Incomplete higher','Academic degree']
 
**Marital_status**:  Marital_status ['Married','Single / not married','Civil marriage','Separated' 'Widow']

**Housing_type**:  Living style ['House / apartment','With parents','Rented apartment','Municipal apartment','Co-op apartment' 'Office apartment']

**Birthday_count**:  Use backward count from current day (0), -1 means yesterday.

**Employed_days**:  Start date of employment. Use backward count from current day (0). Positive value means, individual is currently unemployed.

**Mobile_phone**:  Any mobile phone

**Work_phone**:  Any work phone

**Phone**:  Any phone number

**EMAIL_ID**:  Any email ID

**Type_Occupation**:  Occupation['Core staff','Cooking staff','Laborers','Sales staff','Accountants','High skill tech staff','Managers' 'Cleaning staff','Drivers','Low-skill Laborers','IT staff','Waiters/barmen staff','Security staff','Medicine staff','Private service staff' 'HR staff','Secretaries','Realty agents']

**Family_Members**:  Family size""")

df1=pd.read_csv("Credit_card.csv")
df2=df1[~ df1.isnull().any(axis=1)].head()

st.subheader("the Dataset format to upload")
st.dataframe(df2)



st.write("You can download sample Dataset from this")
st.download_button('Download file',data=pd.DataFrame.to_csv(df2,index=False), mime="text/csv")


st.subheader('The important Feautures To classify an Credit Card Approval Data')
image = Image.open('Shap plot.png')

st.image(image, caption='Important Feautures')





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

#st_shap(shap.force_plot(explainer.expected_value, shap_values, X), 400)

#st_shap(shap.summary_plot(shap_values, df1))
# Display the plot in Streamlit
