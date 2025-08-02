# 🎌 Anime Data Analysis Dashboard

A comprehensive Streamlit web application for analyzing anime data with interactive visualizations and insights.

## 📊 Features

- **Interactive Dashboard**: Beautiful, responsive web interface
- **Genre Analysis**: Explore popular genres and their ratings
- **Rating Analysis**: Distribution and statistics of anime ratings
- **Type Distribution**: Analysis of different anime formats (TV, Movie, OVA, etc.)
- **Correlation Analysis**: Relationships between popularity and ratings
- **Key Insights**: Actionable insights and recommendations

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

#### Windows Users:
```bash
# Double-click the run_app.bat file or run:
run_app.bat
```

#### Unix/Linux/Mac Users:
```bash
# Make the script executable and run:
chmod +x run_app.sh
./run_app.sh
```

### Option 2: Manual Setup

1. **Clone or download this repository**
2. **Create a virtual environment**:
   ```bash
   python -m venv anime_analysis_env
   ```

3. **Activate the virtual environment**:
   - Windows: `anime_analysis_env\Scripts\activate`
   - Unix/Linux/Mac: `source anime_analysis_env/bin/activate`

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

6. **Open your browser** and go to: `http://localhost:8501`

## 📋 Requirements

- Python 3.7 or higher
- Internet connection (for first-time dependency installation)

## 📦 Dependencies

- `streamlit` - Web application framework
- `pandas` - Data manipulation and analysis
- `numpy` - Numerical computing
- `matplotlib` - Basic plotting
- `seaborn` - Statistical data visualization
- `plotly` - Interactive plots
- `scikit-learn` - Machine learning utilities

## 🎯 Dashboard Sections

### 🏠 Overview
- Dataset statistics and metrics
- Data preview and information
- Missing value analysis

### 📈 Genre Analysis
- Top genres by popularity
- Genre rating correlations
- Interactive bar charts and insights

### ⭐ Rating Analysis
- Rating distribution histogram
- Top-rated anime list
- Rating statistics by type

### 📊 Type Distribution
- Anime format distribution
- Interactive pie and bar charts
- Type-specific statistics

### 🔍 Correlation Analysis
- Members vs Rating correlation
- Correlation heatmap
- Statistical insights

### 💡 Key Insights
- Actionable business insights
- Market recommendations
- Summary statistics

## 🛠️ Customization

### Adding New Visualizations
1. Add your analysis code to the appropriate section in `app.py`
2. Use Plotly for interactive charts
3. Follow the existing code structure and styling

### Modifying Styling
- Edit the CSS in the `st.markdown()` section
- Customize colors, fonts, and layout
- Add new CSS classes as needed

### Adding New Data
- Replace `anime.csv` with your dataset
- Update column names in the code if needed
- Ensure data format compatibility

## 📁 Project Structure

```
Anime-Data-Analysis/
├── app.py                 # Main Streamlit application
├── anime.csv              # Anime dataset
├── requirements.txt       # Python dependencies
├── run_app.bat           # Windows setup script
├── run_app.sh            # Unix/Linux/Mac setup script
├── setup_environment.py  # Python setup script
├── eda.ipynb             # Original Jupyter notebook
├── rating_joined.ipynb   # Rating analysis notebook
├── Insights.txt          # Key insights document
└── README.md             # This file
```

## 🔧 Troubleshooting

### Common Issues

1. **Python not found**:
   - Ensure Python is installed and in your PATH
   - Try using `python3` instead of `python`

2. **Port already in use**:
   - Streamlit will automatically use the next available port
   - Check the terminal output for the correct URL

3. **Dependencies installation fails**:
   - Update pip: `pip install --upgrade pip`
   - Try installing packages individually
   - Check your internet connection

4. **Data loading errors**:
   - Ensure `anime.csv` is in the same directory as `app.py`
   - Check file permissions and format

### Getting Help

- Check the terminal output for error messages
- Verify all dependencies are installed correctly
- Ensure your virtual environment is activated

## 📈 Future Enhancements

- [ ] User authentication and personalization
- [ ] Advanced filtering and search capabilities
- [ ] Export functionality for charts and data
- [ ] Real-time data updates
- [ ] Machine learning recommendations
- [ ] Mobile-responsive design improvements

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Streamlit team for the amazing framework
- Plotly for interactive visualizations
- The anime community for the dataset

---

**Happy Analyzing! 🎌📊**
