import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import *
from tkinter import ttk, messagebox, simpledialog, filedialog
import os

# Theme configurations
THEMES = {
    "light": {
        "bg": "#f0f2f5",
        "fg": "#2c3e50",
        "accent": "#5c7cfa",
        "btn_bg": "#e9ecef",
        "btn_fg": "#2c3e50"
    },
    "dark": {
        "bg": "#1a1a1a",
        "fg": "#ecf0f1",
        "accent": "#3498db",
        "btn_bg": "#2c2c2c",
        "btn_fg": "#2c2c2c"
    }
}

current_theme = "light"
FUNDING_FILE = "ngo_funding.csv"
df = pd.DataFrame(columns=["Year", "Source", "Amount"]) if not os.path.exists(FUNDING_FILE) else pd.read_csv(FUNDING_FILE)

class HoverButton(ttk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_bg = self["style"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self["style"] = "Accent.TButton"

    def on_leave(self, e):
        self["style"] = "TButton"

def save_data():
    df.to_csv(FUNDING_FILE, index=False)

def apply_theme(theme_name):
    global current_theme
    current_theme = theme_name
    theme = THEMES[theme_name]
   
    root.configure(bg=theme["bg"])
    style = ttk.Style()
    style.configure("TButton",
                   background=theme["btn_bg"],
                   foreground=theme["btn_fg"],
                   font=("Segoe UI", 10),
                   borderwidth=0)
    style.configure("Accent.TButton",
                   background=theme["accent"],
                   foreground="white",
                   font=("Segoe UI", 10),
                   borderwidth=0)
    style.configure("TFrame", background=theme["bg"])
    style.configure("TLabel", background=theme["bg"], foreground=theme["fg"])
   
    for child in root.winfo_children():
        update_widget_colors(child, theme)

def update_widget_colors(widget, theme):
    if isinstance(widget, (Frame, Label)):
        widget.configure(bg=theme["bg"], fg=theme["fg"])
    for child in widget.winfo_children():
        update_widget_colors(child, theme)

def create_input_dialog(title, fields, callback):
    win = Toplevel(root)
    win.title(title)
    win.geometry("300x200")
    win.configure(bg=THEMES[current_theme]["bg"])
    win.resizable(False, False)
   
    entries = []
    for i, (label_text, default) in enumerate(fields.items()):
        Label(win, text=label_text,
             bg=THEMES[current_theme]["bg"],
             fg=THEMES[current_theme]["fg"]).grid(row=i, column=0, padx=10, pady=5)
        entry = ttk.Entry(win)
        entry.insert(0, default)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)
   
    btn_frame = ttk.Frame(win)
    btn_frame.grid(row=len(fields)+1, columnspan=2, pady=10)
   
    HoverButton(btn_frame, text="Submit", command=lambda: callback(win, entries)).pack(side=LEFT, padx=5)
    HoverButton(btn_frame, text="Cancel", command=win.destroy).pack(side=LEFT, padx=5)
   
    return win

def add_funding():
    def submit(win, entries):
        year = entries[0].get()
        source = entries[1].get()
        amount = entries[2].get()

        if not (year.isdigit() and amount.replace('.', '', 1).isdigit()):
            messagebox.showerror("Error", "Invalid numeric input")
            return

        global df
        df.loc[len(df)] = [int(year), source, float(amount)]
        save_data()
        messagebox.showinfo("Success", "Funding added successfully")
        win.destroy()

    create_input_dialog("Add New Funding",
                       {"Year": "", "Source": "", "Amount": ""},
                       submit)

def edit_funding():
    global df
    if df.empty:
        messagebox.showinfo("No Data", "No records to edit.")
        return

    try:
        index = simpledialog.askinteger("Edit Entry", "Enter index to edit (0-based):\n\nCurrent Data:\n" +
                                      df.to_string(max_rows=10))
        if index is None or index < 0 or index >= len(df):
            return
    except:
        messagebox.showerror("Error", "Invalid index")
        return

    def submit_edit(win, entries):
        year = entries[0].get()
        source = entries[1].get()
        amount = entries[2].get()

        if not (year.isdigit() and amount.replace('.', '', 1).isdigit()):
            messagebox.showerror("Error", "Invalid numeric input")
            return

        df.loc[index] = [int(year), source, float(amount)]
        save_data()
        messagebox.showinfo("Success", "Entry updated successfully")
        win.destroy()

    create_input_dialog("Edit Funding Entry",
                       {"Year": df.loc[index, 'Year'],
                        "Source": df.loc[index, 'Source'],
                        "Amount": df.loc[index, 'Amount']},
                       submit_edit)

def delete_funding():
    global df
    if df.empty:
        messagebox.showinfo("Info", "No data to delete.")
        return

    try:
        index = simpledialog.askinteger("Delete Entry", "Enter index to delete (0-based):\n\nCurrent Data:\n" +
                                      df.to_string(max_rows=10))
        if index is None or index < 0 or index >= len(df):
            return
    except:
        messagebox.showerror("Error", "Invalid index")
        return

    confirm = messagebox.askyesno("Confirm", f"Delete this entry?\n\n{df.loc[index].to_string()}")
    if confirm:
        df.drop(index=index, inplace=True)
        df.reset_index(drop=True, inplace=True)
        save_data()
        messagebox.showinfo("Success", "Entry deleted successfully")

def search_funding():
    query = simpledialog.askstring("Search", "Enter Year or Source to search:")
    if not query:
        return

    results = df[(df["Year"].astype(str).str.contains(query)) | (df["Source"].str.contains(query, case=False))]
    if results.empty:
        messagebox.showinfo("No Results", "No matching entries found.")
    else:
        messagebox.showinfo("Search Results", results.to_string(index=True))

def sort_funding():
    choice = simpledialog.askstring("Sort", "Sort by 'Year' or 'Amount'?")
    if choice not in ["Year", "Amount"]:
        messagebox.showerror("Error", "Invalid sort field")
        return
   
    sorted_df = df.sort_values(by=choice)
    messagebox.showinfo(f"Sorted by {choice}", sorted_df.to_string(index=True))

def show_statistics():
    if df.empty:
        messagebox.showinfo("No Data", "No records to analyze.")
        return

    stats = df["Amount"].describe()
    messagebox.showinfo("Statistics",
                      f"📊 Funding Statistics\n\n{stats.to_string()}")

def export_to_excel():
    if df.empty:
        messagebox.showinfo("No Data", "No data available to export.")
        return

    try:
        df.to_excel("ngo_funding_export.xlsx", index=False)
        messagebox.showinfo("Success", "Data exported to 'ngo_funding_export.xlsx'")
    except Exception as e:
        messagebox.showerror("Error", f"Export failed: {str(e)}")

def visualize_data():
    if df.empty:
        messagebox.showinfo("No Data", "No data to visualize.")
        return

    # Use a valid style
    plt.style.use('dark_background' if current_theme == 'dark' else 'seaborn-v0_8')

    fig = plt.figure(figsize=(18, 10))

    # Plot 1: Yearly Funding
    ax1 = fig.add_subplot(2, 2, 1)
    sns.barplot(x=df["Year"], y=df["Amount"], ax=ax1)
    ax1.set_title("Yearly Funding Comparison")

    # Plot 2: Funding Sources
    ax2 = fig.add_subplot(2, 2, 2)
    df.groupby("Source")["Amount"].sum().plot.pie(autopct='%1.1f%%', ax=ax2)
    ax2.set_ylabel("")  # Remove y-label for pie chart
    ax2.set_title("Funding Source Distribution")

    # Plot 3: Funding Trend
    ax3 = fig.add_subplot(2, 2, 3)
    df.groupby("Year")["Amount"].sum().plot(marker='o', ax=ax3)
    ax3.set_title("Funding Trend Over Time")

    # Plot 4: Amount Distribution
    ax4 = fig.add_subplot(2, 2, 4)
    sns.histplot(df["Amount"], kde=True, ax=ax4)
    ax4.set_title("Funding Amount Distribution")

    plt.tight_layout()
    plt.show()

def create_settings_menu(parent):
    def show_settings_dropdown():
        menu = Menu(parent, tearoff=0,
                   bg=THEMES[current_theme]["bg"],
                   fg=THEMES[current_theme]["fg"])
       
        menu.add_command(label="Toggle Theme",
                        command=lambda: apply_theme("dark" if current_theme == "light" else "light"))
        menu.add_command(label="Backup Data", command=backup_data)
        menu.add_command(label="App Info", command=show_app_info)
        menu.post(parent.winfo_rootx(), parent.winfo_rooty() + 40)
   
    settings_btn = HoverButton(parent, text="⚙", command=show_settings_dropdown)
    settings_btn.pack(side=RIGHT, padx=20)

def backup_data():
    try:
        timestamp = pd.Timestamp.now().strftime("%Y%m%d_%H%M%S")
        backup_file = f"backup_{timestamp}.csv"
        df.to_csv(backup_file, index=False)
        messagebox.showinfo("Backup Successful", f"Data backed up to {backup_file}")
    except Exception as e:
        messagebox.showerror("Backup Failed", str(e))

def show_app_info():
    info = """
    NGO Funding Manager v2.0
   
    Features:
    - Funding data management
    - Data visualization
    - Dark/Light themes
    - Data backup
    - Excel export
   
    Developed by [Your Name]
    """
    messagebox.showinfo("App Information", info)

def main_menu_gui():
    global root
    root = Tk()
    root.title("NGO Funding Manager")
    root.geometry("800x600")
   
    # Header
    header_frame = ttk.Frame(root)
    header_frame.pack(fill=X, pady=10)
   
    ttk.Label(header_frame, text="📊 NGO Funding Manager",
             font=("Segoe UI", 20, "bold")).pack(side=LEFT, padx=20)
   
    create_settings_menu(header_frame)
   
    # Main buttons
    btn_container = ttk.Frame(root)
    btn_container.pack(pady=20, padx=40, fill=BOTH, expand=True)
   
    buttons = [
        ("➕ Add Funding Data", add_funding),
        ("📝 Edit Funding Data", edit_funding),
        ("❌ Delete Funding Data", delete_funding),
        ("🔍 Search Funding Data", search_funding),
        ("↕️ Sort Funding Data", sort_funding),
        ("📈 Visualize Data", visualize_data),
        ("📊 Show Statistics", show_statistics),
        ("📤 Export to Excel", export_to_excel),
        ("🚪 Exit", root.destroy)
    ]
   
    for text, cmd in buttons:
        btn = HoverButton(btn_container, text=text, command=cmd)
        btn.pack(fill=X, pady=4, ipady=8)
   
    apply_theme(current_theme)
    root.mainloop()

if __name__ == "__main__":
    main_menu_gui()
