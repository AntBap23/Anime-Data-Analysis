#!/usr/bin/env python3
"""
Setup script for Anime Data Analysis Streamlit App
This script creates a virtual environment and installs all required dependencies.
"""

import subprocess
import sys
import os
import platform

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}: {e}")
        print(f"Error output: {e.stderr}")
        return False

def main():
    print("🚀 Setting up Anime Data Analysis Environment")
    print("=" * 50)
    
    # Check if Python is installed
    if not run_command("python --version", "Checking Python installation"):
        print("❌ Python is not installed or not in PATH")
        return False
    
    # Create virtual environment
    venv_name = "anime_analysis_env"
    
    if os.path.exists(venv_name):
        print(f"📁 Virtual environment '{venv_name}' already exists")
    else:
        if not run_command(f"python -m venv {venv_name}", "Creating virtual environment"):
            return False
    
    # Determine activation script based on OS
    if platform.system() == "Windows":
        activate_script = f"{venv_name}\\Scripts\\activate"
        pip_path = f"{venv_name}\\Scripts\\pip"
    else:
        activate_script = f"{venv_name}/bin/activate"
        pip_path = f"{venv_name}/bin/pip"
    
    # Install dependencies
    if not run_command(f"{pip_path} install --upgrade pip", "Upgrading pip"):
        return False
    
    if not run_command(f"{pip_path} install -r requirements.txt", "Installing dependencies"):
        return False
    
    print("\n" + "=" * 50)
    print("✅ Environment setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Activate the virtual environment:")
    
    if platform.system() == "Windows":
        print(f"   {venv_name}\\Scripts\\activate")
    else:
        print(f"   source {venv_name}/bin/activate")
    
    print("\n2. Run the Streamlit app:")
    print("   streamlit run app.py")
    
    print("\n3. Open your browser and go to: http://localhost:8501")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1) 