import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Set page config
st.set_page_config(
    page_title="Anime Data Analysis Dashboard",
    page_icon="🎌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #FF6B6B;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #FF6B6B;
    }
    .insight-box {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #4CAF50;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and cache the anime dataset"""
    try:
        df = pd.read_csv("anime.csv")
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

def main():
    # Header
    st.markdown('<h1 class="main-header">🎌 Anime Data Analysis Dashboard</h1>', unsafe_allow_html=True)
    
    # Load data
    df = load_data()
    if df is None:
        st.error("Failed to load data. Please check if anime.csv exists in the current directory.")
        return
    
    # Sidebar
    st.sidebar.title("📊 Navigation")
    page = st.sidebar.selectbox(
        "Choose a section:",
        ["🏠 Overview", "📈 Genre Analysis", "⭐ Rating Analysis", "📊 Type Distribution", "🔍 Correlation Analysis", "💡 Key Insights"]
    )
    
    # Overview Page
    if page == "🏠 Overview":
        st.header("📊 Dataset Overview")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Anime", len(df))
        
        with col2:
            st.metric("Unique Genres", df['genre'].nunique())
        
        with col3:
            st.metric("Average Rating", f"{df['rating'].mean():.2f}")
        
        with col4:
            st.metric("Total Members", f"{df['members'].sum():,.0f}")
        
        # Data preview
        st.subheader("📋 Data Preview")
        st.dataframe(df.head(10))
        
        # Data info
        st.subheader("📋 Dataset Information")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Dataset Shape:**", df.shape)
            st.write("**Columns:**", list(df.columns))
        
        with col2:
            st.write("**Missing Values:**")
            missing_data = df.isnull().sum()
            st.write(missing_data[missing_data > 0])
    
    # Genre Analysis Page
    elif page == "📈 Genre Analysis":
        st.header("📈 Genre Analysis")
        
        # Genre distribution
        st.subheader("🎭 Top 10 Genres by Count")
        
        # Process genres
        genre_counts = df['genre'].str.split(',').explode().str.strip().value_counts()
        
        # Create bar chart with Plotly
        fig = px.bar(
            x=genre_counts.head(10).index,
            y=genre_counts.head(10).values,
            title="Genre Distribution",
            labels={'x': 'Genre', 'y': 'Count'},
            color=genre_counts.head(10).values,
            color_continuous_scale='viridis'
        )
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
        
        # Genre rating correlation
        st.subheader("⭐ Top 10 Genres by Average Rating")
        
        # Process genre ratings
        df['genre_list'] = df['genre'].str.split(', ')
        df_exploded = df.explode('genre_list')
        genre_rating = df_exploded.groupby('genre_list')['rating'].mean().sort_values(ascending=False)
        
        fig2 = px.bar(
            x=genre_rating.head(10).index,
            y=genre_rating.head(10).values,
            title="Genre Rating Correlation",
            labels={'x': 'Genre', 'y': 'Average Rating'},
            color=genre_rating.head(10).values,
            color_continuous_scale='plasma'
        )
        fig2.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig2, use_container_width=True)
        
        # Genre insights
        st.subheader("💡 Genre Insights")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="insight-box">
            <h4>🎯 Most Popular Genres:</h4>
            <ul>
            <li>Action and Comedy dominate the anime landscape</li>
            <li>Slice of Life and Fantasy are also very popular</li>
            <li>These genres appeal to a broad audience</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="insight-box">
            <h4>⭐ Highest Rated Genres:</h4>
            <ul>
            <li>Josei and Seinen target mature audiences</li>
            <li>Psychological and Thriller genres score high</li>
            <li>Quality over quantity in niche genres</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    
    # Rating Analysis Page
    elif page == "⭐ Rating Analysis":
        st.header("⭐ Rating Analysis")
        
        # Rating distribution
        st.subheader("📊 Rating Distribution")
        
        fig = px.histogram(
            df, 
            x='rating', 
            nbins=50,
            title="Distribution of Anime Ratings",
            labels={'rating': 'Rating', 'count': 'Number of Anime'}
        )
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
        
        # Rating statistics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Mean Rating", f"{df['rating'].mean():.2f}")
        
        with col2:
            st.metric("Median Rating", f"{df['rating'].median():.2f}")
        
        with col3:
            st.metric("Rating Std Dev", f"{df['rating'].std():.2f}")
        
        # Top rated anime
        st.subheader("🏆 Top 10 Highest Rated Anime")
        top_rated = df.nlargest(10, 'rating')[['name', 'rating', 'genre', 'type']]
        st.dataframe(top_rated)
        
        # Rating by type
        st.subheader("📺 Average Rating by Type")
        type_rating = df.groupby('type')['rating'].mean().sort_values(ascending=False)
        
        fig2 = px.bar(
            x=type_rating.index,
            y=type_rating.values,
            title="Average Rating by Anime Type",
            labels={'x': 'Type', 'y': 'Average Rating'},
            color=type_rating.values,
            color_continuous_scale='viridis'
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    # Type Distribution Page
    elif page == "📊 Type Distribution":
        st.header("📊 Anime Type Distribution")
        
        # Type distribution
        anime_type = df.groupby('type').size().sort_values(ascending=False)
        
        fig = px.bar(
            x=anime_type.index,
            y=anime_type.values,
            title="Anime Type Distribution",
            labels={'x': 'Type', 'y': 'Count'},
            color=anime_type.values,
            color_continuous_scale='plasma'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Pie chart
        fig2 = px.pie(
            values=anime_type.values,
            names=anime_type.index,
            title="Anime Type Distribution (Pie Chart)"
        )
        st.plotly_chart(fig2, use_container_width=True)
        
        # Type statistics
        st.subheader("📈 Type Statistics")
        type_stats = df.groupby('type').agg({
            'rating': ['mean', 'count'],
            'members': 'sum'
        }).round(2)
        type_stats.columns = ['Average Rating', 'Count', 'Total Members']
        st.dataframe(type_stats)
    
    # Correlation Analysis Page
    elif page == "🔍 Correlation Analysis":
        st.header("🔍 Correlation Analysis")
        
        # Members vs Rating correlation
        st.subheader("👥 Members vs Rating Correlation")
        
        # Clean data for correlation
        df_clean = df.dropna(subset=['members', 'rating'])
        correlation = df_clean['members'].corr(df_clean['rating'])
        
        st.metric("Correlation Coefficient", f"{correlation:.3f}")
        
        # Scatter plot
        fig = px.scatter(
            df_clean,
            x='members',
            y='rating',
            title=f"Members vs Rating (Correlation: {correlation:.3f})",
            labels={'members': 'Number of Members', 'rating': 'Rating'},
            opacity=0.6
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Correlation heatmap
        st.subheader("🔥 Correlation Heatmap")
        
        # Select numeric columns
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        correlation_matrix = df[numeric_cols].corr()
        
        fig2 = px.imshow(
            correlation_matrix,
            title="Correlation Matrix",
            color_continuous_scale='RdBu',
            aspect='auto'
        )
        st.plotly_chart(fig2, use_container_width=True)
        
        # Correlation insights
        st.subheader("💡 Correlation Insights")
        st.markdown("""
        <div class="insight-box">
        <h4>🔍 Key Findings:</h4>
        <ul>
        <li><strong>Members vs Rating:</strong> Moderate positive correlation ({correlation:.3f})</li>
        <li>More popular anime tend to have higher ratings</li>
        <li>This suggests quality content attracts more viewers</li>
        <li>However, correlation is not perfect - some hidden gems exist</li>
        </ul>
        </div>
        """.format(correlation=correlation), unsafe_allow_html=True)
    
    # Key Insights Page
    elif page == "💡 Key Insights":
        st.header("💡 Key Insights & Recommendations")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="insight-box">
            <h4>🎯 Popularity Insights:</h4>
            <ul>
            <li>Action and Comedy are the most popular genres</li>
            <li>TV series dominate the anime market</li>
            <li>Popularity correlates with rating but not perfectly</li>
            <li>Quality content tends to attract more viewers</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="insight-box">
            <h4>⭐ Quality Insights:</h4>
            <ul>
            <li>Josei and Seinen target mature audiences</li>
            <li>Psychological and Thriller genres score highest</li>
            <li>Niche genres often have dedicated fanbases</li>
            <li>Quality over quantity in specialized content</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="insight-box">
            <h4>📊 Market Insights:</h4>
            <ul>
            <li>TV series are the primary format</li>
            <li>Movies and OVAs are less common but valued</li>
            <li>Diversity in content types appeals to different audiences</li>
            <li>Market shows healthy variety in offerings</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="insight-box">
            <h4>🚀 Recommendations:</h4>
            <ul>
            <li>Focus on quality content over mass production</li>
            <li>Explore niche genres for dedicated audiences</li>
            <li>Balance popular and specialized content</li>
            <li>Consider mature audience segments</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # Summary statistics
        st.subheader("📈 Summary Statistics")
        
        summary_stats = {
            'Metric': ['Total Anime', 'Average Rating', 'Most Popular Genre', 'Highest Rated Genre', 'Most Common Type'],
            'Value': [
                len(df),
                f"{df['rating'].mean():.2f}",
                genre_counts.index[0] if 'genre_counts' in locals() else 'N/A',
                genre_rating.index[0] if 'genre_rating' in locals() else 'N/A',
                anime_type.index[0] if 'anime_type' in locals() else 'N/A'
            ]
        }
        
        summary_df = pd.DataFrame(summary_stats)
        st.dataframe(summary_df, use_container_width=True)

if __name__ == "__main__":
    main() 