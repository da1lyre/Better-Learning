import tkinter as tk
from tkinter import ttk, messagebox


class MainWindow:
    def __init__(self, window):
        self.root = window
        self.root.title("Better Learning")
        self.root.geometry("900x500")
        self.root.resizable(False, False)

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
            'danger': '#ef4444'
        }

        self.root.configure(bg=self.colors['bg'])
        self.setup_styles()
        self.center_window()
        self.create_layout()

    def setup_styles(self):
        """Setup styles for minimalist design"""
        style = ttk.Style()

        # Style for titles
        style.configure('Title.TLabel',
                        background=self.colors['bg'],
                        foreground=self.colors['text'],
                        font=('Inter', 32, 'bold'),
                        padding=10)

        # Style for subtitles
        style.configure('Subtitle.TLabel',
                        background=self.colors['bg'],
                        foreground=self.colors['text_secondary'],
                        font=('Inter', 14),
                        padding=5)

        # Style for cards
        style.configure('Card.TFrame',
                        background=self.colors['card'],
                        relief='flat',
                        borderwidth=0)

        # Style for action buttons
        style.configure('Action.TButton',
                        background=self.colors['primary'],
                        foreground=self.colors['button_text'],
                        borderwidth=0,
                        font=('Inter', 12, 'bold'),
                        padding=15)
        style.map('Action.TButton',
                  background=[('active', '#2563eb')])


    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def create_layout(self):
        """Create the main layout"""
        main_container = ttk.Frame(self.root, style='Card.TFrame')
        main_container.place(relx=0.5, rely=0.5, anchor='center', width=800, height=400)

        left_panel = ttk.Frame(main_container, style='Card.TFrame')
        left_panel.pack(side='left', fill='both', expand=True, padx=40, pady=40)

        right_panel = ttk.Frame(main_container, style='Card.TFrame')
        right_panel.pack(side='right', fill='both', expand=True, padx=40, pady=40)

        separator = tk.Frame(main_container, bg=self.colors['border'], width=1)
        separator.pack(side='left', fill='y', padx=20)

        self.create_info_panel(left_panel)
        self.create_actions_panel(right_panel)

    def create_info_panel(self, parent):
        """Create information panel"""
        icon_label = tk.Label(
            parent,
            text="🎯",
            font=('Segoe UI Emoji', 64),
            bg=self.colors['card'],
            fg=self.colors['primary']
        )
        icon_label.pack(pady=(0, 20))

        title_label = ttk.Label(
            parent,
            text="Better Learning",
            style='Title.TLabel'
        )
        title_label.pack(pady=10)

        subtitle_label = ttk.Label(
            parent,
            text="Repeat your studied lessons \nthrough automative system notifications.",
            style='Subtitle.TLabel',
            anchor="center",
            justify="center"
        )
        subtitle_label.pack(pady=5)

    def create_actions_panel(self, parent):
        """Create actions panel"""
        actions_title = tk.Label(
            parent,
            text="Actions",
            font=('Inter', 18, 'bold'),
            bg=self.colors['card'],
            fg=self.colors['text']
        )
        actions_title.pack(pady=(0, 30))

        buttons_frame = ttk.Frame(parent, style='Card.TFrame')
        buttons_frame.pack(fill='both', expand=True)

        # First button - Add Task
        add_task_btn = ttk.Button(
            buttons_frame,
            text="Add new task",
            style='Action.TButton',
            command=self.add_task,
            cursor='hand2'
        )
        add_task_btn.pack(fill='x', pady=10, ipady=10)

        # Second button - Show Tasks
        show_tasks_btn = ttk.Button(
            buttons_frame,
            text="View tracking",
            style='Action.TButton',
            command=self.show_tasks,
            cursor='hand2'
        )
        show_tasks_btn.pack(fill='x', pady=10, ipady=10)

    def add_task(self):
        """Add task"""

    def show_tasks(self):
        """Show tasks"""

