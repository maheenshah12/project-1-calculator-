import streamlit as st

# Function for the simple calculator
def simple_calculator():
    st.title("Simple Calculator")

    # Select operation
    operation = st.selectbox(
        "Select operation:",
        ["Add", "Subtract", "Multiply", "Divide"]
    )

    # Input numbers
    num1 = st.number_input("Enter the first number", value=0.0)
    num2 = st.number_input("Enter the second number", value=0.0)

    # Perform calculation on button click
    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
            st.write(f"Result: {num1} + {num2} = {result}")
        elif operation == "Subtract":
            result = num1 - num2
            st.write(f"Result: {num1} - {num2} = {result}")
        elif operation == "Multiply":
            result = num1 * num2
            st.write(f"Result: {num1} * {num2} = {result}")
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
                st.write(f"Result: {num1} / {num2} = {result}")
            else:
                st.write("Error: Division by zero is not allowed.")

# Call the simple calculator function
simple_calculator()
