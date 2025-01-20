import subprocess
import sys

def run_streamlit():
    subprocess.run([sys.executable, "-m", "streamlit", "run", "invests/Invest.py"])

if __name__ == "__main__":
    run_streamlit()