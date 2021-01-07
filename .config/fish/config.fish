set TERM "xterm-256color"             
set EDITOR "micro"
set VISUAL "kate"
set fish_greeting

## Run neofetch if session is interactive
if status --is-interactive
   neofetch
end


for f in (ls ~/.config/fish/functions/)
  source $HOME/.config/fish/functions/$f
end

## Custom settings
starship init fish | source
source $HOME/.config/fish/aliases.fish

set -x MANPAGER "sh -c 'col -bx | bat -l man -p'"

