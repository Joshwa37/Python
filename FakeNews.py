import google.generativeai as genai

genai.configure(api_key="API KEY") # Replace with your actual Gemini API key

def chat_with_gemini(prompt):
    model = genai.GenerativeModel('gemini-2.0-flash') #or gemini-pro-vision if needed.
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_with_gemini(user_input)
        print("Gemini: ", response) #Changed the output name.
    