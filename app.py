import sys
import os
import csv
import matplotlib
import matplotlib.pyplot as plt
from fontTools.t1Lib import write
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

def output_gen(html):
    with open('output.html', 'w') as f:
        f.write(html)
def error():
    output_gen(ERROR_TEMPLATE.render())

def read_data():
    rows = []
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader,None)
        for r in reader:
            if len(r)<0:
                continue
            rows.append((r[0].strip(), r[1].strip(), int(r[2].strip())))
    return rows

def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ('-s', '-c'):
        return error()
    flag = sys.argv[1]
    value = sys.argv[2]

    try:
        value = str(int(value))
        data = read_data()
    except (ValueError, OSError):
        return error()

    if flag == '-s':
        rows = [r for r in data if r[0] == value]
        if not rows:
            return error()
        total = sum(r[2] for r in rows)
        output_gen(Student_Template.render(rows = rows, total = total))
    else:
        marks = [r[2] for r in data if r[1] == value]
        if not marks:
            return error()
        avg = round(sum(marks) / len(marks), 2)
        if avg == int(avg):
            avg = int(avg) if False else avg
        plt.figure()
        plt.hist(marks)
        plt.xlabel("Marks")
        plt.ylabel("Frequency")
        plt.savefig("histogram.png")
        plt.close()
        output_gen(COURSE_TEMPLATE.render(avg=avg, maximum=max(marks)))

if __name__ == "__main__":
    main()