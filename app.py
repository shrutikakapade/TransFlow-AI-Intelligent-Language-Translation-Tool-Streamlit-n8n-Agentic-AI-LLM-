import streamlit as st
import requests

# ---------- Page config ----------
st.set_page_config(
    page_title="TransFlow AI ",
    page_icon="🌐",
    layout="centered",
)

# ---------- Custom CSS ----------
st.markdown(
    """
    <style>
    /* Main page background */
    .stApp {
        background: radial-gradient(circle at top left, #101729, #05060b 55%);
        color: #f5f5f7;
        font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    /* Remove block gaps */
    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 2.5rem;
        max-width: 850px;
    }

    /* Glassmorphism card */
    .glass-card {
        background: rgba(15, 23, 42, 0.85);
        border-radius: 20px;
        padding: 1.8rem 1.8rem 1.6rem 1.8rem;
        border: 1px solid rgba(148, 163, 184, 0.35);
        box-shadow: 0 22px 45px rgba(15, 23, 42, 0.7);
        backdrop-filter: blur(18px);
    }

    .app-title {
        font-size: 2.4rem;
        font-weight: 700;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        background: linear-gradient(120deg, #38bdf8, #a855f7, #f97316);
        -webkit-background-clip: text;
        color: transparent;
        text-align: center;
        margin-bottom: 0.25rem;
    }

    .app-subtitle {
        text-align: center;
        color: #9ca3af;
        font-size: 0.95rem;
        margin-bottom: 2.2rem;
    }

    .label-text {
        font-size: 0.9rem;
        font-weight: 600;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        color: #9ca3af;
        margin-bottom: 0.35rem;
    }

    textarea, .stTextArea textarea {
        border-radius: 12px !important;
        border: 1px solid #1f2937 !important;
        background-color: #020617 !important;
        color: #e5e7eb !important;
        font-size: 0.95rem !important;
    }

    textarea:focus, .stTextArea textarea:focus {
        border: 1px solid #38bdf8 !important;
        box-shadow: 0 0 0 1px #38bdf8 !important;
    }

    /* Primary button */
    .stButton > button {
        width: 100%;
        border-radius: 999px;
        border: none;
        padding: 0.55rem 1.1rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        font-size: 0.8rem;
        background: linear-gradient(135deg, #38bdf8, #a855f7);
        color: white;
        box-shadow: 0 12px 25px rgba(56, 189, 248, 0.35);
        transition: all 0.18s ease-out;
    }

    .stButton > button:hover {
        box-shadow: 0 16px 32px rgba(88, 28, 135, 0.65);
        transform: translateY(-1px);
        opacity: 0.96;
    }

    .stButton > button:active {
        transform: translateY(1px) scale(0.99);
        box-shadow: 0 7px 18px rgba(15, 23, 42, 0.9);
    }

    /* Output box */
    .output-box {
        margin-top: 1.2rem;
        padding: 1rem 1.2rem;
        border-radius: 14px;
        border: 1px solid rgba(55, 65, 81, 0.8);
        background: radial-gradient(circle at top left, rgba(15,23,42,0.95), rgba(15,23,42,0.75));
        font-size: 0.95rem;
        color: #e5e7eb;
    }

    .pill {
        display: inline-flex;
        align-items: center;
        gap: 0.3rem;
        border-radius: 999px;
        padding: 0.25rem 0.8rem;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        border: 1px solid rgba(148, 163, 184, 0.5);
        color: #9ca3af;
        background: rgba(15, 23, 42, 0.9);
    }

    .footer-note {
        margin-top: 1.6rem;
        text-align: center;
        font-size: 0.75rem;
        color: #6b7280;
    }

    /* Hide default footer and menu */
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Header ----------
st.markdown('<div class="app-title">TransFlow AI </div>', unsafe_allow_html=True)
st.markdown(
    '<div class="app-subtitle">Effortless translation, global clarity. Integrated with n8n automation.</div>',
    unsafe_allow_html=True,
)

# ---------- Main Card ----------
with st.container():
    # st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    # # Top pills
    # col_p1, col_p2, col_p3 = st.columns([1.2, 1, 1])
    # with col_p1:
    #     st.markdown('<span class="pill">🌐 Live translation</span>', unsafe_allow_html=True)
    # with col_p2:
    #     st.markdown('<span class="pill">⚡ n8n webhook</span>', unsafe_allow_html=True)
    # with col_p3:
    #     st.markdown('<span class="pill">🛠️ Streamlit</span>', unsafe_allow_html=True)

    st.markdown("")
    st.markdown('<div class="label-text">Enter text</div>', unsafe_allow_html=True)
    text = st.text_area("", placeholder="Write something to translate...", height=130)

    col_btn, _ = st.columns([1.1, 1])
    with col_btn:
        submit = st.button("Translate")

    if submit:
        if text.strip():
            with st.spinner("Translating via n8n..."):
                try:
                    response = requests.post(
                        url="https://shrutika2125.app.n8n.cloud/webhook-test/97b0edee-c0f1-4e88-bca1-2b5625e041c4",
                        json={"input": text},
                        timeout=20,
                    )
                    if response.status_code == 200:
                        data = response.json()
                        output_text = data.get("output", "")
                        if output_text:
                            st.markdown(
                                f'<div class="output-box"><span class="label-text" style="margin-bottom:0.4rem;">Translation</span><br>{output_text}</div>',
                                unsafe_allow_html=True,
                            )
                        else:
                            st.warning("Translation received but output field was empty.")
                    else:
                        st.error(f"Request failed with status code {response.status_code}.")
                except Exception as e:
                    st.error(f"Something went wrong while calling the translation service: {e}")
        else:
            st.warning("Please enter some text before translating.")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown(
    '<div class="footer-note">Built with ❤️ using Streamlit and n8n.</div>',
    unsafe_allow_html=True,
)
