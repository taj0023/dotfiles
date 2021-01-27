# Custom aliases
alias c="clear; echo; echo; seq 1 (tput cols) | sort -R | spark | lolcat; echo; echo"
alias v="nvim"
alias sl="ls"
alias cat="bat"
alias todo="v /opt/stuffs/todo.md"
alias songs="v /opt/stuffs/songs.txt"
alias ls="lsd"
alias l="ls -al"
alias tree="ls --tree"
alias tt="tt -theme dracula -t 30"
alias def="xdg-open"
alias pacman="pacman -Slq | fzf -m --preview 'cat <(pacman -Si {1} | psub) <(pacman -Fl {1} | awk {print $2}| psub)' | xargs -ro sudo pacman -S"



# Old aliases
alias aup="pamac upgrade --aur"
alias grubup="sudo update-grub"
alias fixpacman="sudo rm /var/lib/pacman/db.lck"
alias tarnow='tar -acf '
alias untar='tar -zxvf '
alias wget='wget -c '
alias psmem='ps auxf | sort -nr -k 4'
alias psmem10='ps auxf | sort -nr -k 4 | head -10'
alias upd='sudo reflector --latest 5 --age 2 --fastest 5 --protocol https --sort rate --save /etc/pacman.d/mirrorlist && cat /etc/pacman.d/mirrorlist && sudo pacman -Syu && fish_update_completions'
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias .....='cd ../../../..'
alias ......='cd ../../../../..'
alias dir='dir --color=auto'
alias vdir='vdir --color=auto'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

