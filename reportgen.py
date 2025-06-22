import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os
import webbrowser
import time

def read_data(file_path):
    df = pd.read_csv(file_path)
    df.replace('-', pd.NA, inplace=True)
    numeric_cols = ['Calories', 'Fat (g)', 'Carb. (g)', 'Fiber (g)', 'Protein', 'Sodium']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

def create_visuals(df):
    os.makedirs("images", exist_ok=True)
    label_col = 'Unnamed: 0' if 'Unnamed: 0' in df.columns else df.columns[0]

    if 'Calories' in df.columns:
        top_cal = df.nlargest(10, 'Calories')
        if not top_cal.empty:
            plt.figure(figsize=(10, 6))
            plt.bar(top_cal[label_col].astype(str), top_cal['Calories'], color='orange')
            plt.title('Top 10 Highest Calorie Drinks', fontname='Times New Roman', fontsize=22)
            plt.xticks(rotation=45, ha='right', fontname='Times New Roman')
            plt.yticks(fontname='Times New Roman')
            plt.tight_layout()
            plt.savefig("images/top_calories.png")
            plt.close()

    if {'Sodium', 'Calories'}.issubset(df.columns):
        temp = df[['Sodium', 'Calories']].dropna()
        temp = temp[(temp['Sodium'] > 0) & (temp['Calories'] > 0)]
        if not temp.empty:
            plt.figure(figsize=(8, 6))
            plt.scatter(temp['Sodium'], temp['Calories'], color='green', alpha=0.7)
            plt.title("Sodium vs Calories", fontname='Times New Roman', fontsize=22)
            plt.xlabel("Sodium", fontname='Times New Roman')
            plt.ylabel("Calories", fontname='Times New Roman')
            plt.xticks(fontname='Times New Roman')
            plt.yticks(fontname='Times New Roman')
            plt.tight_layout()
            plt.savefig("images/Sodium_vs_calories.png")
            plt.close()

    if {'Fat (g)', 'Calories'}.issubset(df.columns):
        temp = df[['Fat (g)', 'Calories']].dropna()
        temp = temp[(temp['Fat (g)'] > 0) & (temp['Calories'] > 0)]
        if not temp.empty:
            plt.figure(figsize=(8, 6))
            plt.scatter(temp['Fat (g)'], temp['Calories'], color='blue', alpha=0.7)
            plt.title("Fat vs Calories", fontname='Times New Roman', fontsize=22)
            plt.xlabel("Fat (g)", fontname='Times New Roman')
            plt.ylabel("Calories", fontname='Times New Roman')
            plt.xticks(fontname='Times New Roman')
            plt.yticks(fontname='Times New Roman')
            plt.tight_layout()
            plt.savefig("images/fat_vs_calories.png")
            plt.close()

    if 'Protein' in df.columns:
        temp = df['Protein'].dropna()
        temp = temp[temp > 0]
        if not temp.empty:
            plt.figure(figsize=(8, 6))
            temp.hist(bins=20, color='purple')
            plt.title('Protein Content Distribution', fontname='Times New Roman', fontsize=22)
            plt.xlabel('Protein', fontname='Times New Roman')
            plt.ylabel('Number of Drinks', fontname='Times New Roman')
            plt.xticks(fontname='Times New Roman')
            plt.yticks(fontname='Times New Roman')
            plt.tight_layout()
            plt.savefig("images/sodium_distribution.png")
            plt.close()

class PDFReport(FPDF):
    def header(self):
        pass

    def add_title_page(self, title):
        self.add_page()
        words = title.split()
        font_size = 70
        self.set_font('Times', 'B', font_size)
        line_height = font_size * 0.5
        total_text_height = line_height * len(words)
        page_height = self.h - 2 * self.t_margin
        y_start = self.t_margin + (page_height - total_text_height) / 2
        y = y_start
        for word in words:
            self.set_xy(0, y)
            self.cell(0, line_height, word, align='C', ln=1)
            y += line_height

    def add_image_page(self, image_path, title):
        self.add_page()
        self.set_font('Times', 'B', 22)
        self.cell(0, 10, title, ln=True)
        self.ln(5)
        if os.path.exists(image_path):
            self.image(image_path, w=170)
        else:
            self.set_font('Times', 'I', 12)
            self.cell(0, 10, "Image not found.", ln=True)

    def add_table(self, df, title, col_widths=None, cell_height=18, header_fill_color=(220, 220, 255)):
        self.add_page()
        self.set_font('Times', 'B', 20)
        self.cell(0, 10, title, ln=True, align='C')
        self.ln(5)

        if col_widths is None:
            col_widths = [self.w / (len(df.columns) + 2)] * len(df.columns)

        if len(col_widths) != len(df.columns):
            raise ValueError("Length of col_widths must match number of dataframe columns")

        self.set_fill_color(*header_fill_color)
        self.set_text_color(0)
        self.set_font('Times', 'B', 14)
        for i, col in enumerate(df.columns):
            self.cell(col_widths[i], cell_height, str(col), border=1, fill=True, align='C')
        self.ln()

        self.set_font('Times', '', 12)
        for _, row in df.iterrows():
            for i, item in enumerate(row):
                self.cell(col_widths[i], cell_height, str(item), border=1)
            self.ln()

    def add_summary(self, df):
        desc = df.describe().round(2)
        self.add_table(desc.reset_index(), "Summary Statistics")


def main():
    file_path = "starbucks-menu-nutrition-drinks.csv"
    df = read_data(file_path)
    create_visuals(df)
    pdf = PDFReport()
    pdf.add_title_page("STARBUCKS NUTRITION REPORT")
    pdf.add_summary(df.select_dtypes(include='number'))
    label_col = 'Unnamed: 0' if 'Unnamed: 0' in df.columns else df.columns[0]

    if 'Calories' in df.columns:
        top_cal = df.nlargest(10, 'Calories')[[label_col, 'Calories']]
        pdf.add_table(top_cal, "Top 10 Highest-Calorie Drinks", col_widths=[120, 50], cell_height=15)

    if 'Sodium' in df.columns:
        top_sodium = df.nlargest(10, 'Sodium')[[label_col, 'Sodium']]
        pdf.add_table(top_sodium, "Top 10 Sodium-Rich Drinks", col_widths=[120, 50], cell_height=15)

    pdf.add_image_page("images/top_calories.png", "Top 10 Calorie Drinks")
    pdf.add_image_page("images/fat_vs_calories.png", "Fat vs Calories")
    pdf.add_image_page("images/Sodium_vs_calories.png", "Sodium vs Calories")
    pdf.add_image_page("images/sodium_distribution.png", "Protein Distribution")

    pdf.output("Starbucks_Report.pdf")
    print("Report generated: Starbucks_Report.pdf")
    webbrowser.open("Starbucks_Report.pdf")

if __name__ == "__main__":
    main()
