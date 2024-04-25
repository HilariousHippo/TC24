#Welcome to Lab Manual!!
##🔑Your Tableau Cloud Credentials
- Your user name is  **@lab.CloudCredential(TC24HoT1797).Username**
- Your password is **@lab.CloudCredential(TC24HoT1797).Password**

> This credentials is assign to ***only you***. Please don’t share this with anyone else. This credentials are only available during the Hands-on training session that you are currently attending.

</br>

##💫How to access Tableau Cloud
1. Click the Google Chrome Shortcut on your VM. You will see Tableau Cloud sign-in page.
1. Copy& paste your `@lab.CloudCredential(TC24HoT1797).Username` into Tableau Cloud’s sign-in page and click [Sign In].
!IMAGE[Snag_3f42fdf.png](instructions258429/Snag_3f42fdf.png)
1. You will be redirected to Auth0’s sign-in page. Don’t worry, you are at the right place. Type again your `@lab.CloudCredential(TC24HoT1797).Username`and `@lab.CloudCredential(TC24HoT1797).Password`. Click [Continue]
!IMAGE[Snag_3f380a4.png](instructions258429/Snag_3f380a4.png)
1. You should now be signed in to Tableau Cloud!

> [+Hint] See it in action
>
>!VIDEO[How to Sign in.mp4](instructions258429/How to Sign in.mp4)

</br>

##👀 Find your assigned folder
You are assigned to the folder number, which is the same number in your email address - @username. If you see 1 or 2 digit in your user name, add 0 to make it 3 digits. Example below:
> 
| username | your folder |
|:---------|:---------|
| user4@tc.com   | "004"   |
| user26@tc.com   | "026"   |
| user314@tc.com   | "314"   |

1. Go to ‘Explore’.
1. Use the search bar on top right, to find your specific project.
1. Click your assigned folder in search result, and click ★ star icon next to your folder name to 'favorite' your contents. This way, your assigned folder will pop up on your home screen and you will not miss it! 

> [+Hint] See it in action
>
>!VIDEO[find your folder.mp4](instructions258429/find your folder.mp4)

===

#✍Chapter 1: Build & Publish

##💡Key Points
- In this chapter, you will create a workbook with using the existing published data source.
- You will experience how to create Tableau’s dashboard
- By publishing your workbook to Tableau Cloud, your content will be available to anyone who has the right permissions. 

🚨 **All the excersise must be done inside of your assinged folder**🚨

##📚Resource Links
- [Getting Started with web authoring](https://help.tableau.com/current/pro/desktop/en-us/getstarted_web_authoring.htm)
- [Best Practices for Published Data Sources](https://help.tableau.com/current/pro/desktop/en-us/publish_datasources_about.htm)


##📝Excercise 1.1 - Create Workbook

1. 🚨**Go to your assigned folder**🚨
1.  Within your assigned folder, click the ‘New’ dropdown and select ‘Workbook’.
1. In [Connect to Data] window, make sure you are in [On This Site] tab. (It's default) Under Data Sources, click "See All" on right side and find the certified data source ‘World Languages’.
1. Select "World Languages" datasource and click ‘Connect’.

> [+Hint] See it in action
>
>!VIDEO[Connect datasource.mp4](instructions258429/Connect datasource.mp4)


##📝Excercise 1.2 - Create Worksheets
####**Step1** 
Create "Language by Location" worksheet, which has a map with [Total Speakers] by [Country].

> [+Hint] Step by step
>
>1. Drag 'Country' to the canvas where Tableau asks ‘Drop field here’.
1. Drop 'Total Speakers (millions)' onto 'Size' on the Marks card.
1. Right-click on 'Sheet1' and choose 'Rename'.
1. Rename it to `Language by Location`.
!VIDEO[first worksheet.mp4](instructions258429/first worksheet.mp4)


    
####**Step2** 
Create "Native vs. Second Language" worksheet, which has a scatter plot with [Native Speakers] and [Second Language Speakers] by [Language]

> [+Hint] Step by step
>
>1. Select the ‘New Worksheet’ icon at the bottom, next to the ‘Language by Location’ sheet to create new worksheet.
1. Multi-select 'Language', 'Native Speakers', and 'Second Language Speakers (millions)'
    1. Mac: Hold 'Command' and select each fields.
    1. Windows: Hold ‘Ctrl’ and select each fields.
1. Click 'Show Me' in the top right corner and choose the highlighted viz, 'scatter-plot'.
1. Change Mark from 'Automatic' to 'Circle'.
1. Click 'Color' on the Marks Card, choose 'Border' dropdown, and select black.
1. Drag the field ‘Language’ in the Marks Card to ‘Label’.
1. Right-click on 'Sheet 2' and rename it to `Native vs. Second Language`.
!VIDEO[second worksheet.mp4](instructions258429/second worksheet.mp4)


####**Step3** 
Create "Total Speakers by Language" worksheet, which has a barchart with [Native Speakers] by [Languages], and [Second Language Speakers] in Color.

> [+Hint] Step by step
>1. Click the 'New Worksheet' icon.
1. Drag 'Total Speakers (millions)' to Columns.
1. Drag 'Language' to Rows.
1. Sort descending.
1. Drag ‘Native Speakers (millions) to ‘Color’ on the Marks card.
1. Rename worksheet to `Total Speakers by Language`.
!VIDEO[third worksheet.mp4](instructions258429/third worksheet.mp4)


##📝Excercise 1.3 - Create and Publish Dashboard
####**Step1** 
Bring three worksheets into a single dashboard and use map and barchart as filters. Name it to "World Languages Analytics".

> [+Hint] Step by step
>1. Click the 'New Dashboard' icon.
1. Drag 
    1. 'Language by Location' worksheet to the dashboard.
    1. 'Native vs. Second Language' under 'Language by Location' worksheet.
    1. 'Total Speakers by Language' worksheet to the right side of the dashboard.
1. Remove 'Total Speakers (millions)' Legend from the top right corner. 
1. Set filters
    1. Click ‘Language by Location’ worksheet on dashbaord, and 4 small icons will appear on top right. Select 'Use as filter'.
    1. Repeat the same on ‘Total Speaker by Language’ wosksheet to set a filter.
1. Check the box in the bottom left “Show Dashboard Title”.
1. Right-click the title ‘Dashboard 1” and rename it to `World Languages Analytics`. Click ‘OK’.
!VIDEO[dashboard.mp4](instructions258429/dashboard.mp4)

####**Step2** 
Publish workbook to your folder. Name your workbook "World Languages_your number"

> [+Hint] Step by step
>1. Select 'Publish As' on upper right.
1. Name the workbook `World Languages` with your project number following: for example “World Languages 042’.
1. Make sure your folder is pre-selected. If not, find your folder.
1. Select ‘Publish’.
1. Lastly, select ‘Go to Workbook’ on the notification at the top of the page.
!VIDEO[publish.mp4](instructions258429/publish.mp4)


##🎁Done already? Here’s your bonus!
- Feel free to create more worksheets!
- Explore interesting findings from the dataset




===
#✍Chapter 2: Interact

##💡Key Points
- In this chapter, you will see what options are available to the end user when working off of a published workbook
- Filter, Comment, Download
- Set subscriptions, data-driven alerts, custom views



##📚Resource Links
- [Share and Collaborate on the Web](https://help.tableau.com/current/pro/desktop/en-us/share_collaborate.htm)

##📝Excercise 2 Interact with Dashboard
####**Step1** Filter & Comment
Click "India" on map and observe findings. Add comment to @Duncan Wingfield with a snapshot and your findings!

> [+Hint] Step by step
>1. Click [World Languages Analytics] dashboard you just created.
1. Select "India" on the map to filter your dashboard.
1. Notice in India, there are multiple languages are spoken. Not just Hindi. This is interesting, let's share this insight.
1. Click "Add or View Comments" on upper right menu
1. In the comment, "@Duncan Wingfield" and add whatever comment you like to add. Click little icon below to attach a snapshot of your dashboard. Click "Post".
1. Click "Reset View" to rest your dashbaord.
!VIDEO[comment.mp4](instructions258429/comment.mp4)


####**Step2** Download
Click "Download" to see the available options for end users.

> [+Hint] Step by step
>1. On the top right, select the 'download' dropdown to explore options available to the end user. You can manage permission in the real business scinario.




####**Step3** Subscriptions
Set up your subscription to receive a snapshot of this dashboard at your desired cadence.

> [+Hint] Step by step
>1. Click the 'Watch' dropdown and select 'Subscriptions'.
1. Check the box 'Subscribe me'.
1. Click the schedule drop down, choose whatever cadence you'd like. (Don't think too much, this is a drill.) and click 'Subscribe'.
!VIDEO[subscribe.mp4](instructions258429/subscribe.mp4)

####**Step4** Data-Driven Alerts    
Set up your Data-Driven Alerts, so you can receive a proactive notification from Tableau Cloud when the underlying data had changed that requires your attention.

> [+Hint] Step by step
>1. Click the 'Watch' dropdown and select 'Alerts'.
1. Select the Y-Axis of your bar chart (Total Speakers (millions)).
1. Click [Create] under Alert
1. Set the threshold to '2000'.
1. Click the 'When the condition is true send alert' dropdown and select 'Weekly at most'.
1. Create Alert.
!VIDEO[alert.mp4](instructions258429/alert.mp4)


####**Step5** Custom Views
Save your filter combination as Custom View, so next time you look at this dashbaord it is filtered to the information that you want to see.
> [+Hint] Step by step
>1. Select the country where you are from on the map.(We hope it's there🙏! If not, choose your favorite country)
1. Click 'Save Custom View'.
1. Name this view `My default view`.
1. Select 'Make it my default' and Save.
!VIDEO[Custom view.mp4](instructions258429/Custom view.mp4)



##🎁Done already? Here’s your bonus!

- Click Data Guide
- Click Data Detail

===

#✍Chapter 3: Administrate

##💡Key Points
- In this chapter, you will learn the basics of permissions and how to manage users/groups
- The default folder inherits the initial permissions. 
- Use “Lock permissions” efficiently.

##📚Resource Links
- [Permissions Quick start guide](https://help.tableau.com/current/online/en-us/qs_permissions.htm)

##📝Excercise 3- Assingn Permission to Group

Right now, your contents are not available for any users. Let’s add a “Sales team” group permission to your project, so they can see your content!

####**Step1**
Go back to your assigned folder

> [+Hint] Step by Step
>1. Click "Explore" on top-left corner then Click "Home" from left navigation bar.
1. Select your favorited folder from the home screen.
1. **OR** Simply click the folder name on top left navigation bar!
!VIDEO[favorite.mp4](instructions258429/favorite.mp4)

####**Step2**
Allow "View Project" Permission for Sales Team
> [+Hint] Step by Step
>1. Click the three dots to the right of the folder name.
1. Choose "permissions" to manage folder permissions.
1. Make sure you are under [Projects] tab (it's default)
1. Click "Add Group/User Rule" to add a new permission rule.
1. Choose “Sales Team” and change Template from None to“View”. Then click "Save"
!VIDEO[sales group permission.mp4](instructions258429/sales group permission.mp4)


####**Step3**
Lock the project permission at the parent folder level for governance best practice.
> [+Hint] Step by Step
>1. Click “Edit” next to Asset permissions:Customizable (locates upper left in pop-up)
1. change it to “Locked” from "Customizable" and Save.
!VIDEO[lock permission.mp4](instructions258429/lock permission.mp4)

##🎁Done already? Here’s your bonus!

- Click around [Workbooks], [Datasources] etc tabs in permission setting to see what are the available options.
- Free exploration in Users/Group section !!! Do not change anything!! 


===

#✍Chapter 4: Pulse

##💡Key Points
- lalala

##📚Resource Links
- [Tableau Pulse whitepaper](https://help.tableau.com/current/online/en-us/pulse_intro.htm)
- [Set up Your Site for Tableau Pulse Guide](https://help.tableau.com/current/online/en-us/pulse_set_up.htm)


##📝Excercise 4- Pulse

Let's explore Tableau Pulse and understand the power of AI + Tabelau!

####**Step1**
Access your pre-assigned Pulse metrics
> [+Hint] Step by Step
>1. Click on "Tableau Pulse" to begin.
1. Read through the provided business summary for context.

####**Step2**
Ask questions and gain insights with one of the Pulse metrics
> [+Hint] Step by Step
>1. Click on the metric "Sales" (Month to Date) for deeper insights.
1. Select ‘Breakdown’ next to ‘Overview’
1. Select ‘Product Name’ 
1. Scroll down and select the question, "Which Category had very high sales?" to pinpoint top-performing categories.
1. Click on the "Ask" button and type in "Which Product Name decreased the most?" to delve into product-specific insights.
1. Choose the suggested question related to decreasing product sales.


####**Step3**
Subscribe new Pulse metrics to get update!

> [+Hint] Step by Step
>1. Hit the "back" button to return to the previous view.
1. Select "Browse Metrics" to explore additional metrics.
1. Choose Average Order Value (AOV) ‘Quarter to Date’ and click Click on "+ Follow" to track this metric for future reference.
1. Go back to Pulse home page, you will see the updates.




##🎁Done already? Here’s your bonus!

- lala

===

#🚀Wrap Up
!IMAGE[1f704733052c9e545158aeec8d586654.gif](instructions258429/1f704733052c9e545158aeec8d586654.gif)

##Congratulations on completing the Getting Started with Tableau Cloud Lab! 

Throughout this session, you've embarked on a journey to harness the power of Tableau Cloud, from accessing your credentials to building and publishing workbooks, interacting with published content, administering permissions, and exploring Tableau Pulse AI capabilities.

As you wrap up, remember that Tableau Cloud offers a dynamic platform for data exploration, visualization, collaboration, and administration. Whether you're a data analyst, business user, or administrator, Tableau Cloud equips you with the tools to transform data into actionable insights.

Continue to explore the rich resources available to you, including the links provided in this manual, to deepen your understanding and proficiency with Tableau Cloud. Keep innovating, experimenting, and discovering new ways to leverage data to drive informed decision-making and propel your organization forward.

Thank you for your participation, and we look forward to seeing your continued success with Tableau Cloud!
