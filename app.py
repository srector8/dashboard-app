import streamlit as st

def main():
    st.title('Dashboard Links')
    
    # Define your dashboard links and corresponding names
    dashboard_links = {
        'Survey Dashboard': 'https://survey-dash1-7kv2sru2jx36mk3qrwdr2d.streamlit.app/',
        'App Card Dashboard': 'https://app-card-dash-gfrsvbpbw67oqz8man8phw.streamlit.app/'
    }
    
    # Display each dashboard link as a button or a tile
    for name, link in dashboard_links.items():
        st.markdown(f"## {name}")
        st.markdown(f"[Open {name}]({link})")

if __name__ == '__main__':
    main()
