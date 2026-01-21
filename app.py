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
    }
    
    .tool-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.3);
    }
    
    .tool-card.card-1 { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
    .tool-card.card-2 { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
    .tool-card.card-3 { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
    .tool-card.card-4 { background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); }
    .tool-card.card-5 { background: linear-gradient(135deg, #ff6b6b 0%, #ff8e53 100%); }
    .tool-card.card-6 { background: linear-gradient(135deg, #feca57 0%, #ff6b81 100%); }
    
    .tool-icon { font-size: 3.4rem; margin-bottom: 0.8rem; display: block; }
    .tool-title { font-size: 1.8rem; font-weight: 700; margin-bottom: 0.8rem; }
    .tool-description { font-size: 1.1rem; margin-bottom: 1.2rem; opacity: 0.95; line-height: 1.5; }
    
    /* Collapsible Styles */
    details > summary {
        cursor: pointer;
        font-weight: 600;
        list-style: none;
        padding: 10px 0;
        border-top: 1px solid rgba(255,255,255,0.2);
    }
    details > summary:hover {
        opacity: 0.9;
    }
    details[open] > summary {
        margin-bottom: 5px;
    }
    
    .stButton > button {
        width: 100%;
        background: white !important;
        color: #333 !important;
        border: none !important;
        padding: 0.75rem 1.5rem !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        border-radius: 10px !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: scale(1.04) !important;
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

    /* Floating AI disclaimer */
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
    
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.active_tool = "Home"
    
    if st.button("📚 FSD Learning", use_container_width=True):
        st.session_state.active_tool = "FSD Learning"

    if st.button("📝 QA Test Case Generation", use_container_width=True):
        st.session_state.active_tool = "QA Test Case Generation"
    
    if st.button("✅ UAT Test Case Generator", use_container_width=True):
        st.session_state.active_tool = "UAT Test Case Generator"
    
    if st.button("▶️ Test Case Script Generation", use_container_width=True):
        st.session_state.active_tool = "Test Case Script Generation"
    
    if st.button("🔧 Execution Refinement", use_container_width=True):
        st.session_state.active_tool = "Execution Refinement"
    
    if st.button("🪲 AI Bug Intelligence", use_container_width=True):
        st.session_state.active_tool = "AI Bug Intelligence"
    
    
    
    st.markdown("---")
    st.markdown("### 📊 Dashboard Stats")
    st.metric("Active Tools", "6")
    
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.markdown("All-in-one AI-powered QA automation dashboard")

# ── MAIN CONTENT ─────────────────────────────────────────────────────────────
if st.session_state.active_tool == "Home":
    st.markdown('<p class="main-header">🤖 Smart QA</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="subtitle">Streamline your testing workflow with intelligent AI-driven automation tools</p>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
    with col1: st.metric("🧠 AI Tools", "6")
    with col2: st.metric("⚡ Automation", "100%")
    with col3: st.metric("🚀 Potential", "Unlimited")

    st.markdown("---")

    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #f8fafc, #eef2ff);
            border: 1px solid #c7d2fe;
            border-radius: 18px;
            padding: 2rem;
            box-shadow: 0 8px 24px rgba(0,0,0,0.06);
        ">
            <h2 style="color:#1e40af; margin-bottom:0.6rem;">
                👋 Welcome to your Smart QA Command Center
            </h2>
            <p style="font-size:1.1rem; color:#334155; line-height:1.6;">
                This suite brings together <strong>intelligent AI tools</strong> designed to help
                QA engineers, testers, and teams build better software — faster and with confidence.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")

    st.subheader("🚀 Quick Start Guide")
    qs1, qs2 = st.columns(2)
    with qs1:
        st.info("**1️⃣ Use the Sidebar** \nNavigate between tools using the menu on the left.\n\n**2️⃣ Return Home Anytime** \nClick 🏠 Home to come back here.")
    with qs2:
        st.success("**3️⃣ Pick a Tool** \nEach tool includes overview & usage tips\n\n**4️⃣ No Setup Needed** \nEverything runs directly in your browser.")

    st.markdown("---")

else:
    # ── TOOL VIEW ───────────────────────────────────────────────────────────────
    st.markdown('<div class="animate-slide">', unsafe_allow_html=True)

    # Add Smart QA header at top of tool pages
    st.markdown('<p class="tool-header">🤖 Smart QA</p>', unsafe_allow_html=True)

    col_main, col_tips = st.columns([7, 3.2])

    tool_data = {
        "FSD Learning": {
            "class": "card-1", "icon": "📚", "title": "FSD Learning",
            "desc": "Transform Functional Specification Documents into actionable insights with AI-powered analysis.",
            "features": "• Document parsing & analysis<br>• Requirement extraction<br>• Feature identification<br>• AI-powered insights",
            "tips": "• Upload FSD in PDF or DOCX<br>• Choose analysis depth<br>• Review AI insights carefully"
        },
        "QA Test Case Generation": {
            "class": "card-2", "icon": "📝", "title": "QA Test Case Generation",
            "desc": "Generate comprehensive test cases automatically from requirements using advanced AI.",
            "features": "• Automated test case creation<br>• Multiple test types<br>• Coverage optimization<br>• Smart scenarios",
            "tips": "• Upload requirements or type them<br>• Choose test types<br>• Adjust coverage level"
        },
        "Test Case Script Generation": {
            "class": "card-3", "icon": "▶️", "title": "Test Case Script Generation",
            "desc": "Convert test cases into executable Playwright scripts with AI assistance.",
            "features": "• Auto conversion to scripts<br>• Smart locator handling<br>• Multi-step workflows",
            "tips": "• Select target environment<br>• Choose browsers<br>• Watch live progress"
        },
        "Execution Refinement": {
            "class": "card-4", "icon": "🔧", "title": "Execution Refinement",
            "desc": "Optimize test execution with AI-powered insights and smart recommendations.",
            "features": "• Flaky test detection<br>• Script optimization<br>• Playwright selectors<br>• Performance analysis",
            "tips": "• Upload execution results<br>• Select refinement options<br>• Review recommendations"
        },
        "AI Bug Intelligence": {
            "class": "card-5", "icon": "🪲", "title": "AI Bug Intelligence",
            "desc": "Predict, analyze and prioritize bugs using advanced AI techniques.",
            "features": "• Bug prediction<br>• Risk scoring<br>• Pattern detection<br>• Proactive insights",
            "tips": "• Upload code/logs/tests<br>• Choose prediction mode<br>• Focus on high-risk items"
        },
        "UAT Test Case Generator": {
            "class": "card-6", "icon": "✅", "title": "UAT Test Case Generator",
            "desc": "Create professional User Acceptance Testing test cases tailored for business validation.",
            "features": "• Business-oriented test cases<br>• Happy path scenarios<br>• Acceptance criteria focus<br>• Stakeholder-friendly format",
            "tips": "• Provide user stories or requirements<br>• Specify business flows<br>• Review for stakeholder approval"
        }
    }

    current = tool_data.get(st.session_state.active_tool, tool_data["FSD Learning"])

    with col_main:
        st.markdown(f"""
        <div class="tool-card {current['class']}">
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
            st.markdown(current["tips"].replace("<br>", "\n"))

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f"### 🚀 Using {st.session_state.active_tool} right now:")
    st.markdown("")

    url_map = {
        "FSD Learning": FSD_LEARNING_URL,
        "QA Test Case Generation": TEST_CASE_GEN_URL,
        "Test Case Script Generation": TEST_CASE_SCRIPT_URL,
        "Execution Refinement": EXECUTION_REFINEMENT_URL,
        "AI Bug Intelligence": BUG_INTELLIGENCE_URL,
        "UAT Test Case Generator": UAT_TESTCASE_GEN_URL
    }
    
    selected_url = url_map.get(st.session_state.active_tool, FSD_LEARNING_URL)
    embed_app(selected_url, height=1000)

# ── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("""
    <div class="footer">
        <strong>Built with ❤️ using Streamlit & AI</strong><br>
        Smart QA Automation Suite • Making testing smarter<br>
    </div>
""", unsafe_allow_html=True)

# ── FLOATING DISCLAIMER (Option 4) ───────────────────────────────────────────
st.markdown("""
    <div class="ai-disclaimer">
        ⚠️ <strong>SmartQA is AI-powered</strong> and can make mistakes.<br>
        <strong>Always verify</strong> important results yourself before use.
    </div>
""", unsafe_allow_html=True)