#!/usr/bin/env python3
"""
Building Energy Predictor - Terminal Launcher
Run this script from terminal: python run_app.py
"""

import subprocess
import sys
import os

def run_app():
    """Run the streamlit app from the project directory"""
    
    # Get the project directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)
    
    # Path to venv python
    venv_python = os.path.join(project_dir, '.venv', 'bin', 'python')
    streamlit_app = os.path.join(project_dir, '.venv', 'streamlit_app_enhanced.py')
    
    # Check if venv exists
    if not os.path.exists(venv_python):
        print("❌ Error: Virtual environment not found!")
        print(f"Expected at: {venv_python}")
        print("\nTo fix this, run:")
        print("  python3 -m venv .venv")
        print("  .venv/bin/pip install --upgrade pip")
        print("  .venv/bin/pip install pandas numpy scikit-learn xgboost lightgbm joblib streamlit plotly faker")
        sys.exit(1)
    
    # Check if streamlit app exists
    if not os.path.exists(streamlit_app):
        print(f"❌ Error: Streamlit app not found at {streamlit_app}")
        sys.exit(1)
    
    print("🚀 Starting Building Energy Predictor...")
    print(f"📁 Project directory: {project_dir}")
    print(f"🐍 Using Python: {venv_python}\n")
    
    # Run streamlit
    try:
        subprocess.run(
            [venv_python, '-m', 'streamlit', 'run', streamlit_app],
            cwd=project_dir
        )
    except KeyboardInterrupt:
        print("\n\n✅ Application stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error running app: {e}")
        sys.exit(1)

if __name__ == '__main__':
    run_app()
