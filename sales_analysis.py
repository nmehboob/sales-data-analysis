import statistics

def analyze_sales(sales_data):
    """Analyze sales data and return statistics"""
    
    # Calculate basic statistics
    total_sales = sum(sales_data)
    average_sales = statistics.mean(sales_data)
    highest_sales = max(sales_data)
    lowest_sales = min(sales_data)
    median_sales = statistics.median(sales_data)
    
    # Find which day had highest and lowest sales
    best_day = sales_data.index(highest_sales) + 1
    worst_day = sales_data.index(lowest_sales) + 1
    
    return {
        'total': total_sales,
        'average': average_sales,
        'highest': highest_sales,
        'lowest': lowest_sales,
        'median': median_sales,
        'best_day': best_day,
        'worst_day': worst_day
    }

def display_results(results):
    """Display analysis results in a nice format"""
    print("\n" + "="*40)
    print("      SALES ANALYSIS REPORT")
    print("="*40)
    print(f"Total Sales:        ${results['total']:,.2f}")
    print(f"Average Sales:      ${results['average']:,.2f}")
    print(f"Highest Sales:      ${results['highest']:,.2f} (Day {results['best_day']})")
    print(f"Lowest Sales:       ${results['lowest']:,.2f} (Day {results['worst_day']})")
    print(f"Median Sales:       ${results['median']:,.2f}")
    print("="*40)
    
    # Performance indicator
    if results['average'] > 5000:
        print("Status: EXCELLENT Performance! 🎉")
    elif results['average'] > 3000:
        print("Status: GOOD Performance ✓")
    else:
        print("Status: Need Improvement")

def main():
    print("=== Sales Data Analysis Tool ===\n")
    
    # Option 1: Enter data manually
    print("Enter daily sales (enter 0 to finish):")
    sales_data = []
    day = 1
    
    while True:
        try:
            sale = float(input(f"Day {day} sales: $"))
            if sale == 0:
                break
            if sale < 0:
                print("Sales cannot be negative! Try again.")
                continue
            sales_data.append(sale)
            day += 1
        except ValueError:
            print("Please enter a valid number!")
    
    if len(sales_data) == 0:
        print("No data entered!")
        return
    
    # Analyze the data
    results = analyze_sales(sales_data)
    
    # Display results
    display_results(results)
    
    # Show trend
    print("\nSales Trend:")
    for i, sale in enumerate(sales_data, 1):
        bar_length = int(sale / 100)
        bar = "█" * bar_length
        print(f"Day {i:2d}: {bar} ${sale:,.2f}")

if __name__ == "__main__":
    main()
