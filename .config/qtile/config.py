from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
# terminal = guess_terminal()

#COLORS

colors = [["#282c34", "#282c34"], # panel background
          ["#434758", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#8d62a9", "#8d62a9"], # border line color for other tab and odd widgets
          ["#668bd7", "#668bd7"], # color for the even widgets
          ["#e1acff", "#e1acff"]] # window name

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "12345678"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Max(),
    layout.Stack(num_stacks=2, margin=8, border_focus='#00ff00'),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=5,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 9,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[2],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[3],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[0],
                       other_screen_border = colors[0],
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 40,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.WindowName(
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " 🌡",
                       padding = 2,
                       foreground = colors[2],
                       background = colors[5],
                       fontsize = 11
                       ),
              widget.ThermalSensor(
                       foreground = colors[2],
                       background = colors[5],
                       threshold = 90,
                       padding = 5
                       ),
              widget.TextBox(
                       text='',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " ⟳",
                       padding = 2,
                       foreground = colors[2],
                       background = colors[4],
                       fontsize = 14
                       ),
              widget.Pacman(
                       update_interval = 1800,
                       foreground = colors[2],
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('alacritty -e sudo pacman -Syu')},
                       background = colors[4]
                       ),
              widget.TextBox(
                       text = "Updates",
                       padding = 5,
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('alacritty -e sudo pacman -Syu')},
                       foreground = colors[2],
                       background = colors[4]
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " 🖬",
                       foreground = colors[2],
                       background = colors[5],
                       padding = 0,
                       fontsize = 14
                       ),
              widget.Memory(
                       foreground = colors[2],
                       background = colors[5],
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('alacritty -e htop')},
                       padding = 5
                       ),
              widget.TextBox(
                       text='',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Net(
                       interface = "wlp2s0",
                       format = '{down} ↓↑ {up}',
                       foreground = colors[2],
                       background = colors[4],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                      text = " Vol:",
                       foreground = colors[2],
                       background = colors[5],
                       padding = 0
                       ),
              widget.Volume(
                       foreground = colors[2],
                       background = colors[5],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.CurrentLayout(
                       foreground = colors[2],
                       background = colors[4],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Clock(
                       foreground = colors[2],
                       background = colors[5],
                       format = "%A, %B %d  [ %H:%M ]"
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 10,
                       foreground = colors[0],
                       background = colors[5]
                       ),
              widget.Systray(
                       background = colors[0],
                       padding = 5
                       ),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
