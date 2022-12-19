import os
import subprocess

from libqtile import qtile
from libqtile import layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile import hook
from libqtile.widget.textbox import TextBox
from libqtile.bar import Bar
from libqtile.widget.clock import Clock
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.spacer import Spacer
from libqtile.widget.systray import Systray
from libqtile.widget.windowname import WindowName
from libqtile.widget.volume import Volume
from libqtile.widget.memory import Memory
from libqtile.widget.battery import Battery
from libqtile.widget.cpu import CPU

mod = "mod4"
terminal = "alacritty"
browser = "brave"
gruvbox = {
    "bg": "#282828",
    "fg": "#d4be98",
    "dark-red": "#ea6962",
    "red": "#ea6962",
    "dark-green": "#a9b665",
    "green": "#a9b665",
    "dark-yellow": "#e78a4e",
    "yellow": "#d8a657",
    "dark-blue": "#7daea3",
    "blue": "#7daea3",
    "dark-magenta": "#d3869b",
    "magenta": "#d3869b",
    "dark-cyan": "#89b482",
    "cyan": "#89b482",
    "dark-gray": "#665c54",
    "gray": "#928374",
    "white": "#ffffff",
    "fg4": "#766f64",
    "fg3": "#665c54",
    "fg2": "#504945",
    "fg1": "#3c3836",
    "bg0": "#32302f",
    "fg0": "#1d2021",
    "fg9": "#ebdbb2",
}

SOUND_VOLUME_TOGGLE_MUTE = "pactl set-sink-mute @DEFAULT_SINK@ toggle"
SOUND_VOLUME_DOWN = "amixer sset Master 5%-"
SOUND_VOLUME_UP = "amixer sset Master 5%+"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="toggle fullscreen"),
    Key([mod], "period", lazy.next_screen(), desc="Next monitor"),
    Key([mod], "comma", lazy.prev_screen(), desc="Next monitor"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(
        [mod],
        "r",
        lazy.spawn("rofi -show drun"),
        desc="Spawn a command using a prompt widget",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "d", lazy.spawn("nautilus"), desc="Launch file manager"),
    KeyChord(
        [mod],
        "w",
        [
            Key([], "b", lazy.spawn(browser), desc="Launch Brave"),
            Key([], "f", lazy.spawn("firefox"), desc="Launch Brave"),
            Key([], "g", lazy.spawn("google-chrome"), desc="Launch google-chrome"),
        ],
    ),
    # Sound and Mpd
    Key([], "XF86AudioRaiseVolume", lazy.spawn(SOUND_VOLUME_UP)),
    Key([], "XF86AudioLowerVolume", lazy.spawn(SOUND_VOLUME_DOWN)),
    Key([], "XF86AudioMute", lazy.spawn(SOUND_VOLUME_TOGGLE_MUTE)),
    # Utilites
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": "DC5F00",
    "border_normal": "000000",
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

groupbox = GroupBox(
    disable_drag=True,
    fontsize=19,
    margin_y=3,
    margin_x=0,
    padding_y=5,
    padding_x=3,
    borderwidth=3,
    highlight_method="line",
    highlight_color=gruvbox["bg0"],
    this_current_screen_border=gruvbox["red"],
    this_screen_border=gruvbox["red"],
    other_current_screen_border=gruvbox["red"],
    active=gruvbox["red"],
    inactive=gruvbox["dark-gray"],
    block_highlight_text_color=gruvbox["red"],
    background=gruvbox["bg"],
)
spacer = Spacer(length=20, background=gruvbox["bg0"])

screens = [
    Screen(
        top=Bar(
            [
                groupbox,
                spacer,
                WindowName(foreground=gruvbox["fg"]),
                Spacer(length=10, background=gruvbox["yellow"]),
                TextBox(
                    text="",
                    fontsize=22,
                    background=gruvbox["yellow"],
                    foreground=gruvbox["white"],
                    padding=0,
                ),
                CPU(background=gruvbox["yellow"], format='{load_percent}%'),
                Spacer(length=10, background=gruvbox["yellow"]),
                Spacer(length=10, background=gruvbox["green"]),
                TextBox(
                    text="",
                    fontsize=22,
                    background=gruvbox["green"],
                    foreground=gruvbox["white"],
                    padding=0,
                ),
                Battery(background=gruvbox["green"]),
                Spacer(length=10, background=gruvbox["green"]),
                Spacer(length=10, background=gruvbox["red"]),
                TextBox(
                    text="",
                    fontsize=22,
                    background=gruvbox["red"],
                    foreground=gruvbox["white"],
                    padding=0,
                ),
                Memory(measure_mem="G", background=gruvbox["red"]),
                Spacer(length=10, background=gruvbox["red"]),
                Spacer(length=15, background=gruvbox["dark-blue"]),
                TextBox(
                    text="墳",
                    fontsize=22,
                    background=gruvbox["dark-blue"],
                    foreground=gruvbox["white"],
                    padding=0,
                ),
                Volume(
                    volume_down_command=SOUND_VOLUME_DOWN,
                    volume_up_command=SOUND_VOLUME_UP,
                    mute_command=SOUND_VOLUME_TOGGLE_MUTE,
                    background=gruvbox["dark-blue"],
                ),
                Spacer(length=15, background=gruvbox["dark-blue"]),
                spacer,
                TextBox(
                    text="",
                    fontsize=22,
                    background=gruvbox["bg"],
                    foreground=gruvbox["white"],
                    padding=0,
                ),
                Clock(
                    padding=8,
                    background=gruvbox["bg"],
                    foreground=gruvbox["white"],
                    format="%d/%m/%Y %H:%M",
                ),
                spacer,
                Spacer(length=10, background=gruvbox["bg"]),
                Systray(background=gruvbox["bg"], padding=5),
                Spacer(length=15, background=gruvbox["bg"]),
                spacer,
                TextBox(
                    text=" ",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn("gnome-control-center")
                    },
                    fontsize=18,
                    background=gruvbox["bg0"],
                    foreground=gruvbox["yellow"],
                    padding=0,
                ),
                spacer,
                TextBox(
                    text="",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn("shutdown now")
                    },
                    fontsize=22,
                    background=gruvbox["bg0"],
                    foreground=gruvbox["red"],
                    padding=0,
                ),
                spacer,
            ],
            background=gruvbox["bg"],
            size=26,
        )
    ),
    Screen(
        top=Bar(
            [
                groupbox,
                spacer,
                WindowName(foreground=gruvbox["fg"]),
                Clock(
                    padding=8,
                    background=gruvbox["bg0"],
                    foreground=gruvbox["white"],
                    format=" %d/%m/%Y %H:%M",
                ),
                spacer,
                Spacer(length=15, background=gruvbox["dark-blue"]),
                TextBox(
                    text="墳",
                    fontsize=22,
                    background=gruvbox["dark-blue"],
                    foreground=gruvbox["white"],
                    padding=0,
                ),
                Volume(
                    volume_down_command=SOUND_VOLUME_DOWN,
                    volume_up_command=SOUND_VOLUME_UP,
                    mute_command=SOUND_VOLUME_TOGGLE_MUTE,
                    background=gruvbox["dark-blue"],
                ),
                Spacer(length=15, background=gruvbox["dark-blue"]),
            ],
            background=gruvbox["bg"],
            size=26,
        )
    ),
]

mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
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


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([home])


auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
