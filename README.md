# Student Performance Analytics

A complete data analytics pipeline that takes raw student marks through
cleaning, exploratory analysis, visualization, database storage, and an
interactive dashboard.

## What this project does

1. **Load & clean data** — handles missing values, duplicates, and out-of-range marks.
2. **Explore the data** — subject averages, correlations, top performers.
3. **Visualize** — bar chart of student averages, correlation heatmap.
4. **Statistics** — mean, median, standard deviation, quartiles.
5. **Store in SQL** — a MySQL database with `students` and `departments` tables,
   including ranking (`RANK()`), conditional logic (`CASE`), and a `LEFT JOIN`.
6. **Dashboard** — a live interactive report built in Google Looker Studio,
   connected directly to the cleaned dataset, with a bar chart and grade filter.

## Tools used

- **Python**: pandas, numpy, matplotlib, seaborn
- **Database**: MySQL (via VS Code MySQL extension)
- **Spreadsheet**: Google Sheets (formulas, sorting, charts)
- **Dashboard**: Google Looker Studio

## Project structure

```
student-performance-analytics/
├── data/
│   └── students_cleaned.csv       # cleaned dataset output
├── scripts/
│   └── analysis.py                # cleaning + EDA + visualization + stats
├── sql/
│   └── queries.sql                # database schema + queries
├── dashboard/
│   ├── student_averages.png       # chart output
│   └── correlation_heatmap.png    # chart output
└── README.md
```

## How to run

1. `pip install pandas numpy matplotlib seaborn`
2. `cd scripts && python analysis.py`
3. Open `sql/queries.sql` in the VS Code MySQL extension and run it against a database.
4. View the dashboard: [add your Looker Studio share link here]

## What I learned

- Turning messy raw data into a clean, analysis-ready dataset
- Using SQL for storage, filtering, ranking, and joining relational data
- Building a live dashboard that updates from a connected data source
- Structuring a data project the way it would look in a real job
