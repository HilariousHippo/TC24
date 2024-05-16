import streamlit as st

# Define markdown content for each section
markdown_sections = {
    "🔑 Your Tableau Cloud Credentials": """
        Your user name is **@lab.CloudCredential(TC24HoT1797).Username**.
        Your password is **@lab.CloudCredential(TC24HoT1797).Password**.
        This credentials are assign to only you. Please don’t share this with anyone else.
        """,
    "Let's get it started!": """
        ### 💫 Step 1. Access Tableau Cloud
        Click the Google Chrome Shortcut on your VM. You will see Tableau Cloud sign-in page.
        Copy & paste your `@lab.CloudCredential(TC24HoT1797).Username` into Tableau Cloud’s sign-in page and click [Sign In].
        You will be redirected to Auth0’s sign-in page. Type again your `@lab.CloudCredential(TC24HoT1797).Username` 
        and `@lab.CloudCredential(TC24HoT1797).Password`. Click [Continue].
        """,
    "✍ Chapter 1: Build & Publish": """
        ### 💡 Key Points
        - In this chapter, you will create a workbook using the existing published data source.
        - You will experience how to create Tableau’s dashboard.
        - By publishing your workbook to Tableau Cloud, your content will be available to anyone who has the right permissions.
        """,
    "📝 Exercise 1.1 - Create Workbook": """
        1. **Go to your assigned folder**
        Within your assigned folder, click the ‘New’ dropdown and select ‘Workbook’.
        In [Connect to Data] window, make sure you are in [On This Site] tab. (It's default) 
        Under Data Sources, click "See All" on right side and find the certified data source ‘World Languages’.
        Select "World Languages" datasource and click ‘Connect’.
        """,
    "📝 Exercise 1.2 - Create Worksheets": """
        #### **Step 1**
        Create "Language by Location" worksheet, which has a map with [Total Speakers] by [Country].
        - Drag 'Country' to the canvas where Tableau asks ‘Drop field here’.
        - Drop 'Total Speakers (millions)' onto 'Size' on the Marks card.
        - Right-click on 'Sheet1' tab at the bottom and choose 'Rename'.
        - Rename it to `Language by Location`.

        #### **Step 2**
        Create "Native vs. Second Language" worksheet, which has a scatter plot with [Native Speakers] and [Second Language Speakers] by [Language].
        - Select the ‘New Worksheet’ icon at the bottom, next to the ‘Language by Location’ sheet to create new worksheet.
        - Multi-select 'Language', 'Native Speakers', and 'Second Language Speakers (millions)'
            - Mac: Hold 'Command' and select each fields.
            - Windows: Hold ‘Ctrl’ and select each fields.
        - Click 'Show Me' in the top right corner and choose the highlighted viz, 'scatter-plot'.
        - Change Mark from 'Automatic' to 'Circle'.
        - Click 'Color' on the Marks Card, choose 'Border' dropdown, and select black.
        - Drag the field ‘Language’ in the Marks Card to ‘Label’.
        - Right-click on 'Sheet 2' at the bottom and rename it to `Native vs. Second Language`.

        #### **Step 3**
        Create "Total Speakers by Language" worksheet, which has a barchart with [Native Speakers] by [Languages], and [Second Language Speakers] in Color.
        - Click the 'New Worksheet' icon.
        - Drag 'Total Speakers (millions)' to Columns.
        - Drag 'Language' to Rows.
        - Sort descending.
        - Drag ‘Native Speakers (millions) to ‘Color’ on the Marks card.
        - Rename worksheet to `Total Speakers by Language`.
        """,
    # Add more sections here...
}

# Sidebar navigation
selected_section = st.sidebar.selectbox("Navigate to", list(markdown_sections.keys()))

# Render selected markdown content
st.markdown(markdown_sections[selected_section])
