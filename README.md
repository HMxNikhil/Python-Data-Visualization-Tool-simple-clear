Got it ✅
Here’s your **updated README** with the project title as
**"Python-Data-Visualization-Tool-simple-clear"** — clean, structured, and GitHub-ready.

---

```markdown
# Python-Data-Visualization-Tool-simple-clear 📊

A modern **Python GUI application** for managing and visualizing NGO funding data.  
Built with **Tkinter**, **Pandas**, **Matplotlib**, and **Seaborn**, it allows you to easily **add, edit, search, sort, and visualize** funding records with beautiful graphs and export options.  

---

## ✨ Features
- **Full Data Management**
  - ➕ Add new funding records
  - 📝 Edit existing entries
  - ❌ Delete funding data
  - 🔍 Search by Year or Source
  - ↕️ Sort data by Year or Amount
- **Data Visualization**
  - Yearly funding comparison (Bar Chart)
  - Funding source distribution (Pie Chart)
  - Funding trend over time (Line Chart)
  - Funding amount distribution (Histogram)
- **Statistics**
  - Quick statistical summary (mean, median, min, max, etc.)
- **Export & Backup**
  - Export data to Excel
  - Backup CSV with timestamp
- **Themes**
  - 🌞 Light mode / 🌙 Dark mode toggle
- **User-Friendly Interface**
  - Hover effects on buttons
  - Simple and clean design

---

## 🛠 Modules Used
| Module | Type | Purpose |
|--------|------|---------|
| `pandas` | External | Data storage, CSV operations, sorting, grouping, statistics |
| `matplotlib` | External | Data visualization |
| `seaborn` | External | Stylish and advanced plotting |
| `tkinter` | Built-in | GUI creation |
| `os` | Built-in | File handling |
| `tkinter.messagebox` | Built-in | Pop-up alerts and info dialogs |
| `tkinter.ttk` | Built-in | Styled widgets |
| `tkinter.simpledialog` | Built-in | Input dialogs |
| `tkinter.filedialog` | Built-in | File selection dialogs |

---

## 📂 Project Structure
```

Python-Data-Visualization-Tool-simple-clear/
│── ngofunding\_fixed.py    # Main application file
│── ngo\_funding.csv        # Funding data (auto-created)
│── README.md              # Project documentation

````

---

## 📊 Graph Calculations
- **Yearly Funding**
  ```python
  df.groupby("Year")["Amount"].sum()
````

→ Calculates total funding for each year.

* **Funding by Source**

  ```python
  df.groupby("Source")["Amount"].sum()
  ```

  → Calculates total funding from each funding source.

* **Pie Chart Percentages**

  ```python
  (Amount per Source / Total Amount) * 100
  ```

  → Computes percentage share per funding source.

* **Funding Trend**
  → Plots yearly totals over time to identify growth or decline.

* **Funding Amount Distribution**
  → Uses histogram bins to show frequency of amounts.

---

## 🚀 Installation & Usage

1. **Clone this repository**

   ```bash
   git clone https://github.com/yourusername/Python-Data-Visualization-Tool-simple-clear.git
   cd Python-Data-Visualization-Tool-simple-clear
   ```

2. **Install dependencies**

   ```bash
   pip install pandas matplotlib seaborn
   ```

3. **Run the program**

   ```bash
   python ngofunding_fixed.py
   ```

---

## 📷 Example Visualizations
* Main Menu (Light/Dark Theme)
<p>
<img width="350" height="350" alt="image" src="https://github.com/user-attachments/assets/6b808312-5b0a-40fd-86e9-8db2ca856281 "style ="margin-right: 30px;" />   <img width="350" height="350" alt="Screenshot 2025-08-15 132413" src="https://github.com/user-attachments/assets/d3dc7f59-4084-46ff-96b0-9d5451259222" /> </p>

* Data Entry Form
  <p>
    <img width="249" height="300" alt="image" src="https://github.com/user-attachments/assets/a124a8c9-815a-44d0-ab87-f719d5b09829" />

  </p>
* Visualization Window showing:

  * Yearly Funding Comparison (Bar Chart)
  * Funding Source Distribution (Pie Chart)
  * Funding Trend Over Time (Line Chart)
  * Funding Amount Distribution (Histogram)

---

## 🛠 Future Improvements

* PDF report generation for yearly summaries
* Multi-condition search and filtering
* Cloud data sync for NGOs with multiple branches
* Role-based access for team members

---

## 📜 License

This project is licensed under the MIT License.

---

💡 *Developed by [Nikhil Kumar Singh](https://github.com/HMxNikhil)*

```

---

If you want, I can now **run your `ngofunding_fixed.py` with sample data**, generate the **real graphs**, and embed them into this README so your GitHub project looks professional.  

Do you want me to prepare that visual version?
```
