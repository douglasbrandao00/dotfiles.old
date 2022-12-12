# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

autoload -Uz vcs_info
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="powerlevel10k/powerlevel10k"

HYPHEN_INSENSITIVE="true"
ENABLE_CORRECTION="false"
COMPLETION_WAITING_DOTS="true"
HIST_STAMPS="dd/mm/yyyy"

zstyle ':omz:update' mode auto      # update automatically without asking
zstyle ':omz:update' frequency 2

source $ZSH/oh-my-zsh.sh

#source /opt/asdf-vm/asdf.sh
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
alias _cat="cat"
alias cat="bat"
alias ls="exa --icons"
alias top="ytop"
#alias tab="/usr/bin/setxkbmap -option 'caps:swapescape'"



export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
