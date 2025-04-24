# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 23:20:48 2025

@author: HP
"""

# carbonify_app.py

import streamlit as st
import os
from openai import OpenAI

# 🔐 Get your API key securely
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai_api_key = st.secrets["OPENAI_API_KEY"]
# carbonify_app.py

# 🧠 Create OpenAI client
client = OpenAI(api_key=openai_api_key)

my_instructions = instructions = """
आप Carbonify कंपनी के सहायक हैं, जो भारत में किसानों को टिकाऊ खेती के लिए biochar आधारित समाधान प्रदान करती है।

**Carbonify कंपनी की जानकारी (ब्रॉशर से):**

- Carbonify एक सतत कृषि समाधान देने वाली कंपनी है।
- कंपनी biochar आधारित उत्पाद बनाती है जो मिट्टी की उर्वरता बढ़ाते हैं।
- Carbonify के उत्पाद कृषि को अधिक टिकाऊ, उर्वर और जलवायु-अनुकूल बनाने के लिए विशेष रूप से डिज़ाइन किए गए हैं।
- MYCOBIOCHAR मिट्टी में नमी बनाए रखता है, उर्वरता सुधारता है, और रासायनिक खाद की ज़रूरत कम करता है।
- HUMINOCARB-G विशेष जीवाणुओं और पोषक तत्वों का सम्पूर्ण संग्रह है।
- K-NUTRA — सूक्ष्म पोषक तत्वों से भरपूर उन्नत जैविक उत्पाद
- BIOPHOS — फॉस्फोरस घुलनशील करने वाले लाभकारी सूक्ष्मजीव
- SUPREME PHOSPHATE — पौधों के लिए उच्च गुणवत्ता वाला फॉस्फोरस स्त्रोत
- SILI-NUTRA — पौधों में रोग प्रतिरोधक क्षमता बढ़ाने वाला सिलिका आधारित उत्पाद
- CALSIPHOS — कैल्शियम और फॉस्फोरस का संतुलित मिश्रण
- VERMICOMPOST — केंचुआ खाद जो मिट्टी की संरचना और जैविकता सुधारती है
- LIQUID BIOFERTILIZERS — तरल जैव उर्वरक जो जड़ों की वृद्धि और पोषण uptake में सहायक
- SILISUPER — पौधों की मजबूती और रोग प्रतिरोधक क्षमता के लिए उन्नत सिलिका फ़ॉर्मूला
- Carbonify का लक्ष्य है खेती को जलवायु-अनुकूल और लागत-कुशल बनाना।
- हमारे उत्पाद से किसानों को बेहतर पैदावार और मिट्टी की गुणवत्ता में सुधार मिला है।
- हम स्थानीय कृषि निकायों के साथ मिलकर समाधान तैयार करते हैं।

**आपका उद्देश्य:**

1. किसानों को खेती, मृदा, फसल, और biochar के उपयोग पर सरल हिंदी में जानकारी देना।
2. जब भी उपयुक्त हो, Carbonify के biochar उत्पादों का उपयोग सुझाना।
3. खेती से बाहर के प्रश्नों का उत्तर न दें; politely मना करें।
4. उत्तर हमेशा देवनागरी हिंदी में और ग्रामीण किसानों के अनुकूल हों।
"""


# --- Setup page ---
st.set_page_config(page_title="Carbonify Chat", layout="centered")
st.title("🌱 Carbonify - Farmer's ChatGPT")
st.markdown("Ask anything about farming, soil, crops, or carbon farming practices.")

# --- Initialize chat history ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Initialize input state ---
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# --- Display chat history ---
for entry in st.session_state.chat_history:
    st.markdown(f"👨‍🌾 **You:** {entry['user']}")
    st.markdown(f"🤖 **Carbonify:** {entry['bot']}")

# --- Input box ---
st.text_input(
    "💬 Type your question:",
    key="user_input",
    on_change=lambda: handle_input()
)

# --- Define handler function ---
def handle_input():
    user_text = st.session_state.user_input.strip()
    if user_text:
        try:
            response = client.responses.create(
                model="gpt-4o-mini",
                instructions = my_instructions,
                input=user_text
            )
            answer = response.output_text

            st.session_state.chat_history.append({
                "user": user_text,
                "bot": answer
            })

        except Exception as e:
            st.session_state.chat_history.append({
                "user": user_text,
                "bot": f"❌ Error: {e}"
            })

    # Clear input after processing
    st.session_state.user_input = ""
