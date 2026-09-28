import streamlit as st

def render_audit_simulator(rag_retriever):
    st.title("🎯 ISO 9001 Audit Simulator")
    st.caption("Simulate a rigorous ISO 9001 certification auditor seeking objective evidence.")
    
    if "audit_chat" not in st.session_state:
        st.session_state.audit_chat = [
            {"role": "auditor", "text": "Please demonstrate how the organization determines competence requirements for personnel performing work affecting QMS performance (Clause 7.2)."}
        ]
        
    for msg in st.session_state.audit_chat:
        if msg["role"] == "auditor":
            st.markdown(f"🧑‍⚖️ **AUDITOR:** {msg['text']}")
        else:
            st.markdown(f"👤 **AUDITEE (You):** {msg['text']}")
            
    user_response = st.text_input("Provide your response / objective evidence reference:")
    if st.button("Submit Evidence / Response"):
        if user_response:
            st.session_state.audit_chat.append({"role": "auditee", "text": user_response})
            retrievals = rag_retriever.similarity_search("competence resources", k=1)
            source_info = retrievals[0]['metadata'].get('chunk_id', 'ISO9001-2026')
            st.session_state.audit_chat.append({
                "role": "auditor", 
                "text": f"Thank you. Verified against [{source_info}]. Please provide the specific document reference or record ID where this competence matrix is archived."
            })
            st.rerun()