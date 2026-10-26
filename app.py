import sys
import os
import csv
import matplotlib
import matplotlib.pyplot as plt
from jinja2 import Template

Student_Template = Template(
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <title>Student Data</title>
    </head>
    <body>
    <h1>Student Details</h1>
    <table border="1">
    <thead>
    <tr>
    <th>Student ID</th>
    <th>Course ID</th>
    <th> Marks</th>
    </tr>
    </thead>
    <tbody>
    {% for r in rows %}
    <tr>
    <td>{{ r[0] }}</td>}
    <td>{{ r[1] }}</td>
    <td>{{ r[2] }}</td>
    </tr>
    {% endfor %}
    <tr>
    <td colspan="2" style = "text-align: center"> Total Marks</td>
    <td> {{ total }} </td>
    </tr>
    </tbody>
    </table>
    </body>
    </html>
    """
)
COURSE_TEMPLATE = Template("""<!DOCTYPE html>
<html lang="en">
<head>
<title>Course Data</title>
</head>
<body>
<h1>Course Details</h1>
<table border="1">
<thead>
<tr><th>Average Marks</th><th>Maximum Marks</th></tr>
</thead>
<tbody>
<tr><td>{{ avg }}</td><td>{{ maximum }}</td></tr>
</tbody>
</table>
<br>
<img src="histogram.png" alt="Histogram of marks">
</body>
</html>
""")
ERROR_TEMPLATE = Template("""<!DOCTYPE html>
<html lang="en">
<head>
<title>Something Went Wrong</title>
</head>
<body>
<h1>Wrong Inputs</h1>
<p>Something went wrong</p>
</body>
</html>
""")