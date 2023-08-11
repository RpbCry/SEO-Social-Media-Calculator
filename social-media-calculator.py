import tkinter as tk
from tkinter import ttk

def calculate_ctr():
    try:
        total_clicks = int(clicks_entry.get())
        total_impressions = int(impressions_entry.get())

        avg_ctr = (total_clicks / total_impressions) * 100
        result_label.config(text=f"Avg. CTR: {avg_ctr:.2f}%")
    except ValueError:
        result_label.config(text="Invalid input")

def copy_result():
    result = result_label.cget("text")
    if result:
        avg_ctr = result.split(": ")[1]
        root.clipboard_clear()
        root.clipboard_append(avg_ctr)
        root.update()

def calculate_clicks():
    try:
        avg_ctr = float(ctr_entry.get())
        total_impressions = int(impressions_entry2.get())

        total_clicks = (avg_ctr / 100) * total_impressions
        result_label2.config(text=f"Total Clicks: {total_clicks:.0f}")
    except ValueError:
        result_label2.config(text="Invalid input")

def copy_result_clicks():
    result = result_label2.cget("text")
    if result:
        total_clicks = result.split(": ")[1]
        root.clipboard_clear()
        root.clipboard_append(total_clicks)
        root.update()

def calculate_impressions():
    try:
        avg_ctr = float(ctr_entry2.get())
        total_clicks = int(clicks_entry2.get())

        total_impressions = (total_clicks / (avg_ctr / 100))
        result_label3.config(text=f"Total Impressions: {total_impressions:.0f}")
    except ValueError:
        result_label3.config(text="Invalid input")

def copy_result_impressions():
    result = result_label3.cget("text")
    if result:
        total_impressions = result.split(": ")[1]
        root.clipboard_clear()
        root.clipboard_append(total_impressions)
        root.update()

def calculate_cvr():
    try:
        total_conversions = int(conversions_entry.get())
        total_clicks = int(clicks_entry3.get())

        cvr = (total_conversions / total_clicks) * 100
        result_label4.config(text=f"CVR: {cvr:.2f}%")
    except ValueError:
        result_label4.config(text="Invalid input")

def copy_result_cvr():
    result = result_label4.cget("text")
    if result:
        cvr = result.split(": ")[1]
        root.clipboard_clear()
        root.clipboard_append(cvr)
        root.update()

def calculate_avg_conversion_value():
    try:
        total_conversion_value = float(conversion_value_entry.get())
        total_conversions = int(conversions_entry2.get())

        avg_conversion_value = total_conversion_value / total_conversions
        result_label5.config(text=f"Avg. Conversion Value: {avg_conversion_value:.2f}")
    except ValueError:
        result_label5.config(text="Invalid input")

def copy_result_avg_conversion_value():
    result = result_label5.cget("text")
    if result:
        avg_conversion_value = result.split(": ")[1]
        root.clipboard_clear()
        root.clipboard_append(avg_conversion_value)
        root.update()

def calculate_roas():
    try:
        cost = float(cost_entry.get())
        total_conversion_value = float(conversion_value_entry2.get())

        roas = total_conversion_value / cost
        result_label6.config(text=f"ROAS: {roas:.2f}")
    except ValueError:
        result_label6.config(text="Invalid input")

def copy_result_roas():
    result = result_label6.cget("text")
    if result:
        roas = result.split(": ")[1]
        root.clipboard_clear()
        root.clipboard_append(roas)
        root.update()

def calculate_reach():
    try:
        total_impressions = int(impressions_entry3.get())
        frequency = float(frequency_entry.get())

        reach = total_impressions / frequency
        result_label7.config(text=f"Reach: {reach:.0f}")
    except ValueError:
        result_label7.config(text="Invalid input")

def copy_result_reach():
    result = result_label7.cget("text")
    if result:
        reach = result.split(": ")[1]
        root.clipboard_clear()
        root.clipboard_append(reach)
        root.update()

def calculate_engagement_reach_based():
    try:
        total_engagements = int(engagements_entry.get())
        total_reach = int(reach_entry.get())

        engagement_percentage = (total_engagements / total_reach) * 100
        result_label8.config(text=f"Engagement % (Reach Based): {engagement_percentage:.2f}%")
    except ValueError:
        result_label8.config(text="Invalid input")

def copy_result_engagement():
    result = result_label8.cget("text")
    if result:
        engagement_percentage = result.split(": ")[1]
        root.clipboard_clear()
        root.clipboard_append(engagement_percentage)
        root.update()

# Create main window
root = tk.Tk()
root.title("CTR Calculator")

# Create tabs
tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)
tab7 = ttk.Frame(tab_control)
tab8 = ttk.Frame(tab_control)

tab_control.add(tab1, text="Calculate Avg. CTR")
tab_control.add(tab2, text="Calculate Clicks")
tab_control.add(tab3, text="Calculate Impressions")
tab_control.add(tab4, text="Calculate CVR")
tab_control.add(tab5, text="Calculate Avg. Conversion Value")
tab_control.add(tab6, text="Calculate ROAS")
tab_control.add(tab7, text="Calculate Reach")
tab_control.add(tab8, text="Calculate Engagement % (Reach Based)")

tab_control.pack(expand=1, fill="both")

# Tab 1: Calculate Avg. CTR
clicks_label = tk.Label(tab1, text="Total Clicks:")
clicks_label.pack()

clicks_entry = tk.Entry(tab1)
clicks_entry.pack()

impressions_label = tk.Label(tab1, text="Total Impressions:")
impressions_label.pack()

impressions_entry = tk.Entry(tab1)
impressions_entry.pack()

calculate_button = tk.Button(tab1, text="Calculate Avg. CTR", command=calculate_ctr)
calculate_button.pack()

result_label = tk.Label(tab1, text="")
result_label.pack()

copy_button = tk.Button(tab1, text="Copy Result", command=copy_result)
copy_button.pack()

# Tab 2: Calculate Clicks
ctr_label = tk.Label(tab2, text="Average CTR (%):")
ctr_label.pack()

ctr_entry = tk.Entry(tab2)
ctr_entry.pack()

impressions_label2 = tk.Label(tab2, text="Total Impressions:")
impressions_label2.pack()

impressions_entry2 = tk.Entry(tab2)
impressions_entry2.pack()

calculate_button2 = tk.Button(tab2, text="Calculate Clicks", command=calculate_clicks)
calculate_button2.pack()

result_label2 = tk.Label(tab2, text="")
result_label2.pack()

copy_button2 = tk.Button(tab2, text="Copy Result", command=copy_result_clicks)
copy_button2.pack()

# Tab 3: Calculate Impressions
ctr_label2 = tk.Label(tab3, text="Average CTR (%):")
ctr_label2.pack()

ctr_entry2 = tk.Entry(tab3)
ctr_entry2.pack()

clicks_label2 = tk.Label(tab3, text="Total Clicks:")
clicks_label2.pack()

clicks_entry2 = tk.Entry(tab3)
clicks_entry2.pack()

calculate_button3 = tk.Button(tab3, text="Calculate Impressions", command=calculate_impressions)
calculate_button3.pack()

result_label3 = tk.Label(tab3, text="")
result_label3.pack()

copy_button3 = tk.Button(tab3, text="Copy Result", command=copy_result_impressions)
copy_button3.pack()

# Tab 4: Calculate CVR
clicks_label3 = tk.Label(tab4, text="Total Clicks:")
clicks_label3.pack()

clicks_entry3 = tk.Entry(tab4)
clicks_entry3.pack()

conversions_label = tk.Label(tab4, text="Total Conversions:")
conversions_label.pack()

conversions_entry = tk.Entry(tab4)
conversions_entry.pack()

calculate_button4 = tk.Button(tab4, text="Calculate CVR", command=calculate_cvr)
calculate_button4.pack()

result_label4 = tk.Label(tab4, text="")
result_label4.pack()

copy_button4 = tk.Button(tab4, text="Copy Result", command=copy_result_cvr)
copy_button4.pack()

# Tab 5: Calculate Avg. Conversion Value
conversion_value_label = tk.Label(tab5, text="Total Conversion Value:")
conversion_value_label.pack()

conversion_value_entry = tk.Entry(tab5)
conversion_value_entry.pack()

conversions_label2 = tk.Label(tab5, text="Number of Conversions:")
conversions_label2.pack()

conversions_entry2 = tk.Entry(tab5)
conversions_entry2.pack()

calculate_button5 = tk.Button(tab5, text="Calculate Avg. Conversion Value", command=calculate_avg_conversion_value)
calculate_button5.pack()

result_label5 = tk.Label(tab5, text="")
result_label5.pack()

copy_button5 = tk.Button(tab5, text="Copy Result", command=copy_result_avg_conversion_value)
copy_button5.pack()

# Tab 6: Calculate ROAS
cost_label = tk.Label(tab6, text="Cost:")
cost_label.pack()

cost_entry = tk.Entry(tab6)
cost_entry.pack()

conversion_value_label2 = tk.Label(tab6, text="Total Conversion Value:")
conversion_value_label2.pack()

conversion_value_entry2 = tk.Entry(tab6)
conversion_value_entry2.pack()

calculate_button6 = tk.Button(tab6, text="Calculate ROAS", command=calculate_roas)
calculate_button6.pack()

result_label6 = tk.Label(tab6, text="")
result_label6.pack()

copy_button6 = tk.Button(tab6, text="Copy Result", command=copy_result_roas)
copy_button6.pack()

# Tab 7: Calculate Reach
impressions_label3 = tk.Label(tab7, text="Total Impressions:")
impressions_label3.pack()

impressions_entry3 = tk.Entry(tab7)
impressions_entry3.pack()

frequency_label = tk.Label(tab7, text="Frequency:")
frequency_label.pack()

frequency_entry = tk.Entry(tab7)
frequency_entry.pack()

calculate_button7 = tk.Button(tab7, text="Calculate Reach", command=calculate_reach)
calculate_button7.pack()

result_label7 = tk.Label(tab7, text="")
result_label7.pack()

copy_button7 = tk.Button(tab7, text="Copy Result", command=copy_result_reach)
copy_button7.pack()

# Tab 8: Calculate Engagement % (Reach Based)
engagements_label = tk.Label(tab8, text="Total Engagements:")
engagements_label.pack()

engagements_entry = tk.Entry(tab8)
engagements_entry.pack()

reach_label = tk.Label(tab8, text="Total Reach:")
reach_label.pack()

reach_entry = tk.Entry(tab8)
reach_entry.pack()

calculate_button8 = tk.Button(tab8, text="Calculate Engagement % (Reach Based)", command=calculate_engagement_reach_based)
calculate_button8.pack()

result_label8 = tk.Label(tab8, text="")
result_label8.pack()

copy_button8 = tk.Button(tab8, text="Copy Result", command=copy_result_engagement)
copy_button8.pack()

# Start GUI main loop
root.mainloop()
