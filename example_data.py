# Example: Using the analysis with sample data

from sales_analysis import analyze_sales, display_results

# Sample weekly sales data
weekly_sales = [4500, 5200, 3800, 6100, 5500, 4200, 3900]

print("Analyzing weekly sales data...\n")
print("Sales data:", weekly_sales)

results = analyze_sales(weekly_sales)
display_results(results)
