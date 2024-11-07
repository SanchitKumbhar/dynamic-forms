import google.generativeai as genai
import os
import json
import ast

genai.configure(api_key="AIzaSyAYRIOGJiBxqf9T3QDmQQgKx-dM1O-b86o")

model = genai.GenerativeModel("gemini-1.0-pro")
# user = "list of colleges in india"
var=" in option tag" 
large="large"
response = model.generate_content(large + "list of animals" + var)

# response_text = response.text.strip()

# # Remove the brackets and split by comma
# if response_text.startswith("[") and response_text.endswith("]"):
#     response_text = response_text[1:-1]  # Strip the brackets

# actual_list = [item.strip().strip("") for item in response_text.split(",")]

print(response.text)

