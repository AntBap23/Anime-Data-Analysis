#!/bin/bash

echo "🚀 Anime Data Analysis Streamlit App Setup"
echo "=========================================="

# Check if Python is installed (try both python3 and python)
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ Python is not installed or not in PATH"
    echo "Please install Python from https://python.org"
    exit 1
fi

echo "✅ Found Python: $($PYTHON_CMD --version)"

# Create virtual environment if it doesn't exist
if [ ! -d "anime_analysis_env" ]; then
    echo "🔄 Creating virtual environment..."
    $PYTHON_CMD -m venv anime_analysis_env
    if [ $? -ne 0 ]; then
        echo "❌ Failed to create virtual environment"
        exit 1
    fi
fi

# Activate virtual environment and install dependencies
echo "🔄 Activating virtual environment and installing dependencies..."
source anime_analysis_env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo "✅ Setup completed successfully!"
echo ""
echo "🎌 Starting Anime Data Analysis Dashboard..."
echo "📱 The app will open in your browser at http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the app"
echo ""

# Run the Streamlit app
streamlit run app.py 