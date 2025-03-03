import streamlit as st 
# Functioniality
def distance_convertor(from_unit,to_unit,value):
    units = {
          "Meters": 1,
          "Kilometers": 1000,
          "Feet": 0.3048,
          "Miles": 1609.34,
    }
    result = value * units[from_unit] / units[to_unit]
    return result
def temprature_converter(from_unit,to_unit,value):
    if from_unit == "Calsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Calsius":
        result = (value - 32) * 5/9
    else:
        result = value
    return result
def weight_convertor(from_unit,to_unit,value):
    units = {
         "Kilograms": 1,
         "Grams": 0.001,
         "Pounds": 0.453592,
         "Ounces": 0.0283495,
    }
    result = value * units[from_unit] / units[to_unit]
    return result
def pressure_convertor(from_unit,to_unit,value):
    units = {
          "Pascals": 1,
          "Hectopascals": 100,
          "Kilopascals": 1000,
          "Bar": 100000,
    }
    result = value * units[from_unit] / units[to_unit]
    return result           
# UI    

st.title("🎰Unit Convertor")
category = st.selectbox("✨Select Category", ["Distance", "Temprature", "Weight", "Pressure"])


if category == "Distance":
    from_unit = st.selectbox("From",["Meters","Kilometers", "Feet", "Miles"])
    to_unit = st.selectbox("To",["Meters","Kilometers","Feet", "Miles"])
    value = st.number_input("Enter  Value")
    if st.button("Convert"):
        result = distance_convertor(from_unit,to_unit,value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Temprature":
     from_unit = st.selectbox("From",["Calsius", "Fahrenheit"])
     to_unit = st.selectbox("To",["Calsius", "Fahrenheit"])
     value = st.number_input("Enter  Value")
     if st.button("Convert"):
        result = temprature_converter(from_unit,to_unit,value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Weight":
     from_unit = st.selectbox("From",["Kilograms", "Grams", "Pounds", "Ounces"])
     to_unit = st.selectbox("To",["Kilograms", "Grams", "Pounds", "Ounces"])
     value = st.number_input("Enter  Value")
     if st.button("Convert"):
        result = weight_convertor(from_unit,to_unit,value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Pressure":
     from_unit = st.selectbox("From",["Pascals", "Hectopascals", "Kilopascales", "Bar"])
     to_unit = st.selectbox("To",["Pascals", "Hectopascals", "Kilopascales", "Bar"])
     value = st.number_input("Enter  Value")
     if st.button("Convert"):
        result = pressure_convertor(from_unit,to_unit,value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
                                                