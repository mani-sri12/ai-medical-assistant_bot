import streamlit as st
from database import init_db, get_connection
from utils.gemini_helper import analyze_symptoms

# Initialize DB once at startup
init_db()

st.set_page_config(
    page_title="AI Medical Assistant",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 AI Medical Assistant Bot")

st.markdown(
    "> ⚠️ This app gives only general health guidance and emergency warnings.\n"
    "> It does **not** diagnose or prescribe medicines. Always consult a doctor for real medical advice."
)

# Sidebar navigation
page = st.sidebar.radio(
    "Menu",
    ["Symptom Checker", "BMI Calculator", "Chat History", "Health Tips"]
)

# 1) Symptom Checker
if page == "Symptom Checker":
    st.header("🩺 Symptom Checker")

    symptoms = st.text_area("Describe your symptoms in your own words")

    if st.button("Analyze"):
        if not symptoms.strip():
            st.warning("Please enter your symptoms first.")
        else:
            # Emergency keywords (extra safety)
            emergency_words = [
                "chest pain",
                "breathing difficulty",
                "shortness of breath",
                "heart attack",
                "stroke",
                "unconscious"
            ]

            if any(word in symptoms.lower() for word in emergency_words):
                st.error(
                    "🚨 Emergency Warning: Your description may need urgent medical attention."
                )

            result = analyze_symptoms(symptoms)
            st.success("Analysis Complete")
            st.write(result)

            # Save to chat history
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(
                    """
                    INSERT INTO chat_history (symptom, response)
                    VALUES (?, ?)
                    """,
                    (symptoms, result)
                )
                conn.commit()
                conn.close()
                st.info("Saved to chat history.")
            except Exception as e:
                st.error(f"Database error: {e}")

# 2) BMI Calculator
elif page == "BMI Calculator":
    st.header("⚖️ BMI Calculator")

    st.markdown(
        "Enter your weight and height to estimate your Body Mass Index (BMI). "
        "BMI is a simple screening tool and does not replace a medical check‑up."
    )

    weight = st.number_input("Weight (kg)", min_value=1.0, value=60.0)
    height = st.number_input("Height (m)", min_value=0.1, value=1.70)

    if st.button("Calculate BMI"):
        bmi = weight / (height * height)
        st.success(f"Your BMI is {bmi:.2f}")

        if bmi < 18.5:
            st.info("Category: Underweight")
            st.markdown(
                "- Try to eat **regular meals and snacks** with enough calories.\n"
                "- Focus on **nutrient‑dense foods**: nuts, seeds, peanut butter, paneer, eggs, lentils, beans, curd.\n"
                "- Include **whole grains** like brown rice, whole‑wheat roti, and millets.\n"
                "- Add healthy oils like a small amount of groundnut, sunflower, or olive oil to meals.\n"
                "- If you stay underweight for a long time, please consult a doctor or nutritionist."
            )
        elif bmi < 25:
            st.info("Category: Normal weight")
            st.markdown(
                "- Maintain a **balanced diet** with vegetables, fruits, whole grains, and protein.\n"
                "- Limit junk food and sugary drinks.\n"
                "- Stay active with regular walking or exercise most days of the week."
            )
        elif bmi < 30:
            st.info("Category: Overweight")
            st.markdown(
                "- Try to choose **more vegetables and fruits** on your plate.\n"
                "- Reduce **fried items, fast food, and sugary drinks**.\n"
                "- Prefer **whole grains** instead of white rice or refined flour.\n"
                "- Aim for regular physical activity, like brisk walking, as suitable for you.\n"
                "- For a personalized weight‑loss plan, talk to a doctor or dietitian."
            )
        else:
            st.info("Category: Obese")
            st.markdown(
                "- Focus on **small, sustainable changes** in eating and activity.\n"
                "- Fill half your plate with **vegetables and salads**, and reduce portion size of rice/roti.\n"
                "- Avoid **sugary drinks, sweets, and frequent fried foods** as much as possible.\n"
                "- Choose **whole grains, pulses, lean protein** (like lentils, beans, egg whites, fish, curd).\n"
                "- Try to move more during the day: short walks, light exercise as your health allows.\n"
                "- Because obesity can affect heart, joints, and sugar levels, please consult a doctor for proper guidance."
            )

        st.markdown(
            "> These BMI tips are general information only and may not suit everyone. "
            "For medical or diet advice, please consult a qualified healthcare professional."
        )

# 3) Chat History
elif page == "Chat History":
    st.header("📜 Chat History")

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT symptom, response FROM chat_history ORDER BY id DESC"
        )
        rows = cursor.fetchall()
        conn.close()

        if rows:
            for symptom, response in rows:
                st.markdown(f"**Symptom:** {symptom}")
                st.markdown(f"**Response:** {response}")
                st.markdown("---")
        else:
            st.info("No chat history found yet. Run the Symptom Checker to add entries.")
    except Exception as e:
        st.error(f"Could not load chat history: {e}")

# 4) Health Tips
elif page == "Health Tips":
    st.header("💡 General Health Tips")

    st.markdown("- Stay hydrated: drink enough clean water throughout the day.")
    st.markdown("- Sleep around 7–8 hours per night as regularly as possible.")
    st.markdown("- Include fruits and vegetables in your daily diet.")
    st.markdown("- Limit sugary drinks, junk food, and very oily or fried items.")
    st.markdown("- Avoid smoking and limit alcohol intake.")
    st.markdown("- Do regular light exercise or walking as per your fitness level.")
    st.markdown("- For any persistent or severe symptoms, consult a qualified doctor.")