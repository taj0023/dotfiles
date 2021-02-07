" My custom mappings
nnoremap <C-a> ggVG
nnoremap <leader>f :Files<CR>
autocmd Filetype vim nnoremap <buffer> <leader>r :so %<CR>
nnoremap <leader>t :FloatermNew --autoclose=2<CR>
nnoremap <leader>m :FloatermNew --autoclose=2 ytop<CR>
nnoremap <leader>p :FloatermNew --autoclose=2 python<CR>
cmap W w
cmap Q q

autocmd Filetype rust nnoremap <buffer> <leader>r :w<CR>:FloatermNew rustc % && ./%:t:r && rm ./%:t:r<CR>
autocmd Filetype java nnoremap <buffer> <leader>r :w<CR>:FloatermNew javac % && java %:t:r && rm ./*.class<CR>
autocmd FileType c nnoremap <buffer> <leader>r :w<CR>:FloatermNew gcc -o noice % && ./noice && rm ./noice<CR>
autocmd FileType javascript nnoremap <buffer> <leader>r :w<CR>:FloatermNew node %<CR>
autocmd Filetype python nnoremap <buffer> <leader>r :w<CR>:FloatermNew python %<CR>

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
