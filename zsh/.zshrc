[ -f "$HOME/.local/share/zap/zap.zsh" ] && source "$HOME/.local/share/zap/zap.zsh"

# Example install plugins
plug "zap-zsh/supercharge"
plug "zsh-users/zsh-autosuggestions"
plug "zsh-users/zsh-syntax-highlighting"

# Example theme
plug "zap-zsh/zap-prompt"
plug "jeffreytse/zsh-vi-mode"

export PATH=$HOME/.local/bin:$HOME/.cargo/bin:$PATH
export PATH=/var/lib/snapd/snap/bin:$HOME/snap/bin:$PATH
export PATH=$HOME/.config/alacritty/alacritty.yml:$HOME/snap/bin:$PATH
export PATH=$PATH:/usr/local/go/bin


alias la="ls -la"
alias cls="clear"
alias alac="vim ~/.config/alacritty.yml"
alias zshrc="vim ~/dotfiles/zsh/.zshrc"
alias vimrc="vim ~/dotfiles/vim/.config/nvim/"
alias qt="vim ~/.config/qtile/config.py"
alias sozsh="source ~/.zshrc"
alias vim="nvim"
# alias _cat="cat"
# alias cat="bat"
# alias ls="exa --icons"
# alias top="ytop"



export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
