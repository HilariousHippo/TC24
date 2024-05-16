# Welcome to your Lab Manual!

## 🔑 Your Tableau Cloud Credentials

- Your username is `@lab.CloudCredential(TC24HoT1797).Username`
- Your password is `@lab.CloudCredential(TC24HoT1797).Password`

> This credential is assigned to ***only you***. Please don’t share it with anyone else. These credentials are only available during the hands-on training session that you are currently attending.

---

# Let's Get Started!

## 💫 Step 1. Access Tableau Cloud

1. Click the Google Chrome Shortcut on your VM. You will see the Tableau Cloud sign-in page.
2. Copy & paste your `@lab.CloudCredential(TC24HoT1797).Username` into Tableau Cloud’s sign-in page and click [Sign In].
3. You will be redirected to Auth0’s sign-in page. Don’t worry, you are at the right place. Type again your `@lab.CloudCredential(TC24HoT1797).Username` and `@lab.CloudCredential(TC24HoT1797).Password`. Click [Continue].
4. You should now be signed in to Tableau Cloud!

---

# ✍ Chapter 1: Build & Publish

## 💡 Key Points

- In this chapter, you will create a workbook using the existing published data source.
- You will experience how to create Tableau’s dashboard.
- By publishing your workbook to Tableau Cloud, your content will be available to anyone who has the right permissions.

## 📚 Resource Links

- [Getting Started with web authoring](https://help.tableau.com/current/pro/desktop/en-us/getstarted_web_authoring.htm)
- [Best Practices for Published Data Sources](https://help.tableau.com/current/pro/desktop/en-us/publish_datasources_about.htm)

## 📝 Exercise 1.1 - Create Workbook

1. 🚨 **Go to your assigned folder** 🚨
2. Within your assigned folder, click the ‘New’ dropdown and select ‘Workbook’.
3. In the [Connect to Data] window, make sure you are in the [On This Site] tab (default). Under Data Sources, click "See All" on the right side and find the certified data source ‘World Languages’.
4. Select the "World Languages" datasource and click ‘Connect’.

---

## 📝 Exercise 1.2 - Create Worksheets

### **Step 1: Language by Location**

Create "Language by Location" worksheet, which has a map with [Total Speakers] by [Country].

1. Drag 'Country' to the canvas where Tableau asks ‘Drop field here’.
2. Drop 'Total Speakers (millions)' onto 'Size' on the Marks card.
3. Right-click on 'Sheet1' tab at the bottom and choose 'Rename'.
4. Rename it to `Language by Location`.

### **Step 2: Native vs. Second Language**

Create "Native vs. Second Language" worksheet, which has a scatter plot with [Native Speakers] and [Second Language Speakers] by [Language].

1. Select the ‘New Worksheet’ icon at the bottom, next to the ‘Language by Location’ sheet to create a new worksheet.
2. Multi-select 'Language', 'Native Speakers', and 'Second Language Speakers (millions)'.
   - Mac: Hold 'Command' and select each field.
   - Windows: Hold ‘Ctrl’ and select each field.
3. Click 'Show Me' in the top right corner and choose the highlighted viz, 'scatter-plot'.
4. Change Mark from 'Automatic' to 'Circle'.
5. Click 'Color' on the Marks Card, choose 'Border' dropdown, and select black.
6. Drag the field ‘Language’ in the Marks Card to ‘Label’.
7. Right-click on 'Sheet 2' at the bottom and rename it to `Native vs. Second Language`.

### **Step 3: Total Speakers by Language**

Create "Total Speakers by Language" worksheet, which has a bar chart with [Native Speakers] by [Languages], and [Second Language Speakers] in Color.

1. Click the 'New Worksheet' icon.
2. Drag 'Total Speakers (millions)' to Columns.
3. Drag 'Language' to Rows.
4. Sort descending.
5. Drag ‘Native Speakers (millions) to ‘Color’ on the Marks card.
6. Rename the worksheet to `Total Speakers by Language`.

---

## 📝 Exercise 1.3 - Create and Publish Dashboard

### **Step 1: World Languages Analytics**

Bring three worksheets into a single dashboard and use a map and bar chart as filters. Name it "World Languages Analytics".

1. Click the 'New Dashboard' icon.
2. Drag 
   - 'Language by Location' worksheet to the dashboard.
   - 'Native vs. Second Language' under 'Language by Location' worksheet.
   - 'Total Speakers by Language' worksheet to the right side of the dashboard.
3. Remove 'Total Speakers (millions)' Legend from the top right corner. 
4. Set filters
   - Click ‘Language by Location’ worksheet on the dashboard, and 4 small icons will appear on the top right. Select 'Use as filter'.
   - Repeat the same on ‘Total Speakers by Language’ worksheet to set a filter.
5. Check the box in the bottom left “Show Dashboard Title”.
6. Right-click on **‘Dashboard 1” tab at the bottom** and rename it to `World Languages Analytics`. Click ‘OK’.

---

# 🎁 Done already? Here’s your bonus!

- Feel free to create more worksheets!
- Explore interesting findings from the dataset

---

# 🚀 Wrap Up

## Congratulations on completing the Getting Started with Tableau Cloud Lab!

Throughout this session, you've embarked on a journey to harness the power of Tableau Cloud, from accessing your credentials to building and publishing workbooks, interacting with published content, administering permissions, and exploring Tableau Pulse AI capabilities.

As you wrap up, remember that Tableau Cloud offers a dynamic platform for data exploration, visualization, collaboration, and administration. Whether you're a data analyst, business user, or administrator, Tableau Cloud equips you with the tools to transform data into actionable insights.

Continue to explore the rich resources available to you, including the links provided in this manual, to deepen your understanding and proficiency with Tableau Cloud. Keep innovating, experimenting, and discovering new ways to leverage data to drive informed decision-making and propel your organization forward.

Thank you for your participation, and we look forward to seeing your continued success with Tableau Cloud!
