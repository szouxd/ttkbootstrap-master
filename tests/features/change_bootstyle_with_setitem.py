import tkinter as tk
import ttkbootstrap as ttk

"""
    Test that Widget['bootstyle'] = value is able to change the widget
"""

root = tk.Tk()
style = ttk.Style()
colors = style.theme.colors

btn = ttk.Button(root, text="Push Button", bootstyle='outline-danger')
btn.pack(padx=10, pady=10)

# initial style
ttkstyle = btn.cget('style')
assert ttkstyle == 'danger.Outline.TButton'

# intial bordercolor
bordercolor = style.lookup(ttkstyle, 'bordercolor')
assert bordercolor == colors.danger

# change the style with `configure`
btn['bootstyle'] = 'link-success'

# new style
ttkstyle = btn.cget('style')
assert ttkstyle == 'success.Link.TButton'

# foreground color
foreground = style.lookup(ttkstyle, 'foreground')
assert foreground == colors.success
