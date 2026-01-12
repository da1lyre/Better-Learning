import tkinter as tk
from tkinter import ttk, messagebox


class Task:
    """Task class for adding new learning tasks"""
    def __init__(self, main_root):
        self.task_name = tk.StringVar()
        self.task_description = tk.StringVar()
        self.main_root = main_root

        self.root = tk.Toplevel(main_root)
        self.root.title("Adding new task")
        self.root.geometry("900x500")
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
            'input_focus': '#3b82f6'
        }

        self.root.configure(bg=self.colors['bg'])
        self.setup_styles()
        self.center_window()
        self.create_window_style()

        self.root.bind('<Return>', lambda e: self.add_to_tracking())

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
                        padding=12)
        style.map('Primary.TButton',
                  background=[('active', '#2563eb')])

        # Style for secondary buttons
        style.configure('Secondary.TButton',
                        background=self.colors['secondary'],
                        foreground=self.colors['text'],
                        borderwidth=0,
                        font=('Segoe UI', 12, 'bold'),
                        padding=12)
        style.map('Secondary.TButton',
                  background=[('active', '#7c3aed')])

        # Style for text input
        style.configure('Input.TEntry',
                        fieldbackground=self.colors['input_bg'],
                        foreground=self.colors['text'],
                        borderwidth=1,
                        relief='flat',
                        padding=10,
                        insertcolor=self.colors['text'])
        style.map('Input.TEntry',
                  fieldbackground=[('focus', '#374151')],
                  bordercolor=[('focus', self.colors['primary'])])

    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def create_window_style(self):
        """Create the window layout with input fields"""
        main_container = ttk.Frame(self.root, style='Card.TFrame')
        main_container.place(relx=0.5, rely=0.5, anchor='center', width=850, height=450)

        title_frame = ttk.Frame(main_container, style='Card.TFrame')
        title_frame.pack(fill='x', padx=40, pady=(30, 20))

        title_label = ttk.Label(
            title_frame,
            text="Add New Task",
            style='WindowTitle.TLabel'
        )
        title_label.pack()

        subtitle_label = ttk.Label(
            title_frame,
            text="Fill in the details below to create a new learning task",
            style='Normal.TLabel'
        )
        subtitle_label.pack()

        separator = tk.Frame(main_container, bg=self.colors['border'], height=1)
        separator.pack(fill='x', padx=40, pady=10)

        form_frame = ttk.Frame(main_container, style='Card.TFrame')
        form_frame.pack(fill='both', expand=True, padx=40, pady=20)

        name_frame = ttk.Frame(form_frame, style='Card.TFrame')
        name_frame.pack(fill='x', pady=(0, 20))

        name_label = ttk.Label(
            name_frame,
            text="Task Name *",
            style='Section.TLabel'
        )
        name_label.pack(anchor='w', pady=(0, 8))

        name_entry_container = tk.Frame(name_frame, bg=self.colors['input_bg'], bd=1, relief='flat')
        name_entry_container.pack(fill='x', pady=(0, 5))

        self.name_entry = tk.Entry(
            name_entry_container,
            bg=self.colors['input_bg'],
            fg=self.colors['text'],
            insertbackground=self.colors['text'],
            font=('Segoe UI', 11),
            relief='flat',
            textvariable=self.task_name
        )
        self.name_entry.pack(fill='both', padx=10, pady=12, ipady=2)

        self.name_entry.bind('<FocusIn>', lambda e: name_entry_container.configure(bg=self.colors['input_focus']))
        self.name_entry.bind('<FocusOut>', lambda e: name_entry_container.configure(bg=self.colors['input_bg']))

        self.name_entry.insert(0, "Enter task name...")
        self.name_entry.bind('<FocusIn>', lambda e: self.clear_placeholder(self.name_entry, "Enter task name..."))
        self.name_entry.bind('<FocusOut>', lambda e: self.add_placeholder(self.name_entry, "Enter task name..."))

        desc_frame = ttk.Frame(form_frame, style='Card.TFrame')
        desc_frame.pack(fill='both', expand=True, pady=(0, 20))

        desc_label = ttk.Label(
            desc_frame,
            text="Task Description",
            style='Section.TLabel'
        )
        desc_label.pack(anchor='w', pady=(0, 8))

        desc_container = tk.Frame(desc_frame, bg=self.colors['input_bg'], bd=1, relief='flat')
        desc_container.pack(fill='both', expand=True)

        self.desc_text = tk.Text(
            desc_container,
            bg=self.colors['input_bg'],
            fg=self.colors['text'],
            insertbackground=self.colors['text'],
            font=('Segoe UI', 11),
            relief='flat',
            height=8,
            wrap='word',
            padx=10,
            pady=10
        )
        self.desc_text.pack(side='left', fill='both', expand=True)

        self.desc_text.insert('1.0', "Enter task description...")
        self.desc_text.bind('<FocusIn>',
                            lambda e: self.clear_text_placeholder(self.desc_text, "Enter task description..."))
        self.desc_text.bind('<FocusOut>',
                            lambda e: self.add_text_placeholder(self.desc_text, "Enter task description..."))

    def clear_placeholder(self, entry, placeholder):
        """Clear placeholder text on focus"""
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.configure(fg=self.colors['text'])

    def add_placeholder(self, entry, placeholder):
        """Add placeholder text if field is empty"""
        if not entry.get().strip():
            entry.insert(0, placeholder)
            entry.configure(fg=self.colors['text_secondary'])

    def clear_text_placeholder(self, text_widget, placeholder):
        """Clear placeholder from Text widget"""
        if text_widget.get('1.0', 'end-1c') == placeholder:
            text_widget.delete('1.0', tk.END)
            text_widget.configure(fg=self.colors['text'])

    def add_text_placeholder(self, text_widget, placeholder):
        """Add placeholder to Text widget"""
        if not text_widget.get('1.0', 'end-1c').strip():
            text_widget.insert('1.0', placeholder)
            text_widget.configure(fg=self.colors['text_secondary'])

    def add_to_tracking(self):
        """Add task to tracking system"""

        messagebox.showinfo("Success", f"Task '{1}' added to tracking!")
        self.close_window()

    def close_window(self):
        """Close the task window"""
        self.root.destroy()
