def analyze_symptoms(symptoms):
    text = symptoms.lower()

    # Strong emergency patterns
    if ("chest pain" in text and "breathing" in text) or "heart attack" in text:
        return (
            "Possible serious heart or lung problem. "
            "This may be an emergency. Please seek immediate medical attention."
        )
    if "stroke" in text or "face drooping" in text or "slurred speech" in text:
        return (
            "Warning signs of possible stroke. "
            "Call emergency services or go to the nearest hospital immediately."
        )
    if "unconscious" in text or "not waking up" in text:
        return (
            "Loss of consciousness is a medical emergency. "
            "Call emergency services immediately."
        )

    # Fever + respiratory
    if "fever" in text and ("cough" in text or "cold" in text or "sore throat" in text):
        return (
            "You may have a viral or respiratory infection such as flu or a common cold. "
            "Rest, drink plenty of fluids, and monitor your temperature. "
            "If breathing becomes difficult or fever is very high, see a doctor."
        )

    # Only fever
    if "fever" in text and "cough" not in text and "cold" not in text:
        return (
            "Fever can be caused by many infections. "
            "Rest, drink fluids, and watch for other symptoms. "
            "If fever is very high or lasts more than 2–3 days, consult a doctor."
        )

    # Headache
    if "headache" in text or "migraine" in text:
        return (
            "Headache may be related to stress, dehydration, or migraine. "
            "Rest in a quiet dark room, drink water, and avoid screen strain. "
            "If the pain is sudden and very severe, or with vision changes or weakness, seek urgent care."
        )

    # Stomach / abdomen
    if "stomach" in text or "abdomen" in text or "abdominal" in text:
        return (
            "Stomach or abdominal pain may be related to indigestion, infection, or other digestive issues. "
            "Eat light food, avoid very spicy or oily meals, and stay hydrated. "
            "If pain is severe, with vomiting, blood in stool, or persistent, see a doctor."
        )

    # Nausea / vomiting / diarrhea
    if "nausea" in text or "vomiting" in text or "diarrhea" in text or "loose motion" in text:
        return (
            "Nausea, vomiting, or diarrhea may suggest a stomach infection or food-related illness. "
            "Sip oral rehydration solutions or clear fluids to prevent dehydration. "
            "If symptoms are severe, bloody, or last more than a day, consult a doctor."
        )

    # Chest pain (non‑emergency description)
    if "chest pain" in text and "breathing" not in text:
        return (
            "Chest pain can have many causes, including muscle strain, heart, or lung issues. "
            "Avoid heavy activity and monitor your symptoms. "
            "If pain is severe, spreads to arm or jaw, or you feel breathless or sweaty, seek emergency care."
        )

    # Shortness of breath
    if "shortness of breath" in text or "breathing difficulty" in text or "wheezing" in text:
        return (
            "Breathing difficulty or wheezing may be related to asthma, infection, or heart problems. "
            "Sit upright, stay calm, and avoid exertion. "
            "If breathing is getting worse or very fast, go to emergency care."
        )

    # Joint / body pain
    if "joint pain" in text or "knee pain" in text or "back pain" in text or "body pain" in text:
        return (
            "Joint or body pain may be due to strain, posture, or infection. "
            "Use rest, gentle stretching, and simple pain relief if needed. "
            "If pain is severe, with swelling, redness, or fever, consult a doctor."
        )

    # Skin rash / itching
    if "rash" in text or "itching" in text or ("skin" in text and "red" in text):
        return (
            "Skin rash or itching can be due to allergy, infection, or irritation. "
            "Avoid scratching, use gentle soap, and keep the area clean. "
            "If rash is spreading, painful, or with breathing difficulty or swelling, seek urgent care."
        )

    # Sore throat / cold only
    if "sore throat" in text or "cold" in text or "runny nose" in text or "sneezing" in text:
        return (
            "Sore throat, runny nose, or sneezing often suggest a common cold or mild infection. "
            "Drink warm fluids, rest, and use salt‑water gargles. "
            "If symptoms last more than a week or breathing/swallowing is very difficult, see a doctor."
        )

    # Dizziness
    if "dizzy" in text or "dizziness" in text or "lightheaded" in text:
        return (
            "Dizziness can be related to low blood pressure, dehydration, or ear problems. "
            "Sit or lie down safely and drink water slowly. "
            "If dizziness is severe, with chest pain, weakness, or confusion, seek urgent medical care."
        )

    # Default
    return (
        "I can give only general health guidance based on your description. "
        "Your symptoms may need a professional medical evaluation. "
        "Please consult a qualified doctor for a proper diagnosis and treatment."
    )