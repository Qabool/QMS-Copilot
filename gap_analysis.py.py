import streamlit as st

def render_gap_analysis(rag_retriever):
    st.title("🔍 QMS Gap Analysis & Compliance Status")
    st.caption("Transparent evidence-based status tracking with live ISO RAG lookups.")
    
    query = st.text_input("Query ISO 9001 standard requirement:", value="competence training requirements")
    if st.button("Retrieve Standard Clause"):
        results = rag_retriever.similarity_search(query, k=2)
        for r in results:
            st.info(f"**Retrieved Source metadata:** {r['metadata']}")
            st.markdown(f"> {r['text'][:500]}...")

    st.markdown("---")
    st.markdown("### Clause 7.2 — Competence (Evaluation)")
    st.info("**Status:** YELLOW — Procedure requirement exists, but objective training records for the current audit cycle were not provided.")
    st.markdown("**Evidence Required:** Training attendance sheets, qualification matrices, and effectiveness evaluation records.")