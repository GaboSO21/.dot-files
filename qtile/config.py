# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.layout.floating import Floating

mod = "mod1"
terminal = 'kitty'
rofi = "./.config/rofi/scripts/launcher_t7"
brave = 'brave-nightly'
brave_git = 'brave-nightly "github.com/GaboSO21"'
brave_teams = 'brave-nightly "teams.microsoft.com"'
scrot = "scrot -s '/home/gabo-arch/Pictures/screenshots/%F_%T_$wx$h.png' -e 'xclip -selection clipboard -target image/png -i $f'"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    # Toggle floating and tiling
    Key([mod], "space", lazy.window.toggle_floating()),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "d", lazy.spawn(rofi), desc="Launch rofi"),
    Key([mod], "b", lazy.spawn(brave), desc="Launch brave browser"),
    Key([mod], "g", lazy.spawn(brave_git), desc="Launch brave browser on github"),
    Key([mod], "t", lazy.spawn(brave_teams), desc="Launch brave browser on teams"),
    # Screenshoj
    Key([mod, "shift"], "s", lazy.spawn(scrot), desc="Take screenshot"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    # Key([mod, "control"], "h", lazy.hide_show_bar(), desc="Hide bar"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

groups = [Group(i) for i in ['','','','󰙯','','','󰍳','󰶈','󰑴']]
group_hotkeys = '123456789'

for i, y in zip(groups, group_hotkeys):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                y,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                y,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
            Key(
                [mod, "shift"], "Return", lazy.group["scratchpad"].dropdown_toggle("term")
            ),
        ]
    )

# Append ScratchPad to groups list
groups.append(
    ScratchPad("scratchpad", [
        # define a drop down temrinal.
        DropDown("term", terminal, opacity=0.9, height=0.5, width=0.8, x=0.1, y=0.2),
    ]),
)

# Colors
gruvbox_material = {
    'bg': '#282828',
    'bg0_h': '#1d2021',
    'bg_1': '#3c3836',
    'bg_2': '#504945',
    'bg_3': '#665c54',
    'bg_4': '#7c6f64',
    'red': '#cc241d',
    'red_2': '#fb4934',
    'green': '#98971a',
    'green_2': '#b8bb26',
    'yellow': '#d79921',
    'yellow_2': '#fabd2f',
    'orange': '#d65d0e',
    'orange_2': '#fe8019',
    'blue': '#458588',
    'blue_2': '#83a598',
    'purple': '#b16286',
    'purple_2': '#d3869b',
    'aqua': '#689d6a',
    'aqua_2': '#8ec07c',
    'gray': '#a89984',
    'gray_2': '#928374',
    'gray_3': '#a89984',
    'fg_0': '#fbf1c7',
    'fg_1': '#ebdbb2',
    'fg_2': '#d5c4a1',
    'fg_3': '#bdae93',
    'fg_4': '#a89984',
}

fuji = {
    'A': '#304D57',
    'B': '#16252E',
    'C': '#F6f6E6',
    'D': '#E3E3C6',
    'E': '#E0C77A',
    'F': '#C0A05B',
    'H': '#5A7E7A',
    'I': '#8DAC97',
    'J': '#716C4B',
    'K': '#C6C9A8'
}

layouts = [
    layout.MonadTall(
        margin=10,
        border_width=1,
        border_focus=gruvbox_material['bg_3'],
        border_normal=gruvbox_material['bg']
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # Floating(
    #     border_width=1,
    #     border_focus=gruvbox_material['yellow'],
    #     border_normal=gruvbox_material['bg_1']
    # ),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(
        sections = ['Windows'],
        active_bg = fuji['I'],
        bg_color = "#00000000",
        font = "SF Pro Text Regular",
        fontsize = 13,
        section_top = 30,
    ),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="SF Pro Text Regular",
    fontsize=13,
    padding=3,
    foreground=fuji['C'] 
)
extension_defaults = widget_defaults.copy()

def get_widgets(primary=False):
    widgets = [
        widget.Spacer(
            length=3,
            background='#00000000',
            ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=gruvbox_material['bg'],
            background='#00000000',
            ),
        widget.GroupBox(
            highlight_method="text",
            active=gruvbox_material["fg_4"],
            this_current_screen_border=gruvbox_material['purple_2'],
            foreground=gruvbox_material["orange"],
            highlight_color=gruvbox_material["orange"],
            inactive=fuji['J'],
            background=gruvbox_material['bg']
            ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=gruvbox_material['bg'],
            background='#00000000',
            ),
        widget.WindowName(
            fontsize=12,
            foreground=gruvbox_material['fg_2']
            ),
        widget.Spacer(
            length=10,
            background='#00000000',
            ),
        widget.PulseVolume(
            fmt="墳 {}",
            foreground=gruvbox_material['fg_2'],
            background='#00000000',
            ),
        widget.Spacer(
            length=10,
            background='#00000000',
            ),
        widget.Spacer(
            length=10,
            background='#00000000',
            ),
        widget.CPU(
            format=" {load_percent:04}%",
            foreground=gruvbox_material['fg_2'],
            background='#00000000',
            ),
        widget.TextBox(
            text="-",
            padding=0,
            fontsize=15,
            foreground=gruvbox_material['fg_2'],
            background='#00000000',
            ),
        widget.ThermalSensor(
            foreground=gruvbox_material['fg_2'],
            background='#00000000',
            ),
        widget.Spacer(
            length=10,
            background='#00000000',
            ),
        widget.Memory(
            format="󰍛 {MemUsed:.0f}M/{MemTotal:.0f}M",
            foreground=gruvbox_material['fg_2'],
            background='#00000000',
            ),
        widget.Spacer(
            length=10,
            background='#00000000',
            ),
        widget.Spacer(
            length=10,
            background='#00000000',
            ),
        widget.Clock(
            format=" %I:%M %p",
            foreground=gruvbox_material['fg_2'],
            background='#00000000',
            ),
        widget.Spacer(
            length=10,
            background='#00000000',
            ),
            ]
    if primary:
        widgets.insert(10, widget.Systray())
    else: 
        rm_widgets = (15,14,13,12,11,10,9,8,7,6)
        for i in rm_widgets:
            widgets.pop(i)

    return widgets

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

screens = [
    Screen(
        wallpaper='/home/gabo-arch/Pictures/wallpaper.png',
        wallpaper_mode='stretch',
        top=bar.Bar(
            get_widgets(primary=True),
            20,
            background='#00000000', opacity = 1
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
    # Screen(
    #     wallpaper='/home/gabo-arch/Pictures/wave3.jpg',
    #     wallpaper_mode='fill',
    #     top=bar.Bar(
    #         get_widgets(),
    #         20,
    #         background='#00000000', opacity = 1
    #         # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
    #         # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
    #     ),
    # ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=gruvbox_material['fg_0'],
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
