import tkinter as tk
from tkinter import ttk


class ListTasks:
    """Window for displaying all tracked tasks"""

    def __init__(self, main_root):
        self.main_root = main_root

        self.root = tk.Toplevel(main_root)
        self.root.title("Task Tracking")
        self.root.geometry("1000x600")
        self.root.resizable(False, False)

        self.root.transient(main_root)
        self.root.grab_set()

        self.colors = {
            'bg': '#0f172a',
            'card': '#1e293b',
            'primary': '#3b82f6',
            'secondary': '#8b5cf6',
            'text': '#f1f5f9',
            'button_text': '#0f172a',
            'text_secondary': '#94a3b8',
            'border': '#334155',
            'success': '#10b981',
            'danger': '#ef4444',
            'input_bg': '#2d3748',
            'input_border': '#4a5568',
            'hover': '#475569',
            'tabel': '#000000'
        }

        self.root.configure(bg=self.colors['bg'])
        self.setup_styles()
        self.center_window()
        self.create_window_style()

        self.load_demo_data()

    def setup_styles(self):
        """Setup styles for minimalist design"""
        style = ttk.Style()

        # Style for window title
        style.configure('WindowTitle.TLabel',
                        background=self.colors['card'],
                        foreground=self.colors['text'],
                        font=('Segoe UI', 24, 'bold'),
                        padding=10)

        # Style for section titles
        style.configure('Section.TLabel',
                        background=self.colors['card'],
                        foreground=self.colors['text'],
                        font=('Segoe UI', 14, 'bold'),
                        padding=5)

        # Style for normal text
        style.configure('Normal.TLabel',
                        background=self.colors['card'],
                        foreground=self.colors['text_secondary'],
                        font=('Segoe UI', 11),
                        padding=2)

        # Style for cards/frames
        style.configure('Card.TFrame',
                        background=self.colors['card'],
                        relief='flat',
                        borderwidth=0)

        # Style for primary buttons
        style.configure('Primary.TButton',
                        background=self.colors['primary'],
                        foreground=self.colors['button_text'],
                        borderwidth=0,
                        font=('Segoe UI', 12, 'bold'),
                        padding=10)
        style.map('Primary.TButton',
                  background=[('active', '#2563eb')])

        # Style for danger buttons
        style.configure('Danger.TButton',
                        background=self.colors['danger'],
                        foreground=self.colors['text'],
                        borderwidth=0,
                        font=('Segoe UI', 10, 'bold'),
                        padding=8)
        style.map('Danger.TButton',
                  background=[('active', '#dc2626')])

        # Style for success buttons
        style.configure('Success.TButton',
                        background=self.colors['success'],
                        foreground=self.colors['text'],
                        borderwidth=0,
                        font=('Segoe UI', 10, 'bold'),
                        padding=8)
        style.map('Success.TButton',
                  background=[('active', '#059669')])

        # Style for Treeview
        style.configure('Custom.Treeview',
                        background=self.colors['text'],
                        foreground=self.colors['tabel'],
                        fieldbackground=self.colors['text'],
                        borderwidth=0,
                        font=('Segoe UI', 10))

        style.configure('Custom.Treeview.Heading',
                        background=self.colors['input_bg'],
                        foreground=self.colors['tabel'],
                        relief='flat',
                        font=('Segoe UI', 11, 'bold'))

        style.map('Custom.Treeview.Heading',
                  background=[('active', self.colors['border'])])

    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def create_window_style(self):
        """Create the window layout for displaying tasks"""
        main_container = ttk.Frame(self.root, style='Card.TFrame')
        main_container.place(relx=0.5, rely=0.5, anchor='center', width=950, height=550)

        header_frame = ttk.Frame(main_container, style='Card.TFrame')
        header_frame.pack(fill='x', padx=30, pady=(25, 15))

        title_frame = ttk.Frame(header_frame, style='Card.TFrame')
        title_frame.pack(side='left', fill='y')

        title_label = ttk.Label(
            title_frame,
            text="Task Tracking",
            style='WindowTitle.TLabel'
        )
        title_label.pack(anchor='w')

        subtitle_label = ttk.Label(
            title_frame,
            text="View and manage your learning tasks",
            style='Normal.TLabel'
        )
        subtitle_label.pack(anchor='w', pady=(0, 5))

        separator = tk.Frame(main_container, bg=self.colors['border'], height=1)
        separator.pack(fill='x', padx=30, pady=(0, 15))

        toolbar_frame = ttk.Frame(main_container, style='Card.TFrame')
        toolbar_frame.pack(fill='x', padx=30, pady=(0, 15))

        table_frame = ttk.Frame(main_container, style='Card.TFrame')
        table_frame.pack(fill='both', expand=True, padx=30, pady=(0, 20))

        table_container = tk.Frame(table_frame, bg=self.colors['card'])
        table_container.pack(fill='both', expand=True)

        v_scrollbar = ttk.Scrollbar(table_container)
        v_scrollbar.pack(side='right', fill='y')

        h_scrollbar = ttk.Scrollbar(table_container, orient='horizontal')
        h_scrollbar.pack(side='bottom', fill='x')

        self.tasks_table = ttk.Treeview(
            table_container,
            style='Custom.Treeview',
            yscrollcommand=v_scrollbar.set,
            xscrollcommand=h_scrollbar.set,
            selectmode='extended',
            height=15
        )

        v_scrollbar.config(command=self.tasks_table.yview)
        h_scrollbar.config(command=self.tasks_table.xview)

        self.tasks_table['columns'] = ('ID', 'Task Name', 'Description', 'Created', 'Near repetition', 'Repeated')

        self.tasks_table.column('#0', width=0, stretch=False)
        self.tasks_table.column('ID', width=50, anchor='center')
        self.tasks_table.column('Task Name', width=200, anchor='w')
        self.tasks_table.column('Description', width=300, anchor='w')
        self.tasks_table.column('Created', width=100, anchor='center')
        self.tasks_table.column('Near repetition', width=120, anchor='center')
        self.tasks_table.column('Repeated', width=120, anchor='center')

        self.tasks_table.heading('#0', text='', anchor='w')
        self.tasks_table.heading('ID', text='ID', anchor='center')
        self.tasks_table.heading('Task Name', text='Task Name', anchor='w')
        self.tasks_table.heading('Description', text='Description', anchor='w')
        self.tasks_table.heading('Created', text='Created', anchor='center')
        self.tasks_table.heading('Near repetition', text='Near repetition', anchor='center')
        self.tasks_table.heading('Repeated', text='Repeated', anchor='center')

        self.tasks_table.pack(fill='both', expand=True)

        button_frame = ttk.Frame(main_container, style='Card.TFrame')
        button_frame.pack(fill='x', padx=30, pady=(0, 25))

    def load_demo_data(self):
        """Load demo tasks into the table"""
        item_id = self.tasks_table.insert(
            '',
            'end',
            values=(1, "Learn Python OOP", "Object-oriented programming concepts", "2024-01-15", "Tommorow", "2"),
        )

    def close_window(self):
        """Close the tasks window"""
        self.root.grab_release()
        self.root.destroy()
