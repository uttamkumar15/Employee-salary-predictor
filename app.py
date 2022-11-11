import streamlit as st
import streamlit.components.v1 as components
import pickle
st.set_page_config(page_title= 'Employee Salary Predictor')
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://images.unsplash.com/photo-1521737852567-6949f3f9f2b5?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=847&q=80");
background-size: cover;
}
</style>

'''
st.markdown(page_bg_img,unsafe_allow_html=True)
st.title(":adult: Employee Salary Predictor :chart:")
experience = st.number_input('Years of Experience')
if st.button("Predict Salary"):
    model = pickle.load(open('Employee Salary predictor.pkl', 'rb'))
    result = model.predict([[experience]])
    result = round(result[0],2)
    st.header("Salary :dollar: : "+str(result))