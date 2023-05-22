[ -f "$HOME/.local/share/zap/zap.zsh" ] && source "$HOME/.local/share/zap/zap.zsh"

# Example install plugins
plug "zap-zsh/supercharge"
plug "zsh-users/zsh-autosuggestions"
plug "zsh-users/zsh-syntax-highlighting"
plug "zap-zsh/zap-prompt"
plug "jeffreytse/zsh-vi-mode"

export PATH=$HOME/.local/bin:$HOME/.cargo/bin:$PATH
export PATH=/var/lib/snapd/snap/bin:$HOME/snap/bin:$PATH
export PATH=$HOME/.config/alacritty/alacritty.yml:$HOME/snap/bin:$PATH
export PATH=$PATH:/usr/local/go/bin
export PATH="$HOME/.asdf/bin:$HOME/.asdf/shims:$PATH"


alias cls="clear"
alias qt="vim ~/.config/qtile/config.py"
alias vim="nvim"
alias tmz="~/tmux-session-manager"

setopt NO_NOMATCH


