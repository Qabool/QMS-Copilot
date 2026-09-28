import streamlit as st

def render_dashboard():
    st.title("📊 QMS Recertification Readiness Workspace")
    st.caption("Transform your existing QMS into an evidence-based, audit-ready management system.")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total QMS Documents", "24", "+2 revisions")
    with col2:
        st.metric("Documents Reviewed", "18", "75%")
    with col3:
        st.metric("Evidence Gaps", "5", "Requires Action", delta_color="inverse")
    with col4:
        st.metric("Readiness Status", "YELLOW", "Partial Evidence")

    st.markdown("---")
    st.subheader("30-Day Recertification Workflow Status")
    
    phases = [
        ("Phase 1: QMS Discovery", "Completed", "green"),
        ("Phase 2: ISO Requirement Mapping", "Completed", "green"),
        ("Phase 3: QMS Gap Analysis", "In Progress", "orange"),
        ("Phase 4: Change Impact Analysis", "Pending", "gray"),
        ("Phase 5: Document Regeneration", "Pending", "gray"),
        ("Phase 6: Forms & Evidence Regeneration", "Pending", "gray"),
        ("Phase 7: Evidence Verification", "Pending", "gray"),
        ("Phase 8: Mock Audit", "Pending", "gray"),
        ("Phase 9: Corrective Action", "Pending", "gray"),
        ("Phase 10: Final Audit Readiness Review", "Pending", "gray")
    ]
    
    for phase, status, color in phases:
        st.markdown(f"**{phase}** — :{color}[{status}]")
