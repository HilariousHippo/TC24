import streamlit as st

# Define markdown content for each section
markdown_sections = {
    "Welcome": """
    # Welcome to your Lab Manual!
    "🔑 Your Tableau Cloud Credentials": """
        Your user name is **@lab.CloudCredential(TC24HoT1797).Username**.
        Your password is **@lab.CloudCredential(TC24HoT1797).Password**.
        This credentials are assign to only you. Please do not share this with anyone else.
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
    "📝 Exercise 1.3 - Create and Publish Dashboard": """
        #### **Step 1**
        Bring three worksheets into a single dashboard and use map and barchart as filters. Name it to "World Languages Analytics".
        - Click the 'New Dashboard' icon.
        - Drag 
            - 'Language by Location' worksheet to the dashboard.
            - 'Native vs. Second Language' under 'Language by Location' worksheet.
            - 'Total Speakers by Language' worksheet to the right side of the dashboard.
        - Remove 'Total Speakers (millions)' Legend from the top right corner. 
        - Set filters
            - Click ‘Language by Location’ worksheet on dashboard, and 4 small icons will appear on top right. Select 'Use as filter'.
            - Repeat the same on ‘Total Speaker by Language’ worksheet to set a filter.
        - Check the box in the bottom left “Show Dashboard Title”.
        - Right-click on **‘Dashboard 1” tab at the bottom** and rename it to `World Languages Analytics`. Click ‘OK’.

        #### **Step 2**
        Publish workbook to your folder. Name your workbook "World Languages_your number".
        - Select 'Publish As' on upper right.
        - Name the workbook `World Languages` with your project number following: for example “World Languages 042’.
        - Make sure your folder is pre-selected. If not, find your folder.
        - Select ‘Publish’.
        - Lastly, select ‘Go to Workbook’ on the notification at the top of the page.
        """,
    "✍ Chapter 2: Interact": """
        ### 💡 Key Points
        - In this chapter, you will see what options are available to the end user when working off of a published workbook.
        - Filter, Comment, Download
        - Set subscriptions, data-driven alerts, custom views
        """,
    "📝 Exercise 2 Interact with Dashboard": """
        #### **Step 1 - Filter & Comment**
        Click "India" on map and observe findings. Add comment to @Duncan Wingfield with a snapshot and your findings!
        - Click [World Languages Analytics] dashboard you just created.
        - Select "India" on the map to filter your dashboard.
        - Notice in India, there are multiple languages spoken. Not just Hindi. This is interesting, let's share this insight.
        - Click "Add or View Comments" on upper right menu.
        - In the comment, "@Duncan Wingfield" and add whatever comment you like to add. Click little icon below to attach a snapshot of your dashboard. Click "Post".
        - Click "Reset View" to reset your dashboard.

        #### **Step 2 - Download**
        Click "Download" to see the available options for end users.
        - On the top right, select the 'download' dropdown to explore options available to the end user. You can manage permission in the real business scenario.

        #### **Step 3 - Subscriptions**
        Set up your subscription to receive a snapshot of this dashboard at your desired cadence.
        - Click the 'Watch' dropdown and select 'Subscriptions'.
        - Check the box '""",
    "🚀 Wrap Up": """
        ## Congratulations on completing the Getting Started with Tableau Cloud Lab! 

        Throughout this session, you've embarked on a journey to harness the power of Tableau Cloud, from accessing your credentials to building and publishing workbooks, interacting with published content, administering permissions, and exploring Tableau Pulse AI capabilities.

        As you wrap up, remember that Tableau Cloud offers a dynamic platform for data exploration, visualization, collaboration, and administration. Whether you're a data analyst, business user, or administrator, Tableau Cloud equips you with the tools to transform data into actionable insights.

        Continue to explore the rich resources available to you, including the links provided in this manual, to deepen your understanding and proficiency with Tableau Cloud. Keep innovating, experimenting, and discovering new ways to leverage data to drive informed decision-making and propel your organization forward.

        Thank you for your participation, and we look forward to seeing your continued success with Tableau Cloud!
        """
}

# Render the markdown content with a button at the bottom
def render_markdown_with_button(section_content):
    st.markdown(section_content, unsafe_allow_html=True)
    st.write("")  # Add a space for layout
    st.button("Go to Next Section", key=section_content[:20])  # Button to navigate to next section

# Main function to run the app
def main():
    st.sidebar.title("Navigation Bar")
    selected_section = st.sidebar.radio("Go to", list(markdown_sections.keys()))

    st.title(selected_section)
    render_markdown_with_button(markdown_sections[selected_section])

if __name__ == "__main__":
    main()
