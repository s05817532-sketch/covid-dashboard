import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.graph_objects as go
import base64

left,right=st.columns([3,2])

with left:

    st.markdown("""
    <h1 style='color:#FFC107;font-size:45px'>
    COVID-19 & Vaccination Analysis
    </h1>
    """,unsafe_allow_html=True)

with right:
   
   st.image("corona.jpg")

st.set_page_config(page_title="COVID-19 ",page_icon="🦠",layout="wide")

covid = pd.read_csv("Latest Covid-19 India Status.csv")
vaccine = pd.read_csv("COVID-19 India Statewise Vaccine Data.csv")
df=pd.read_csv("Merged_COVID_Vaccine_Data.csv")

with st.sidebar:

 st.sidebar.info("COVID-19 Dashboard\nDeveloped using Streamlit")
 selected = option_menu(menu_title="Navigation",

    options=["Home",
             "Data Cleaning",
             "Covid Analysis",
             "Vaccination Analysis",
             "Interactive Charts",
             "Insights",
             "About"],
    
    icons=[
            "house",
            "database",
            "virus",
            "shield-plus",
            "bar-chart",
            "lightbulb",
            "info-circle"
        ],

    menu_icon="menu-button",
    default_index=0
)

def set_video_background(video_path):
    with open(video_path, "rb") as f:
        video_bytes = f.read()

    video_base64 = base64.b64encode(video_bytes).decode()

    st.markdown(
        f"""
        <style>

        #bg-video {{
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%;
            min-height: 100%;
            object-fit: cover;
            z-index: -999;
        }}

        .stApp {{
            background: transparent;
        }}

        [data-testid="stHeader"] {{
            background: rgba(0,0,0,0);
        }}

        [data-testid="stSidebar"] {{
            background: rgba(20,20,20,0.7);
            backdrop-filter: blur(8px);
        }}

        </style>

        <video autoplay muted loop playsinline id="bg-video">
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True,
    )  
if selected == "Home":
    
    st.divider()

    st.write(
    """
    Welcome to the COVID-19 Dashboard.

    This dashboard analyzes COVID-19 cases and vaccination
    progress across India using real-world datasets.
    """
    )

    st.image("covid_banner.jpg", use_container_width=True)
    
    st.divider()

    st.subheader("📊 Dashboard Overview")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "States/UTs",
            df["State/UTs"].nunique())

    with c2:
        st.metric(
            "Total Cases",
            f"{df['Total Cases'].sum():,}")

    with c3:
        st.metric(
            "Total Vaccinations",
            f"{df['Total Vaccination Doses'].sum():,}")

    st.divider()

    st.subheader("🔦 Objectives")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("📈 Analyze COVID-19 spread")
        st.success("🦠 Study cases and deaths")
        st.success("🗺️ Perform state-wise analysis")

    with c2:
        st.success("💉 Analyze vaccination progress")
        st.success("🏆 Identify top affected states")
        st.success("📊 Create visualizations")

    with c3:
        st.success("🔍 Generate insights")
        st.success("🐍 Apply Python and Pandas")
        st.success("🌐 Build an interactive dashboard")

    st.divider()

    st.subheader("🛠️ Technologies Used")

    st.write(
        "🐍 Python | 🐼 Pandas | 📊 Matplotlib | 🎨 Seaborn | "
        "📈 Plotly | 🌐 Streamlit"
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.info("Dataset 1\n\nCOVID-19 India State-wise Data")
        st.markdown("[View Dataset](https://www.kaggle.com/datasets/anandhuh/latest-covid19-india-statewise-data)")

    with col2:
        st.info("Dataset 2\n\nIndia Vaccination Data")
        st.markdown("[View Dataset](https://www.kaggle.com/datasets/anandhuh/covid19-india-statewise-vaccine-data)")

elif selected == "Data Cleaning":
    set_video_background("covid.mp4")
    st.title("🧹 Data Cleaning")

    st.markdown("""
    Before performing data analysis, the COVID-19 and Vaccination datasets
    were cleaned and merged into a single dataset.
    """)

    st.divider()

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📋 Process",
        "📄 Preview",
        "📊 Dataset Info",
        "❓ Missing Values",
        "📈 Statistics"
    ])

    

    with tab1:

        st.subheader("📋 Data Cleaning Steps")

        st.markdown("""
           - Loaded COVID-19 Dataset
           - Loaded Vaccination Dataset
           - Merged both datasets using **State/UTs**
           - Checked Missing (Null) Values
           - Verified Data Types
           - Prepared the Final Clean Dataset
        """)

        st.subheader("🔗 Dataset Merging")

        st.code("""
merged_data = pd.merge(covid, vaccine, on="State/UTs")
        """, language="python")

    

    with tab2:

        st.subheader("📄 Cleaned Dataset Preview")

        st.dataframe(df.head())


    with tab3:

        st.subheader("📊 Dataset Shape")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Rows", df.shape[0])

        with col2:
            st.metric("Columns", df.shape[1])

        st.divider()

        st.subheader("📑 Data Types")

        datatype = df.dtypes.reset_index()
        datatype.columns = ["Column", "Data Type"]

        st.dataframe(datatype)



    with tab4:

        st.subheader("❓ Missing Values")

        st.dataframe(
            df.isnull().sum().reset_index().rename(
                columns={
                    "index": "Column",
                    0: "Missing Values"
                }
            )
        )

    

    with tab5:

        st.subheader("📈 Statistical Summary")

        st.dataframe(df.describe())

        st.success(
            "✅ Data preprocessing was successfully completed and the cleaned dataset is ready for further analysis."
        )

    st.divider()

    st.subheader("⬇️ Download Cleaned Dataset")

    csv=df.to_csv(index=False)

    st.download_button(label="📥Download Cleaned Dataset",data=csv,

    file_name="Merged_COVID_Vaccine_Data.csv",mime="text/csv")

elif selected == "Covid Analysis":
    set_video_background("covid.mp4")
    st.title("🦠 Covid-19 Analysis")
    
    st.divider()

    total_cases=df["Total Cases"].sum()
    active_cases=df["Active"].sum()
    recovered_cases=df["Discharged"].sum()
    total_deaths=df["Deaths"].sum()
    
    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.metric("Total Cases",f"{total_cases:,}")

    with c2:
        st.metric("Active Cases",f"{active_cases:,}")

    with c3:
        st.metric("Recovered Cases",f"{recovered_cases:,}")

    with c4:
        st.metric("Deaths",f"{total_deaths:,}")

    st.divider()

    st.subheader("COVID Dataset Preview")
    st.dataframe(df[[
        "State/UTs",
        "Total Cases",
        "Active",
        "Discharged",
        "Deaths"
     ]]
    )

    st.divider()
    
    st.subheader("Top 10 States by Total Cases")

    top = df.sort_values('Total Cases', ascending=False).head(10)

    fig = px.bar(
      top,
      x='Total Cases',
      y='State/UTs',
      orientation='h',
      color='Total Cases',
      color_continuous_scale='Viridis', 
      title='Top 10 States by Total Cases'
    )
    fig.update_layout(
    template='plotly_dark',
    xaxis_title='Total Cases',
    yaxis_title='States',
    xaxis_showgrid=True,
    yaxis_showgrid=False,
    hovermode='y unified',
   )
    fig.update_yaxes(autorange='reversed')
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("📊 Top 10 States by Active Cases")

    st.subheader("Top 10 States by Active")

    top=df.nlargest(10,"Active")

    fig = px.bar(
    top,
    x='State/UTs',
    y='Active',
    color='Active',
    color_continuous_scale='Viridis',
    title='Active Cases by State'
    )

    fig.update_xaxes(tickangle=-90)

    st.plotly_chart(fig, use_container_width=True)

    st.divider()
 
    st.subheader("Top 10 States by Deaths")

    top = df.nlargest(10, 'Deaths')

    fig = px.bar(
      top,
      x='State/UTs',
      y='Deaths',
      color='Deaths',
      color_continuous_scale='Reds',
      title='Top 10 States by Deaths'
    )

    fig.update_xaxes(tickangle=-45)
    fig.update_layout(template='plotly_white')

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("🏥 Top 10 States by Discharged Cases")

    top_recovered = df.nlargest(10, "Discharged")

    fig = px.scatter(
     top_recovered,
     x="Discharged",
     y="State/UTs",
     size="Discharged",
     color="Discharged",
     color_continuous_scale="Greens",
     title="Top 10 States by Discharged Cases"
    )

    for i in range(len(top_recovered)):
     fig.add_shape(
        type="line",
        x0=0,
        y0=i,
        x1=top_recovered["Discharged"].iloc[i],
        y1=i,
        line=dict(color="gray", width=2)
     )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("☀️ State-wise Total Cases")

    fig = px.sunburst(
    df,
    path=["State/UTs"],
    values="Total Cases",
    color="Total Cases",
    color_continuous_scale="Plasma",
    title="State-wise Total COVID-19 Cases"
   )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

elif selected == "Vaccination Analysis":
   set_video_background("covid.mp4")
   st.title("💉 Vaccination Analysis")

   st.divider()

   st.image("coronavirus-vaccine-bottles.webp", use_container_width=True)

   total_vaccination = df["Total Vaccination Doses"].sum()
   dose1_15_18=df["Dose 1 15-18"].sum()
   dose2_15_18=df["Dose 2 15-18"].sum()
   dose1_12_14=df["Dose 1 12-14"].sum()
   dose2_12_14=df["Dose 2 12-14"].sum()

   c1,c2,c3,c4,c5 = st.columns(5)

   with c1:
      st.metric("Total Vaccination Doses",f"{total_vaccination:,}")

   with c2:
      st.metric("Dose 1 15-18",f"{dose1_15_18:,}")

   with c3:
      st.metric("Dose 2 15-18",f"{dose2_15_18:,}")

   with c4:
      st.metric("Dose 1 12-14",f"{dose1_12_14:,}")

   with c5:
      st.metric("Dose 2 12-14",f"{dose1_12_14:,}")

   st.divider()

   st.subheader("COVID Dataset Preview")
   st.dataframe(df[[
        "State/UTs",
        "Total Vaccination Doses",
        "Dose 1 15-18",
        "Dose 2 15-18",
        "Dose 1 12-14",
        "Dose 2 12-14"
     ]]
    )
   
   st.divider()

   st.subheader("Top 10 Vaccinated States")

   top = df.nlargest(10, 'Total Vaccination Doses')

   fig = px.bar(
    top,
    x='Total Vaccination Doses',
    y='State/UTs',
    orientation='h',
    color='State/UTs',
    title='Top 10 Vaccinated States'
   )

   fig.update_yaxes(autorange='reversed')

   st.plotly_chart(fig, use_container_width=True)

   st.divider()

   st.subheader("Dose 1 (15-18) Distribution")
   
   print(df.columns.tolist())
   top = df.nlargest(10,"Dose 1 15-18")

   st.divider()
   fig = px.histogram(
    top,
    x="Dose 1 15-18",
    nbins=15,
    color_discrete_sequence=['blue'],
    title="Dose 1 (15-18)")
   
   fig.update_layout(title_x=0.5,bargap=0.3)

   st.plotly_chart(fig, use_container_width=True)  

   st.divider()

   st.subheader("📈 Top 10 States by Dose 2 (15-18)")

   top_dose2_15 = df.nlargest(10, "Dose 2 15-18")

   fig = px.area(
    top_dose2_15,
    x="State/UTs",
    y="Dose 2 15-18",
    title="Top 10 States by Dose 2 (15-18)"
   )

   fig.update_xaxes(tickangle=-45)

   st.plotly_chart(fig, use_container_width=True)
  
   st.divider()

   st.subheader("💉 Top 10 States by Precaution Dose (18-59)")

   top_precaution = df.nlargest(10, "Precaution 18-59")

   fig = px.bar(
    top_precaution,
    x="State/UTs",
    y="Precaution 18-59",
    color="State/UTs",
    color_discrete_sequence=px.colors.qualitative.Bold,
    text_auto=True,
    title="Top 10 States by Precaution Dose (18-59)"
   )

   fig.update_layout(
    title_x=0.5,
    xaxis_tickangle=-45,
    showlegend=False,
    plot_bgcolor="white"
   )

   fig.update_traces(
    marker_line_color="black",
    marker_line_width=1.5
   )

   st.plotly_chart(fig, use_container_width=True)

   st.divider()

   st.subheader("😷 State-wise Vaccination Statistics")

   selected_state = st.selectbox("Select State/UT",df["State/UTs"])

   state_data=df[df["State/UTs"] == selected_state]

   c1,c2,c3 =st.columns(3)

   with c1:st.metric("Total Vaccination",f"{int(state_data['Total Vaccination Doses'].iloc[0]):,}")

   with c2:st.metric("Dose 1",f"{int(state_data['Dose1'].iloc[0]):,}")

   with c3:st.metric("Dose 2",f"{int(state_data['Dose 2'].iloc[0]):,}")

elif selected == "Interactive Charts":
   set_video_background("covid.mp4")
   st.divider()
   st.title("📊 Interactive Charts")

   st.divider()

   chart_column = st.selectbox("Select a Column",
        [
            "Total Cases",
            "Active",
            "Discharged",
            "Deaths",
            "Total Vaccination Doses",
            "Dose1",
            "Dose 2"
        ]
    )
   
   st.subheader(f"Bar Chart of {chart_column}")

   fig = px.bar(
    df,
    x="State/UTs",
    y=chart_column,
    color=chart_column,
    color_discrete_sequence=px.colors.qualitative.Bold,
    title=f"{chart_column} Across States")

   fig.update_xaxes(tickangle=-90)

   st.plotly_chart(fig, use_container_width=True)

   st.divider()

   st.subheader("Total Cases vs Deaths")

   fig = px.scatter(
    df,
    x='Total Cases',
    y='Deaths',
    color='Deaths',
    hover_name='State/UTs',
    color_continuous_scale='Magma',
    size='Deaths',
    title='Total Cases vs Deaths'
   )
   
   fig.update_layout(title_x=0.5)
   fig.update_xaxes(tickangle=-45)

   st.plotly_chart(fig, use_container_width=True)

   st.divider()

   st.subheader("Total Cases vs Discharged")

   fig = px.scatter(
    df,
    x='Total Cases',
    y='Discharged',
    color='Discharged',
    hover_name='State/UTs',
    color_continuous_scale='Plasma',
    size='Discharged',
    title='Total Cases vs Discharged'
  )
   st.plotly_chart(fig, use_container_width=True)

   
   st.divider()

   st.subheader("🌲 Top 10 States by Discharged Cases")

   top = df.nlargest(10, "Discharged")

   fig = px.treemap(
    top,
    path=["State/UTs"],
    values="Discharged",
    color="Discharged",
    color_continuous_scale="Turbo",
    title="Top 10 States by Discharged Cases"
    )
   st.plotly_chart(fig, use_container_width=True)

   st.divider()

   st.subheader("Discharged Distribution")

   fig = px.histogram(
    df,
    x='Discharged',
    nbins=15,
    color_discrete_sequence=['green'],
    title='Discharged Distribution'
   )

   fig.update_layout(bargap=0.3)

   st.plotly_chart(fig, use_container_width=True)

   st.divider()

   st.subheader("📊 Top 10 States by Active Ratio")

   top = df.nlargest(10, "Active Ratio")

   fig = px.bar(
    top,
    x="State/UTs",
    y="Active Ratio",
    color="Active Ratio",
    color_continuous_scale="Turbo",
    title="Top 10 States by Active Ratio"
   )

   fig.update_layout(
    title_x=0.5,
    xaxis_title="State/UTs",
    yaxis_title="Active Ratio (%)"
  )

   fig.update_xaxes(tickangle=-45)

   st.plotly_chart(fig, use_container_width=True)

   st.divider()

   st.subheader("Population vs Vaccination")

   fig = px.scatter(
    df,
    x='Population_y',
    y='Total Vaccination Doses',
    color='Total Vaccination Doses',
    color_continuous_scale='Blues',
    hover_name='State/UTs',
    title='Population vs Vaccination'
  )

   st.plotly_chart(fig, use_container_width=True)

   st.divider()

   st.subheader("Dose 1 vs Dose 2")

   fig = px.scatter(
    df,
    x='Dose1',
    y='Dose 2',
    color='Dose1',
    size='Dose1',
    color_continuous_scale='Plasma',
    hover_name='State/UTs',
    title='Dose 1 vs Dose 2'
  )

   st.plotly_chart(fig, use_container_width=True)

   st.divider()

   st.subheader("Correlation Heatmap")

   corr = df.select_dtypes(include='number').corr()

   fig = px.imshow(
    corr,
    text_auto='.2f',
    color_continuous_scale='RdBu',
    title='Correlation Heatmap'
  )

   st.plotly_chart(fig, use_container_width=True)

   st.divider()

   st.subheader("Top 5 States by Total Cases")

   top = df.sort_values('Total Cases', ascending=False).head(5)

   fig = px.pie(
    top,
    names='State/UTs',
    values='Total Cases',
    hole=0.3,
    title='Top 5 States by Total Cases'
  )

   st.plotly_chart(fig, use_container_width=True)

   st.divider()

   st.subheader("Dose 1 vs Dose 2 Comparision")

   dose1_total = df['Dose1'].sum()
   dose2_total = df['Dose 2'].sum()

   fig = px.pie(
    names=['Dose 1', 'Dose 2'],
    values=[dose1_total, dose2_total],
    hole=0.3,
    title='Comparison of Total Dose 1 and Dose 2 Vaccinations'
   )

   st.plotly_chart(fig, use_container_width=True)

   st.divider()

   st.subheader("Vaccination Distribution")

   labels = ['Dose1 15-18', 'Dose2 15-18',
          'Dose1 12-14', 'Dose2 12-14']

   values = [
    df['Dose 1 15-18'].sum(),
    df['Dose 2 15-18'].sum(),
    df['Dose 1 12-14'].sum(),
    df['Dose 2 12-14'].sum()]

   fig = px.pie(
    names=labels,
    values=values,
    title='Vaccination Distribution')

   st.plotly_chart(fig, use_container_width=True)

   st.divider()

   st.subheader("Total Vaccinations")

   fig = px.bar(
    x=labels,
    y=values,
    color=values,
    color_continuous_scale='Viridis',
    title='Total Vaccinations')

   st.plotly_chart(fig, use_container_width=True)

   st.subheader("Precaution Dose (18-59 Years)")

   fig = px.line(
    df,
    x='State/UTs',
    y='Precaution 18-59',
    markers=True,
    title='Precaution Dose (18-59 Years) Across States')

   fig.update_xaxes(tickangle=-90)

   st.plotly_chart(fig, use_container_width=True)

elif selected == "Insights":
    set_video_background("covid.mp4")
    st.divider()

    st.title("💡 Insights ")

    st.divider()

    highest_cases = df.loc[df["Total Cases"].idxmax(), "State/UTs"]
    highest_deaths = df.loc[df["Deaths"].idxmax(), "State/UTs"]
    highest_vaccination = df.loc[
        df["Total Vaccination Doses"].idxmax(),
        "State/UTs"
    ]
    highest_active = df.loc[df["Active"].idxmax(), "State/UTs"]

    st.success(
        f"📌 {highest_cases} has the highest number of COVID-19 cases."
    )

    st.success(
        f"📌 {highest_deaths} has the highest number of deaths."
    )

    st.success(
        f"📌 {highest_vaccination} has administered the highest number of vaccination doses."
    )

    st.success(
        f"📌 {highest_active} has the highest number of active cases."
    )

    st.info(
        "📌 Most states have significantly higher recovered cases than active cases."
    )

    st.info(
        "📌 Vaccination coverage varies across different states and union territories."
    )

    st.info(
        "📌 Data visualization helps identify patterns and compare state-wise performance."
    )   
    
elif selected == "About":
    set_video_background("covid.mp4")

    st.image("coronavirus-scaled.jpg", width=800)

    st.caption("An Interactive Data Analytics Dashboard for Monitoring COVID-19 Cases and Vaccination Progress Across India")

    st.divider()

    st.subheader("📖 Project Overview")

    st.write("""
    This dashboard provides a comprehensive analysis of COVID-19 cases,
    recoveries, deaths, and vaccination statistics across Indian states
    and union territories. It enables users to explore trends through
    interactive visualizations and state-wise comparisons.
    """)

    st.divider()

    st.subheader("📌 Dashboard Highlights")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Country", "India")

    with col2:
        st.metric("Datasets", "2")

    with col3:
        st.metric("Visualizations", "20+")

    with col4:
        st.metric("Platform", "Streamlit")

    st.divider()

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "🎯 Objective",
            "📊 Features",
            "🛠 Technology Stack",
            "👨‍💻 Developers",
        ]
    )

    
    with tab1:

        st.subheader("Project Objective")

        st.write("""
        The primary objective of this project is to perform exploratory
        data analysis on COVID-19 datasets and present meaningful
        insights through an interactive dashboard.

        The dashboard assists users in:

        • Understanding COVID-19 trends

        • Comparing state-wise statistics

        • Monitoring vaccination progress

        • Exploring interactive charts

        • Supporting data-driven decision making
        """)

    
    with tab2:

        st.subheader("Key Features")

        c1, c2 = st.columns(2)

        with c1:

            st.success("""
            ✔ Data Cleaning

            ✔ Missing Value Handling

            ✔ State-wise Analysis

            ✔ Vaccination Analysis

            ✔ Interactive Filters
            """)

        with c2:

            st.success("""
            ✔ Plotly Visualizations

            ✔ Comparative Charts

            ✔ Statistical Insights

            ✔ Responsive Dashboard

            ✔ User-Friendly Interface
            """)


    with tab3:

        st.subheader("Technology Stack")

        tech1, tech2 = st.columns(2)

        with tech1:

            st.markdown("""
            #### Programming

            • Python

            • Pandas

            • NumPy
            """)

        with tech2:

            st.markdown("""
            #### Visualization

            • Plotly

            • Matplotlib

            • Seaborn

            • Streamlit
            """)

        st.info("Dataset Source: Kaggle (COVID-19 India State-wise Dataset & Vaccination Dataset)")


        with tab4:

         st.subheader("Project Developers")

         d1, d2 = st.columns(2)

        with d1:

            st.markdown("""
            ### 👩 Sukhmanpreet Kaur

            **Course:** B.Tech Computer Science Engineering

            **Institution:** Anand College of Engineering & Management (A.C.E.M.)
            """)

        with d2:

            st.markdown("""
            ### 👩 Mehakpreet Kaur

            **Course:** B.Tech Computer Science Engineering

            **Institution:** Anand College of Engineering & Management (A.C.E.M.)
            """)

    st.divider()

    st.caption("Developed as a B.Tech Computer Science Engineering Academic Project using Python, Streamlit, Plotly, and Pandas.")
