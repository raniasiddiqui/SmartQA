import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="AI QA Automation Suite",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'active_tool' not in st.session_state:
    st.session_state.active_tool = "Home"

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
    <style>
    .main-header {
        font-size: 3.4rem !important;
        font-weight: 900 !important;
        background: linear-gradient(120deg, #1f77b4 0%, #00d4ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin: 1.5rem 0 0.5rem 0;
        animation: fadeIn 1.2s ease-in;
        line-height: 1.1;
    }
    
    .tool-header {
        font-size: 3.2rem !important;
        font-weight: 800 !important;
        background: linear-gradient(120deg, #1f77b4 0%, #00d4ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin: -0.5rem 0 1.5rem 0;
        padding-top: 1rem;
        animation: fadeIn 1s ease-in;
    }
    
    .subtitle {
        text-align: center;
        color: #555;
        font-size: 1.3rem;
        margin-bottom: 1.8rem;
        font-weight: 400;
    }
    
    .tool-card {
        padding: 2.2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin: 0.6rem 0;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        color: white;
        height: 100%;
        /* Unified Indigo Gradient for ALL cards */
        background: linear-gradient(135deg, #5a67d8 0%, #764ba2 70%) !important;
    }
    
    .tool-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.3);
    }
    
    .tool-icon { font-size: 3.4rem; margin-bottom: 0.8rem; display: block; }
    .tool-title { font-size: 1.8rem; font-weight: 700; margin-bottom: 0.8rem; }
    .tool-description { font-size: 1.1rem; margin-bottom: 1.2rem; opacity: 0.95; line-height: 1.5; }
    
    /* Sidebar Button Styling - Left aligned + Active State */
    .css-1cpxl2t {  /* This targets sidebar buttons */
        text-align: left !important;
        justify-content: flex-start !important;
    }
    
    /* Active button highlight */
    div[data-testid="stSidebar"] button[kind="secondary"] {
        background-color: transparent !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 0.75rem 1.2rem !important;
        font-weight: 500 !important;
        font-size: 1.05rem !important;
    }
    
    /* When button is active (clicked) */
    div[data-testid="stSidebar"] button[aria-selected="true"],
    div[data-testid="stSidebar"] button:hover {
        background: rgba(102, 126, 234, 0.35) !important;
        backdrop-filter: blur(10px);
        border-left: 4px solid #667eea !important;
        font-weight: 600 !important;
        color: #ffffff !important;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .footer {
        text-align: center;
        color: #666;
        padding: 2.5rem 1rem;
        margin-top: 4rem;
        border-top: 2px solid #eee;
        font-size: 0.95rem;
    }

    .ai-disclaimer {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: rgba(0,0,0,0.82);
        color: #f0f0f0;
        padding: 10px 16px;
        border-radius: 10px;
        font-size: 0.84rem;
        z-index: 999;
        max-width: 360px;
        line-height: 1.4;
        box-shadow: 0 6px 16px rgba(0,0,0,0.45);
        border: 1px solid rgba(255,255,255,0.12);
    }
    
    .ai-disclaimer strong {
        color: #ffcc00;
    }
    </style>
""", unsafe_allow_html=True)

# ── Tool URLs ────────────────────────────────────────────────────────────────
FSD_LEARNING_URL = "https://automated-fsd-generator.streamlit.app/"
TEST_CASE_GEN_URL = "https://automated-testcase-generation.streamlit.app/"
TEST_CASE_SCRIPT_URL = "https://automated-execution.streamlit.app/"
EXECUTION_REFINEMENT_URL = "https://automated-execution-refiner.streamlit.app/"
BUG_INTELLIGENCE_URL = "https://automated-bug-prediction.streamlit.app/"
UAT_TESTCASE_GEN_URL = "https://uat-testcase-generator.streamlit.app/"

def embed_app(url, height=1000):
    embed_url = f"{url}?embed=true"
    components.iframe(embed_url, height=height, scrolling=True)

# ── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🎯 Quick Navigation")
    st.markdown("---")
    
    # Home Button
    if st.button("🏠 Home", use_container_width=True, key="home"):
        st.session_state.active_tool = "Home"
        st.rerun()
    
    tools = [
        ("📚 Requirements Learning", "Requirements Learning"),
        ("📝 QA Test Case Generation", "QA Test Case Generation"),
        ("✅ UAT Test Case Generation", "UAT Test Case Generation"),
        ("▶️ Automation test script generation", "Automation test script generation"),
        ("🔧 Automation test script refinement", "Automation test script refinement"),
        ("🪲 Bug Prediction", "Bug Prediction")
    ]
    
    for label, key in tools:
        if st.button(label, use_container_width=True, key=key):
            st.session_state.active_tool = key
            st.rerun()
    
    st.markdown("---")
    st.markdown("### 📊 Dashboard Stats")
    st.metric("Active AI Engines", "7")  # Including Home as command center
    
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.markdown("All-in-one AI-powered QA automation dashboard")

# ── MAIN CONTENT ─────────────────────────────────────────────────────────────
if st.session_state.active_tool == "Home":
    st.markdown('<p class="main-header">🤖 Smart QA</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="subtitle">Elevate Testing with Intelligence • Accelerate Delivery with Confidence</p>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🧠 Intelligent Tools", "6")
    with col2:
        st.metric("⚡ Tests Automated", "Testing Simplified")
    with col3:
        st.metric("🚀 Time Saved", "Focus on What Matters")

    st.markdown("---")

    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #f8fafc, #eef2ff);
            border: 1px solid #c7d2fe;
            border-radius: 18px;
            padding: 2.2rem;
            box-shadow: 0 8px 28px rgba(0,0,0,0.08);
            margin: 1.5rem 0;
        ">
            <h2 style="color:#1e40af; margin-bottom:0.8rem; font-size:2.1rem;">
                👋 Welcome to the Smart QA
            </h2>
            <p style="font-size:1.15rem; color:#334155; line-height:1.75;">
                This is not just a tool — it's your <strong>AI Co-Pilot for flawless software delivery</strong>.<br>
                From smart requirement analysis to predictive bug hunting, everything you need to ship faster, better, and bolder.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")

    st.subheader("🚀 Jump Right In")
    qs1, qs2 = st.columns(2)
    with qs1:
        st.info("**1️⃣ Navigate** → Use the left sidebar\n\n**2️⃣ Select** → Click any tool to launch instantly")
    with qs2:
        st.success("**Zero Setup** → Works in your browser\n\n**Return Home Anytime** -> Click 🏠 Home to come back here.")

    st.markdown("---")

else:
    st.markdown('<p class="tool-header">🤖 Smart QA</p>', unsafe_allow_html=True)

    col_main, col_tips = st.columns([7, 3.2])

    tool_data = {
        "Requirements Learning": {
            "icon": "📚", "title": "Requirements Learning",
            "desc": "Transform Functional Specification Documents into actionable insights with AI-powered analysis.",
            "features": "• Document parsing & analysis<br>• Requirement extraction<br>• Feature identification<br>• AI-powered insights",
            "tips": "• Upload FSD in PDF, DOCX or txt\n• Choose analysis mode\n• Review AI insights carefully"
        },
        "QA Test Case Generation": {
            "icon": "📝", "title": "QA Test Case Generation",
            "desc": "Generate comprehensive test cases automatically from requirements using AI.",
            "features": "• Automated test case creation<br>• Multiple test types<br>• Coverage optimization<br>• Smart scenarios",
            "tips": "• Upload requirements or type them\n• Choose test types\n• Adjust coverage level"
        },
        "Automation test script generation": {
            "icon": "▶️", "title": "Automation test script generation",
            "desc": "Convert test cases into executable Playwright scripts with AI assistance.",
            "features": "• Auto conversion to scripts<br>• Smart locator handling<br>• Multi-step workflows",
            "tips": "• Select target environment\n• Choose browsers\n• Watch live progress"
        },
        "Automation test script refinement": {
            "icon": "🔧", "title": "Automation test script refinement",
            "desc": "Optimize test execution with AI-powered insights and smart recommendations.",
            "features": "• Flaky test detection<br>• Script optimization<br>• Playwright selectors<br>• Performance analysis",
            "tips": "• Upload execution scripts\n• Upload playwright results\n• Review recommendations"
        },
        "Bug Prediction": {
            "icon": "🪲", "title": "Bug Prediction",
            "desc": "Predict, analyze and prioritize bugs using advanced AI techniques.",
            "features": "• Bug prediction<br>• Pattern detection<br>• Proactive insights",
            "tips": "• Upload previous bugs\n• Choose prediction mode\n• Focus on high-risk items"
        },
        "UAT Test Case Generation": {
            "icon": "✅", "title": "UAT Test Case Generation",
            "desc": "Create professional User Acceptance Testing test cases tailored for business validation.",
            "features": "• Business-oriented test cases<br>• Happy path scenarios<br>• Acceptance criteria focus<br>• Stakeholder-friendly format",
            "tips": "• Provide user stories or requirements\n• Specify business flows\n• Review for stakeholder approval"
        }
    }

    current = tool_data.get(st.session_state.active_tool, tool_data["Requirements Learning"])

    with col_main:
        st.markdown(f"""
        <div class="tool-card">
            <span class="tool-icon">{current['icon']}</span>
            <div class="tool-title">{current['title']}</div>
            <p class="tool-description">{current['desc']}</p>
            <details>
                <summary><strong>🔑 Key Features</strong></summary>
                <div style="margin-top: 0.8rem; font-size: 1rem; line-height: 1.6;">
                    {current['features']}
                </div>
            </details>
        </div>
        """, unsafe_allow_html=True)

    with col_tips:
        with st.expander("💡 Quick Tips", expanded=True):
            st.markdown(current["tips"].replace("•", "→"))

    st.markdown(f"### 🚀 Using {st.session_state.active_tool} right now:")
    st.markdown("")

    url_map = {
        "Requirements Learning": FSD_LEARNING_URL,
        "QA Test Case Generation": TEST_CASE_GEN_URL,
        "Automation test script generation": TEST_CASE_SCRIPT_URL,
        "Automation test script refinement": EXECUTION_REFINEMENT_URL,
        "Bug Prediction": BUG_INTELLIGENCE_URL,
        "UAT Test Case Generation": UAT_TESTCASE_GEN_URL
    }
    
    selected_url = url_map.get(st.session_state.active_tool, FSD_LEARNING_URL)
    embed_app(selected_url, height=1000)

# ── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("""
    <div class="footer">
        <strong>Built with ❤️ using Streamlit & Cutting-Edge AI</strong><br>
        Smart QA Automation Suite • Because Quality Should Never Be a Bottleneck
    </div>
""", unsafe_allow_html=True)

# ── FLOATING DISCLAIMER ──────────────────────────────────────────────────────
st.markdown("""
    <div class="ai-disclaimer">
        ⚠️ <strong>SmartQA is AI-powered, in-house developed tool.<br>
        It can make mistakes — please always verify your results.</strong>
    </div>
""", unsafe_allow_html=True)
