import streamlit as st
import pandas as pd
import scipy.stats as stats
import math

st.set_page_config(page_title="A/B Testing", page_icon=":tada", layout="wide")

with st.container():
    st.title("A/B TESTING")
    
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("""This is a small streamlit web application that allows users to perform hypothesis testing for A/B tests with ease. Users can input data related to their control and treatment groups, including the number of visitors and conversions for each group, as well as their desired confidence level.
Based on this input, the app conducts the hypothesis test and provides the result: whether the experiment group is better, the control group is better, or if the results are indeterminate.""")
    with right_column:
        htp5= "https://img.freepik.com/free-vector/web-design-content-creating-landing-page-website-homepage-creating-design-element-female-graphics-designer-developer-flat-character_335657-2617.jpg?t=st=1710695653~exp=1710699253~hmac=3f5f11f2dcff17385dadc999fabe7d04cc737ebaefeef8d24b60ebbd5f3afef5&w=740"
        st.image(htp5, width=300)\
        
with st.container():
    st.write("---")
    
    uploaded_file = st.file_uploader("File is uploaded below")
    
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.write(data)
        st.write(data.isnull().sum())
    
with st.container():

    st.write("---")
    left_column, right_column= st.columns(2)

with left_column:
    def test_hypothesis(control_group_visitors, control_group_conversions, experiment_group_visitors, experiment_group_conversions, confidence_level):
        control_group_rate = control_group_conversions / control_group_visitors
        experiment_group_rate = experiment_group_conversions / experiment_group_visitors
        
        std_dev = math.sqrt(control_group_rate * (1 - control_group_rate) / control_group_visitors + experiment_group_rate * (1 - experiment_group_rate) / experiment_group_visitors)

        if confidence_level == 90:
            critical_value = 1.645
        elif confidence_level == 95:
            critical_value = 1.96
        elif confidence_level == 99:
            critical_value = 2.576
        else:
            raise ValueError("Invalid confidence level.")

        z_score = (experiment_group_rate - control_group_rate) / std_dev

        p_value = stats.norm.cdf(-abs(z_score))

        significant = p_value < 0.05

        return p_value, significant, control_group_rate, experiment_group_rate

st.title("A/B Test Hypothesis Testing App")
with st.container():

    st.write("---")
    left_column, right_column= st.columns(2)

with right_column:
    control_group_visitors = st.number_input("Control Group Visitors")
    control_group_conversions = st.number_input("Control Group Conversions")
    experiment_group_visitors = st.number_input("Experiment Group Visitors")
    experiment_group_conversions = st.number_input("Experiment Group Conversions")
    confidence_level = st.selectbox("Confidence Level", [90, 95, 99])
with left_column:
    htp6= "https://img.freepik.com/free-vector/storyboard-process-illustration_23-2148679316.jpg?t=st=1710695791~exp=1710699391~hmac=a77e95c008215ba23257b0a7a2801cdc07904871046b52461bb58feb3861830a&w=740"
    st.image(htp6, width= 400)

st.write("To run the hypothesis test, click on the specified button below ↓")

if st.button("Run Hypothesis Test"):
    p_value, significant, control_group_rate, experiment_group_rate = test_hypothesis(control_group_visitors, control_group_conversions, experiment_group_visitors, experiment_group_conversions, confidence_level)

    if significant:
        if experiment_group_rate > control_group_rate:
            st.write("Experiment Group's variant is better.")
        else:
            st.write("Control Group's variant is better.")
    else:
        st.write("Indeterminate")

    st.write("p-value:", p_value)
    
