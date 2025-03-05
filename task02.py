import pandas as pd
from fpdf import FPDF

def analyze_data(file_path):
    df = pd.read_csv(file_path)
    summary = {
        'Total Employees': len(df),
        'Average Age': round(df['Age'].mean(), 2),
        'Average Salary': round(df['Salary'].mean(), 2),
        'Departments': df['Department'].nunique()
    }
    return df, summary

def generate_pdf_report(summary, file_name="report.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, "Employee Data Analysis Report", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", size=12)
    for key, value in summary.items():
        pdf.cell(0, 10, f"{key}: {value}", ln=True)
    
    pdf.output(file_name)
    print(f"PDF Report Generated: {file_name}")

if __name__ == "__main__":
    data_file = "sample_data.csv"  # Ensure this file exists
    df, summary = analyze_data(data_file)
    generate_pdf_report(summary)
