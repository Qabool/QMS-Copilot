import streamlit as st
from config.settings import get_api_key
from rag.vector_store import LocalFAISSRetriever
from ui.dashboard import render_dashboard
from ui.document_inventory import render_document_inventory
from ui.gap_analysis import render_gap_analysis
from ui.audit_simulator import render_audit_simulator

st.set_page_config(
    page_title="QMS-Copilot — ISO 9001 Compliance & Audit Agent",
    page_icon="🛡️",
    layout="wide"
)

@st.cache_resource
def load_rag():
    return LocalFAISSRetriever()

def main():
    st.sidebar.title("🛡️ QMS-Copilot")
    st.sidebar.caption("ISO 9001 Compliance & Audit Agent")
    
    rag_retriever = load_rag()
    
    page = st.sidebar.radio(
        "Navigation",
        ["Dashboard", "Document Inventory", "Gap Analysis", "Audit Simulator", "Settings"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("Certification Basis")
    cert_basis_confirmed = st.sidebar.checkbox("Confirm Certification Basis", value=True)
    if not cert_basis_confirmed:
        st.warning("⚠️ Certification basis requires confirmation before performing compliance analysis.")
        return

    if page == "Dashboard":
        render_dashboard()
    elif page == "Document Inventory":
        render_document_inventory()
    elif page == "Gap Analysis":
        render_gap_analysis(rag_retriever)
    elif page == "Audit Simulator":
        render_audit_simulator(rag_retriever)
    elif page == "Settings":
        st.header("⚙️ QMS-Copilot Settings")
        api_key = get_api_key("gemini")
        st.text_input("Gemini API Key (loaded from secrets)", value="********" if api_key else "", type="password", disabled=True)
        st.success("API Key successfully loaded via Streamlit secure configuration.")
        st.info("FAISS Knowledge Base loaded from `data/vectorstore/iso_faiss_index`.")

if __name__ == "__main__":
    main()