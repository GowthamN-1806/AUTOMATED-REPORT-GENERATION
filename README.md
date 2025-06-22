# AUTOMATED-REPORT-GENERATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: GOWTHAM N

*INTERN ID*: CT04DF178

*DOMAIN*: PYTHON

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH KUMAR

*DESCRIPTION*:

        For Task 2 of the CodTech Python Internship, the objective was to create an automated report generation system using Python. This task required the development of a script that could read data from a file, analyze it, and then generate a well-structured and formatted PDF report using libraries such as FPDF or ReportLab. The purpose of this task was to simulate real-world scenarios where data needs to be processed and presented in a professional format suitable for business reports, audits, or academic submissions. The focus was not only on correct data analysis but also on ensuring that the output report was aesthetically appealing and easy to interpret. To begin with, I selected a dataset in CSV format that contained nutritional information of food items from Starbucks, including columns such as Calories, Fat, Carbohydrates, Fiber, Protein, and Sodium. Using the `pandas` library, I read the CSV file and performed initial data cleaning by replacing missing values (represented by '-') with NaN values and converting relevant columns into numeric types to enable accurate statistical analysis. This preprocessing ensured that the data could be used reliably for generating summary statistics and visualizations.

Once the data was clean, I carried out basic data analysis. This included calculating mean, minimum, and maximum values for each nutritional metric and identifying high-calorie or high-fat items using conditional filtering. The insights from this analysis provided the content for the narrative part of the report. I also used `matplotlib.pyplot` to create various visualizations that added depth and clarity to the report. These visual elements included bar charts, pie charts, and distribution plots that conveyed how nutrients like fat, protein, or sodium varied across different food items. Each plot was saved as an image file to be later embedded in the PDF report. To generate the PDF report, I used the `FPDF` library, a lightweight and easy-to-use tool for creating PDF documents with Python. I started by creating a custom title page with a large, bold header that read “Starbucks Nutrition Report,” styled in Times New Roman font to give the document a formal appearance. I ensured that the layout was consistent and visually balanced by adjusting font sizes, margins, and spacing. On subsequent pages, I added both textual summaries and the visual plots that were generated earlier. Each section of the report was carefully structured to include a heading, a short descriptive paragraph, and a related chart. For example, under the heading “Fat vs. Calories,” I included a bar chart illustrating how fat content correlates with calorie count for different items. This visual approach made the report easy to follow and more informative than plain text.

Special care was taken to avoid layout issues, such as images overflowing onto the next page or being misaligned. I used the `FPDF.image()` method with precise coordinates to place each chart exactly where it needed to appear. The final report included all necessary sections: an introduction, data summary, individual nutrient analysis, and conclusions based on the visualized trends. Each page was neatly formatted, with attention given to font consistency and spacing. By completing this task, I gained practical experience in working with real datasets, performing exploratory data analysis, and automating report generation — a skill highly relevant in roles such as data analyst, business intelligence developer, or scientific researcher. I learned how to convert raw data into valuable insights and how to present those insights in a professional format that adds real value. Task 2 was not just a technical assignment; it mimicked the end-to-end process of analyzing and reporting data in a business or research environment, making it an immensely valuable learning experience.

