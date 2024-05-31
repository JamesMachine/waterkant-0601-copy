import streamlit as st
from openai import OpenAI

# chat_model = "gpt-4o"
chat_model = "gpt-3.5-turbo-0125"

api_key=st.secrets.api_key
client = OpenAI(api_key=api_key)

system_content = """
    You are a highly skilled AI trained in Skincare Expertise with aesthetic medicine background. 
    A case is given. You task is the following:

    1. identity the client's background
    2. identify client's concerns
    3. if client has any skin diseases or problems, suggest possible causes of those diseases and problems

    Return message in a more organize format. Use list, point form, or table to present the result, if necessary.
    """

def user_background(user_name):

    user_anna = """
        Anna Müller, a 22-year-old from Berlin, Germany, has combination skin and is dealing with several common skin concerns. 
        Her primary issues include acne, particularly in the form of inflammatory pimples concentrated around her chin and jawline, 
        indicative of hormonal acne. She also struggles with blackheads, whiteheads, and enlarged pores, especially in her T-zone. 
        Additionally, Anna experiences post-inflammatory hyperpigmentation, uneven skin tone, and occasional dullness, 
        all of which contribute to her desire to prevent early signs of aging. 
        Her skincare routine includes using a gentle foaming cleanser with salicylic acid to control 
        acne, a lightweight, non-comedogenic gel moisturizer with hyaluronic acid and niacinamide to maintain hydration, and spot treatments with benzoyl peroxide.
        She incorporates a BHA exfoliant several times a week to address blackheads and clogged pores and applies a clay mask weekly for deep cleansing. 
        To improve skin texture and brighten her complexion, she has recently started using a vitamin C serum in the morning and a mild retinol cream at night. 
        Anna also consistently uses a broad-spectrum SPF 30 sunscreen daily to protect her skin from UV damage and prevent further pigmentation. 
        She avoids harsh physical exfoliants, over-washing her face, picking or squeezing pimples, heavy comedogenic products, 
        and alcohol-based products to prevent further irritation and maintain her skin's health.
    """
    user_sara = "I am Sarah!"
    user_user = "I am Emma!"

    li_user = {
        "anna":user_anna, 
        "sara":user_sara, 
        "user":user_user
        }

    return (li_user[user_name])

def chat_response(conversation_history):

    response = client.chat.completions.create(
      model=chat_model,
      messages=conversation_history
    )

    assistant_message = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": assistant_message})
    
    return conversation_history, assistant_message



