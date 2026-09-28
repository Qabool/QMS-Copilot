import streamlit as st
import pandas as pd

def render_document_inventory():
    st.title("📁 QMS Document Inventory")
    st.caption("Manage, classify, and track all controlled QMS documents and records.")
    
    data = [
        {"Doc ID": "QMS-MAN-01", "Title": "Quality Manual", "Type": "Manual", "Rev": "03", "Status": "CONTROLLED", "Owner": "QMS Manager"},
        {"Doc ID": "QMS-PRO-01", "Title": "Document Control Procedure", "Type": "Procedure", "Rev": "02", "Status": "AI REVIEW", "Owner": "Document Controller"},
        {"Doc ID": "QMS-PRO-07", "Title": "Competence and Training Procedure", "Type": "Procedure", "Rev": "01", "Status": "DRAFT", "Owner": "HR Manager"},
        {"Doc ID": "QMS-PRO-12", "Title": "Internal Audit Procedure", "Type": "Procedure", "Rev": "02", "Status": "CONTROLLED", "Owner": "Lead Auditor"}
    ]
    
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)