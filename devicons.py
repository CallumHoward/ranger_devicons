#!/usr/bin/env python3
# coding=UTF-8
"""Mappings and helpers for displaying developer icons in ranger."""

# These glyphs, and the mapping of file extensions to glyphs
# has been copied from the vimscript code that is present in
# https://github.com/ryanoasis/vim-devicons

import os
from colors import *
import importlib
import locale


# Get the XDG_USER_DIRS directory names from environment variables
xdgs_dirs = {
    os.path.basename(os.getenv(key).rstrip('/')): icon
    for key, icon in (
        ('XDG_DOCUMENTS_DIR', ''),
        ('XDG_DOWNLOAD_DIR', ''),
        ('XDG_CONFIG_DIR', ''),
        ('XDG_MUSIC_DIR', ''),
        ('XDG_PICTURES_DIR', ''),
        ('XDG_PUBLICSHARE_DIR', ''),
        ('XDG_TEMPLATES_DIR', ''),
        ('XDG_VIDEOS_DIR', ''),
    )
    if os.getenv(key)
}


# all those glyphs will show as weird squares if you don't have the correct patched font
# My advice is to use NerdFonts which can be found here:
# https://github.com/ryanoasis/nerd-fonts
file_node_extensions = {
    '7z'       : color('', 'white'),
    'a'        : color('', 'white'),
    'ai'       : color('', 185),
    'apk'      : color('', 'white'),
    'asm'      : color('', 'white'),
    'asp'      : color('', 'white'),
    'aup'      : color('', 'white'),
    'avi'      : color('', 'white'),
    'awk'      : color('', 59),
    'bash'     : color('', 113),
    'bat'      : color('', 154),
    'bmp'      : color('', 140),
    'bz2'      : color('', 'white'),
    'c'        : color('', 75),
    'c++'      : color('', 204),
    'cab'      : color('', 'white'),
    'cbr'      : color('', 'white'),
    'cbz'      : color('', 'white'),
    'cc'       : color('', 204),
    'class'    : color('', 'white'),
    'clj'      : color('', 107),
    'cljc'     : color('', 107),
    'cljs'     : color('', 67),
    'cmake'    : color('', 66),
    'coffee'   : color('', 185),
    'conf'     : color('', 66),
    'cp'       : color('', 67),
    'cpio'     : color('', 'white'),
    'cpp'      : color('', 67),
    'cs'       : color('󰌛', 58),
    'csh'      : color('', 59),
    'css'      : color('', 60),
    'cue'      : color('', 'white'),
    'csv'      : color('', 113),
    'cxx'      : color('', 67),
    'd'        : color('', 64),
    'dart'     : color('', 25),
    'db'       : color('', 188),
    'deb'      : color('', 'white'),
    'diff'     : color('', 59),
    'dockerfile': color('', 59),
    'dll'      : color('', 'white'),
    'wps'      : color('', 25),
    'wpt'      : color('', 25),
    'doc'      : color('', 25),
    'docx'     : color('', 25),
    'docm'     : color('', 25),
    'dotx'     : color('', 25),
    'dotm'     : color('', 25),
    'dump'     : color('', 188),
    'edn'      : color('', 67),
    'eex'      : color('', 140),
    'efi'      : color('', 'white'),
    'ejs'      : color('', 185),
    'elf'      : color('', 'white'),
    'elm'      : color('', 67),
    'epub'     : color('', 'white'),
    'erl'      : color('', 132),
    'ex'       : color('', 140),
    'exe'      : color('', 'white'),
    'exs'      : color('', 140),
    'f#'       : color('', 67),
    'fifo'     : color('󰟥', 'white'),
    'fish'     : color('', 59),
    'flac'     : color('', 'white'),
    'flv'      : color('', 'white'),
    'fs'       : color('', 67),
    'fsi'      : color('', 67),
    'fsscript' : color('', 67),
    'fsx'      : color('', 67),
    'gem'      : color('', 'white'),
    'gemspec'  : color('', 52),
    'gif'      : color('', 140),
    'go'       : color('', 67),
    'gz'       : color('', 'white'),
    'gzip'     : color('', 'white'),
    'h'        : color('', 140),
    'haml'     : color('', 188),
    'hbs'      : color('', 208),
    'hh'       : color('', 140),
    'hpp'      : color('', 140),
    'hrl'      : color('', 132),
    'hs'       : color('', 140),
    'htaccess' : color('', 'white'),
    'htm'      : color('', 166),
    'html'     : color('', 166),
    'htpasswd' : color('', 'white'),
    'hxx'      : color('', 140),
    'ico'      : color('', 185),
    'img'      : color('', 'white'),
    'ini'      : color('', 66),
    'ipynb'    : color('', 179),
    'iso'      : color('', 'white'),
    'jar'      : color('', 167),
    'java'     : color('', 167),
    'jl'       : color('', 133),
    'jpeg'     : color('', 140),
    'jpg'      : color('', 140),
    'js'       : color('', 185),
    'cjs'      : color('', 185),
    'mjs'      : color('', 185),
    'json'     : color('', 185),
    'jsonc'    : color('', 185),
    'jsx'      : color('', 67),
    'key'      : color('', 'white'),
    'ksh'      : color('', 59),
    'leex'     : color('', 140),
    'less'     : color('', 60),
    'lha'      : color('', 'white'),
    'lhs'      : color('', 140),
    'log'      : color('', 'white'),
    'lua'      : color('', 74),
    'lz'       : color('', 'white'),
    'lzh'      : color('', 'white'),
    'lzma'     : color('', 'white'),
    'm4a'      : color('', 'white'),
    'm4v'      : color('', 'white'),
    'markdown' : color('', 67),
    'md'       : color('', 67),
    'mdx'      : color('', 67),
    'mjs'      : color('', 221),
    'mka'      : color('', 'white'),
    'mkv'      : color('', 'white'),
    'ml'       : color('λ', 173),
    'mli'      : color('λ', 173),
    'mov'      : color('', 'white'),
    'mp3'      : color('', 'white'),
    'mp4'      : color('', 'white'),
    'mpeg'     : color('', 'white'),
    'mpg'      : color('', 'white'),
    'msi'      : color('', 'white'),
    'mustache' : color('', 173),
    'nix'      : color('', 110),
    'o'        : color('', 'white'),
    'ogg'      : color('', 'white'),
    'opus'     : color('', 'white'),
    'part'     : color('', 'white'),
    'pdf'      : color('', 124),
    'php'      : color('', 140),
    'pl'       : color('', 67),
    'pm'       : color('', 67),
    'png'      : color('', 140),
    'pp'       : color('', 'white'),
    'dps'      : color('', 167),
    'dpt'      : color('', 167),
    'ppt'      : color('', 167),
    'pptx'     : color('', 167),
    'pptm'     : color('', 167),
    'pot'      : color('', 167),
    'potx'     : color('', 167),
    'potm'     : color('', 167),
    'pps'      : color('', 167),
    'ppsx'     : color('', 167),
    'ppsm'     : color('', 167),
    'ps1'      : color('', 59),
    'psb'      : color('', 67),
    'psd'      : color('', 67),
    'pub'      : color('', 'white'),
    'py'       : color('', 179),
    'pyc'      : color('', 67),
    'pyd'      : color('', 67),
    'pyo'      : color('', 67),
    'r'        : color('󰴭', 65),
    'rake'     : color('', 52),
    'rar'      : color('', 'white'),
    'rb'       : color('', 52),
    'rc'       : color('', 'white'),
    'rlib'     : color('', 180),
    'rmd'      : color('', 67),
    'rom'      : color('', 'white'),
    'rpm'      : color('', 'white'),
    'rproj'    : color('󰗆', 65),
    'rs'       : color('', 180),
    'rss'      : color('', 255),
    'rtf'      : color('', 'white'),
    's'        : color('', 'white'),
    'sass'     : color('', 204),
    'scala'    : color('', 167),
    'scss'     : color('', 204),
    'sh'       : color('', 59),
    'slim'     : color('', 166),
    'sln'      : color('', 98),
    'so'       : color('', 'white'),
    'sql'      : color('', 188),
    'styl'     : color('', 107),
    'suo'      : color('', 98),
    'svelte'   : color('', 202),
    'svg'      : color('', 215),
    'swift'    : color('', 173),
    't'        : color('', 67),
    'tar'      : color('', 'white'),
    'tex'      : color('󰙩', 58),
    'tgz'      : color('', 'white'),
    'toml'     : color('', 66),
    'torrent'  : color('', 'white'),
    'ts'       : color('', 67),
    'tsx'      : color('', 67),
    'twig'     : color('', 107),
    'vim'      : color('', 29),
    'vimrc'    : color('', 29),
    'vue'      : color('󰡄', 107),
    'wav'      : color('', 'white'),
    'webm'     : color('', 140),
    'webmanifest' : color('', 'white'),
    'webp'     : color('', 140),
    'xbps'     : color('', 'white'),
    'xcplayground' : color('', 173),
    'xhtml'    : color('', 173),
    'et'       : color('󰈛','white'),
    'ett'      : color('󰈛','white'),
    'xls'      : color('', 173),
    'xlt'      : color('󰈛','white'),
    'xlsx'     : color('', 173),
    'xlsm'     : color('󰈛','white'),
    'xlsb'     : color('󰈛','white'),
    'xltx'     : color('󰈛','white'),
    'xltm'     : color('󰈛','white'),
    'xla'      : color('󰈛','white'),
    'xlam'     : color('󰈛','white'),
    'xml'      : color('', 173),
    'xul'      : color('', 173),
    'xz'       : color('', 'white'),
    'yaml'     : color('', 66),
    'yml'      : color('', 66),
    'zip'      : color('', 'white'),
    'zsh'      : color('', 113),
}


# Base mapping for English directory names
dir_node_exact_matches_base = {
    '.git'        : color('', 59),
    'Desktop'     : color('', 4),
    'Documents'   : color('', 4),
    'Downloads'   : color('', 4),
    'Dotfiles'    : color('', 4),
    'Dropbox'     : color('', 27),
    'Music'       : color('', 4),
    'Pictures'    : color('', 4),
    'Public'      : color('', 4),
    'Templates'   : color('', 4),
    'Videos'      : color('', 4),
    'anaconda3'   : color('', 4),
    'go'          : color('', 67),
    'workspace'   : color('', 4),
    'OneDrive'    : color('', 4),
}


# Mapping of localized directory names to their English counterparts.
# Languages are loaded from separate modules in :mod:`ranger_devicons.locales`.
dir_name_translations = {}


def load_translations(lang=None):
    """Load directory name translations for the given language."""
    if lang is None:
        lang = os.getenv('DEVICONS_LANG')
        if not lang:
            loc = locale.getdefaultlocale()[0]
            if loc:
                lang = loc.split('_')[0]
    if not lang:
        return {}
    try:
        module = importlib.import_module(f'ranger_devicons.locales.{lang}')
        return getattr(module, 'translations', {})
    except ModuleNotFoundError:
        return {}


# Populate translations for the current locale
dir_name_translations.update(load_translations())


# Working mapping used by the plugin
dir_node_exact_matches = dict(dir_node_exact_matches_base)


def translate_dir_name(name):
    """Translate localized directory names to English."""
    return dir_name_translations.get(name, name)

# Python 2.x-3.4 don't support unpacking syntex `{**dict}`
# XDG_USER_DIRS
dir_node_exact_matches.update(xdgs_dirs)


file_node_exact_matches = {
    '.bash_aliases'                    : color('', 133),
    '.bash_history'                    : color('', 133),
    '.bash_logout'                     : color('', 133),
    '.bash_profile'                    : color('', 133),
    '.bashprofile'                     : color('', 133),
    '.bashrc'                          : color('', 133),
    '.dmrc'                            : color('', 133),
    '.DS_Store'                        : color('', 133),
    '.fasd'                            : color('', 133),
    '.fehbg'                           : color('', 'white'),
    '.gitattributes'                   : color('', 59),
    '.gitconfig'                       : color('', 59),
    '.gitignore'                       : color('', 59),
    '.gitlab-ci.yml'                   : color('', 166),
    '.gvimrc'                          : color('', 29),
    '.inputrc'                         : color('', 133),
    '.jack-settings'                   : color('', 133),
    '.mime.types'                      : color('', 133),
    '.ncmpcpp'                         : color('', 'white'),
    '.nvidia-settings-rc'              : color('', 133),
    '.pam_environment'                 : color('', 133),
    '.profile'                         : color('', 133),
    '.recently-used'                   : color('', 133),
    '.selected_editor'                 : color('', 133),
    '.vim'                             : color('', 29),
    '.viminfo'                         : color('', 29),
    '.vimrc'                           : color('', 29),
    '.Xauthority'                      : color('', 133),
    '.Xdefaults'                       : color('', 133),
    '.xinitrc'                         : color('', 133),
    '.xinputrc'                        : color('', 133),
    '.Xresources'                      : color('', 133),
    '.zshrc'                           : color('', 133),
    '_gvimrc'                          : color('', 29),
    '_vimrc'                           : color('', 29),
    'a.out'                            : color('', 'white'),
    'authorized_keys'                  : color('', 179),
    'bspwmrc'                          : color('', 66),
    'cmakelists.txt'                   : color('', 66),
    'config'                           : color('', 52),
    'config.ac'                        : color('', 52),
    'config.m4'                        : color('', 52),
    'config.mk'                        : color('', 52),
    'config.ru'                        : color('', 52),
    'configure'                        : color('', 'white'),
    'docker-compose.yml'               : color('', 59),
    'dockerfile'                       : color('', 59),
    'Dockerfile'                       : color('', 59),
    'Dockerfile.dev'                   : color('', 59),
    'Dockerfile.prod'                  : color('', 59),
    'dropbox'                          : color('', 27),
    'favicon.ico'                      : color('', 185),
    'gemfile'                          : color('', 52),
    'gruntfile.coffee'                 : color('', 173),
    'gruntfile.js'                     : color('', 173),
    'gruntfile.ls'                     : color('', 173),
    'gulpfile.coffee'                  : color('', 167),
    'gulpfile.js'                      : color('', 167),
    'gulpfile.ls'                      : color('', 167),
    'ini'                              : color('', 66),
    'known_hosts'                      : color('', 179),
    'ledger'                           : color('', 179),
    'license'                          : color('', 179),
    'LICENSE'                          : color('', 179),
    'LICENSE.md'                       : color('', 179),
    'LICENSE.txt'                      : color('', 179),
    'Makefile'                         : color('', 66),
    'makefile'                         : color('', 66),
    'Makefile.ac'                      : color('', 66),
    'Makefile.in'                      : color('', 66),
    'mimeapps.list'                    : color('', 66),
    'mix.lock'                         : color('', 140),
    'node_modules'                     : color('', 124),
    'package-lock.json'                : color('', 124),
    'package.json'                     : color('', 124),
    'playlists'                        : color('', 'white'),
    'procfile'                         : color('', 140),
    'Rakefile'                         : color('', 52),
    'rakefile'                         : color('', 52),
    'react.jsx'                        : color('', 67),
    'README'                           : color('', 67),
    'README.markdown'                  : color('', 67),
    'README.md'                        : color('', 67),
    'README.rst'                       : color('', 67),
    'README.txt'                       : color('', 67),
    'sxhkdrc'                          : color('', 66),
    'user-dirs.dirs'                   : color('', 66),
    'webpack.config.js'                : color('', 67),
}


def devicon(file):
    """Return the devicon for the given ranger file object."""

    if file.is_directory:
        dir_name = translate_dir_name(file.relative_path)
        return dir_node_exact_matches.get(dir_name, color('', fg=4))
    basename = os.path.basename(file.relative_path)
    if basename.endswith(('.stories.ts', '.stories.tsx', '.stories.js', '.stories.jsx')):
        return color('', 204)
    if basename.endswith(('.test.ts', '.test.tsx', '.spec.ts', '.spec.tsx',
                          '.test.js', '.test.jsx', '.spec.js', '.spec.jsx')):
        return color('', 173)
    return file_node_exact_matches.get(
        basename,
        file_node_extensions.get(file.extension, color('', fg=7)),
    )
