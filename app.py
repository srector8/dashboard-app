import streamlit as st

def main():
    st.title('Dashboard Links')

    # Define your dashboard links and corresponding names
    dashboard_links = {
        'Dashboard 1': 'http://yourdashboard1link.com',
        'Dashboard 2': 'http://yourdashboard2link.com',
        'Dashboard 3': 'http://yourdashboard3link.com'
    }

    # Create a beta_container for the tiles
    with st.beta_container():
        # Iterate over dashboard links to create tiles
        for name, link in dashboard_links.items():
            with st.beta_expander(f'{name}', expanded=False):
                st.markdown(f"[Open {name}]({link})")

if __name__ == '__main__':
    main()
