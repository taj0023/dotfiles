" My custom mappings
nnoremap <F8> :NERDTreeToggle<CR>
nnoremap <C-a> ggVG
nnoremap <leader>f :Files<CR>

autocmd Filetype python nnoremap <buffer> <F5> :w<CR>:ter python %<CR>i
autocmd Filetype java nnoremap <buffer> <F5> :w<CR>:ter javac % && java %:t:r && rm ./*.class<CR>i

autocmd Filetype java inoremap <buffer> console System.out.println("");<Esc>hhi
autocmd Filetype java inoremap <buffer> main public static void main(String args[]){}<Esc>i<CR><CR><Esc>ki<Tab><Tab>
autocmd Filetype python inoremap <buffer> console print("")<Esc>hi
autocmd Filetype javascript inoremap <buffer> console console.log("");<Esc>hhi

autocmd Filetype python nnoremap <F6> 0i# <Esc>j 
autocmd Filetype java nnoremap <F6> <S-^>i// <Esc>j 
nnoremap <F7> 0lli<BS><BS><Esc>j
inoremap <C-s> <Esc>:w<CR>
nnoremap <F2> i#!/usr/bin/env python3<CR>
autocmd Filetype php inoremap <C-p> <?php ?><Esc>hhi 
" autocmd Filetype php,html inoremap ><Tab> <Esc><S-^>lvey<S-$>a></><Esc>hpF<i

" Better nav for omnicomplete
inoremap <expr> <c-j> ("\<C-n>")
inoremap <expr> <c-k> ("\<C-p>")

" Use alt + hjkl to resize windows
nnoremap <M-j>    :resize -2<CR>
nnoremap <M-k>    :resize +2<CR>
nnoremap <M-h>    :vertical resize -2<CR>
nnoremap <M-l>    :vertical resize +2<CR>

" Easy CAPS
inoremap <c-u> <ESC>viwUi
nnoremap <c-u> viwU<Esc>

" TAB in general mode will move to text buffer
nnoremap <TAB> :bnext<CR>
" SHIFT-TAB will go back
nnoremap <S-TAB> :bprevious<CR>

" Alternate way to save
nnoremap <C-s> :w<CR>
" Alternate way to quit
nnoremap <C-Q> :wq!<CR>
" Use control-c instead of escape
nnoremap <C-c> <Esc>
" <TAB>: completion.
inoremap <expr><TAB> pumvisible() ? "\<C-n>" : "\<TAB>"

" Better tabbing
vnoremap < <gv
vnoremap > >gv

" Better window navigation
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

nnoremap <Leader>o o<Esc>^Da
nnoremap <Leader>O O<Esc>^Da
