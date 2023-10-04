import streamlit as st
from PIL import Image
import base64

st.title("Algorithm used in it")


st.subheader("The models Applied for This Dataset and its Performance(F1Score)")

image = Image.open('Model plot.png')
st.image(image, caption='ML Models F1-Score')

 
st.subheader("The best classifier suitable for this model is **RandomForestClassifier** according to precision,Accuracy,Time taken")
st.write("""the best parameters of this classifiers are  

             max_features:     'log2'
         min_samples_leaf:  1
         min_samples_split: 2 
         n_estimators:      100 """)
st.write("The **f1 score** is **99.1%**")
st.write("The **precision** and **REcall** also above **98.1%**")





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