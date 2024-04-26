# index.py file
import base64
import datetime as dt
import random
import jinja2

# Step 1 - create data for report
salesTblRows = []
for k in range(10):
    costPu = random.randint(1, 15)
    nUnits = random.randint(100, 500)
    salesTblRows.append({"sNo": k+1, "name": "Item "+str(k+1),
                         "cPu": costPu, "nUnits": nUnits, "revenue": costPu*nUnits})

topItems = [x["name"] for x in sorted(
    salesTblRows, key=lambda x: x["revenue"], reverse=True)][0:3]

todayStr = dt.datetime.now().strftime("%d-%b-%Y")

# create logo image from file
with open("templates/logo.png", "rb") as f:
    logoImg = base64.b64encode(f.read()).decode()

# data for injecting into jinja2 template
context = {
    "reportDtStr": todayStr,
    "salesTblRows": salesTblRows,
    "topItemsRows": topItems,
    "logoImg": logoImg,
}

# Step 2 - create jinja template object from file
template = jinja2.Environment(
    loader=jinja2.FileSystemLoader("./templates"),
    autoescape=jinja2.select_autoescape
).get_template("sales_report_template_plotly.html")

# Step 3 - render data in jinja template
reportText = template.render(context)

# Step 4 - Save genereate text as a HTML file
reportPath = "./reports/sales_report.html"
with open(reportPath, mode='w') as f:
    f.write(reportText)