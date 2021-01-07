" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  "autocmd VimEnter * PlugInstall
  "autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

call plug#begin('~/.config/nvim/autoload/plugged')

    " Better Syntax Support
    Plug 'sheerun/vim-polyglot'
    " File Explorer
    Plug 'scrooloose/NERDTree'
    " Auto pairs for '(' '[' '{'
    Plug 'jiangmiao/auto-pairs'
    " One-dark Theme
    Plug 'joshdick/onedark.vim'
    " Stable version of coc
    Plug 'neoclide/coc.nvim', {'branch': 'release0'}
    " Keeping up to date with master
    Plug 'neoclide/coc.nvim', {'do': 'yarn install --frozen-lockfile'}
    " Airline Status
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'
    " Dracula Theme
    Plug 'dracula/vim', { 'as': 'dracula' }
    " Split Terminal
    Plug 'vimlab/split-term.vim'
call plug#end()
