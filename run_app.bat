@echo off
echo 🚀 Anime Data Analysis Streamlit App Setup
echo ==========================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist "anime_analysis_env" (
    echo 🔄 Creating virtual environment...
    python -m venv anime_analysis_env
    if errorlevel 1 (
        echo ❌ Failed to create virtual environment
        pause
        exit /b 1
    )
)

REM Activate virtual environment and install dependencies
echo 🔄 Activating virtual environment and installing dependencies...
call anime_analysis_env\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

echo ✅ Setup completed successfully!
echo.
echo 🎌 Starting Anime Data Analysis Dashboard...
echo 📱 The app will open in your browser at http://localhost:8501
echo.
echo Press Ctrl+C to stop the app
echo.

REM Run the Streamlit app
streamlit run app.py

pause 