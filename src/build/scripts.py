#!/usr/bin/env python

import argparse
import os

from src.build.clean_svg import CleanSVG
from src.build.helpers.color import Color
from src.build.helpers.print_message import print_build_message
from src.build.icons import IconPNG
from src.build.icons_syntaxes import IconSyntax
from src.build.preferences import Preference
from src.build.utils.build_dir_paths import (
    ALIASES_PATH,
    ASSETS_PATH,
    DATA_PATH,
    ICONS_PNG_PATH,
    ICONS_SVG_PATH,
    PREFERENCES_PATH,
    ICONS_TEST_PATH,
    ICONS_PNG_TEST_PATH,
    ICONS_SYNTAXES_TEST_PATH,
    PREFERENCES_TEST_PATH,
)
from src.build.utils.svg_unused_list import UNUSED_LIST


def main():
    # from https://gist.github.com/jirihnidek/3f5d36636198e852280f619847d22d9e
    # Create the top-level parser
    parser = argparse.ArgumentParser(prog=f'{ Color.CYAN }Builder scripts{ Color.END }')
    # parser.add_argument('-d', '--debug', action='store_true', help='debug flag')

    # Create sub-parser
    subparsers = parser.add_subparsers(dest='subparser_name', help='sub-command help')

    # Create the parser for the "clean" sub-command
    parser_clean = subparsers.add_parser(
        'clean',
        help=f'{ Color.YELLOW }Clean unused SVGs tags and attributes.{ Color.END }',
    )
    parser_clean.add_argument(
        '-a',
        '--all',
        action='store_true',
        required=False,
        help=f'{ Color.YELLOW }Clean all SVGs from src/icons folder.{ Color.END }',
    )
    parser_clean.add_argument(
        '-d',
        '--directory',
        type=str,
        required=False,
        help=f'{ Color.YELLOW }Path to SVGs folder.{ Color.END }',
    )
    parser_clean.add_argument(
        '-f',
        '--file',
        type=str,
        required=False,
        help=f'{ Color.YELLOW }Path to SVG file.{ Color.END }',
    )
    parser_clean.add_argument(
        '-l',
        '--list',
        default=UNUSED_LIST,
        required=False,
        help=f'{ Color.YELLOW }List(str) of unused tags to be removed.{ Color.END }',
    )

    # Create the parser for the "icon-theme" sub-command
    parser_icontheme = subparsers.add_parser(
        'icon-theme',
        help=f'{ Color.YELLOW }Create icon theme PNGs, sublime-syntax '
        f'and tmPreferences.{ Color.END }',
    )
    parser_icontheme.add_argument(
        '-a',
        '--all',
        action='store_true',
        required=False,
        help=f'{ Color.YELLOW }Create all PNGs, sublime-syntaxes and '
        f'tmPreferences.{ Color.END }',
    )
    parser_icontheme.add_argument(
        '-d',
        '--data',
        type=str,
        required=False,
        help=f'{ Color.YELLOW }Path to folder data.{ Color.END }',
    )
    parser_icontheme.add_argument(
        '-f',
        '--file',
        type=str,
        required=False,
        help=f'{ Color.YELLOW }Path to icon data file.{ Color.END }',
    )
    parser_icontheme.add_argument(
        '-i',
        '--icon',
        default=os.path.abspath(ICONS_TEST_PATH),
        type=str,
        required=False,
        help=f'{ Color.YELLOW }Path to icons SVGs folder.{ Color.END }',
    )
    parser_icontheme.add_argument(
        '-p',
        '--png',
        default=os.path.abspath(ICONS_PNG_TEST_PATH),
        type=str,
        required=False,
        help=f'{ Color.YELLOW }Path to destiny for PNGs.{ Color.END }',
    )
    parser_icontheme.add_argument(
        '-s',
        '--syntax',
        default=os.path.abspath(ICONS_SYNTAXES_TEST_PATH),
        type=str,
        required=False,
        help=f'{ Color.YELLOW }Path to destiny for sublime-syntaxes files.{ Color.END }',
    )
    parser_icontheme.add_argument(
        '-t',
        '--tmpreference',
        default=os.path.abspath(PREFERENCES_TEST_PATH),
        type=str,
        required=False,
        help=f'{ Color.YELLOW }Path to destiny for tmPreferences files.{ Color.END }',
    )

    # Create the parser for the "png" sub-command
    parser_png = subparsers.add_parser(
        'png',
        help=f'{ Color.YELLOW }Generate icon PNGs.{ Color.END }',
    )
    parser_png.add_argument(
        '-a',
        '--all',
        action='store_true',
        required=False,
        help=f'{ Color.YELLOW }Generate all PNGs in icons/ folder.{ Color.END }',
    )
    parser_png.add_argument(
        '-d',
        '--data',
        type=str,
        required=False,
        help=f'{ Color.YELLOW }Path to folder data.{ Color.END }',
    )
    parser_png.add_argument(
        '-f',
        '--file',
        type=str,
        required=False,
        help=f'{ Color.YELLOW }Path to icon data file.{ Color.END }',
    )
    parser_png.add_argument(
        '-i',
        '--icon',
        default=os.path.abspath(ICONS_TEST_PATH),
        type=str,
        required=False,
        help=f'{ Color.YELLOW }Path to icons SVGs folder.{ Color.END }',
    )
    parser_png.add_argument(
        '-p',
        '--png',
        default=os.path.abspath(ICONS_PNG_TEST_PATH),
        type=str,
        required=False,
        help=f'{ Color.YELLOW }Path to destiny for PNGs.{ Color.END }',
    )

    # Create the parser for the "preference" sub-command
    parser_preference = subparsers.add_parser(
        'preference',
        help=f'{ Color.YELLOW }Create icons tmPreferences.{ Color.END }',
    )
    parser_preference.add_argument(
        '-a',
        '--all',
        action='store_true',
        required=False,
        help=f'{ Color.YELLOW }Create all tmPreferences in preferences/ folder.{ Color.END }',
    )
    parser_preference.add_argument(
        '-d',
        '--data',
        type=str,
        required=False,
        help=f'{ Color.YELLOW }Path to folder data.{ Color.END }',
    )
    parser_preference.add_argument(
        '-f',
        '--file',
        type=str,
        required=False,
        help=f'{ Color.YELLOW }Path to icon data file.{ Color.END }',
    )
    parser_preference.add_argument(
        '-t',
        '--tmpreference',
        default=os.path.abspath(PREFERENCES_TEST_PATH),
        type=str,
        required=False,
        help=f'{ Color.YELLOW }Path to destiny for tmPreferences files.{ Color.END }',
    )

    # Create the parser for the "syntax" sub-command
    parser_syntax = subparsers.add_parser(
        'syntax',
        help=f'{ Color.YELLOW }Create icons sublime-syntaxes.{ Color.END }',
    )
    parser_syntax.add_argument(
        '-a',
        '--all',
        action='store_true',
        required=False,
        help=f'{ Color.YELLOW }Create all sublime-syntaxes in aliases/ folder.{ Color.END }',
    )
    parser_syntax.add_argument(
        '-d',
        '--data',
        type=str,
        required=False,
        help=f'{ Color.YELLOW }Path to folder data.{ Color.END }',
    )
    parser_syntax.add_argument(
        '-f',
        '--file',
        type=str,
        required=False,
        help=f'{ Color.YELLOW }Path to icon data file.{ Color.END }',
    )
    parser_syntax.add_argument(
        '-s',
        '--syntax',
        default=os.path.abspath(ICONS_SYNTAXES_TEST_PATH),
        type=str,
        required=False,
        help=f'{ Color.YELLOW }Path to destiny for sublime-syntaxes files.{ Color.END }',
    )

    # Namespaces
    args = parser.parse_args()
    # Subparser - subcommands
    parser = args.subparser_name

    # Clean
    if parser == 'clean':
        if args.all and not (args.file or args.directory):
            print_build_message(
                '🛠️  Cleaning all SVGs files:', os.path.abspath(ICONS_TEST_PATH)
            )
            CleanSVG.clean_all_svgs(ICONS_TEST_PATH, args.list)
        elif args.file and not (args.all or args.directory):
            print_build_message('🛠️  Cleaning SVG file:', args.file)
            CleanSVG.clean_svg(args.file, args.list)
        elif args.directory and not (args.all or args.file):
            print_build_message('🛠️  Cleaning all SVGs files:', args.directory)
            CleanSVG.clean_all_svgs(args.directory, args.list)
        else:
            print(parser.print_help())
    # Icon Theme
    elif parser == 'icon-theme':
        if args.all and not (args.file or args.data):
            print(
                f'{ Color.BLUE }[⚙] Starting building all icons PNGs, sublime-syntaxes '
                f'and tmPreferences.{ Color.END }'
            )
            print_build_message(
                '🛠️  Generating all PNGs files:', os.path.abspath(ICONS_PNG_TEST_PATH)
            )
            IconPNG.svg_to_png_all(DATA_PATH, args.icon, args.png)
            print_build_message(
                '🛠️  Creating all icons tmPreferences:',
                os.path.abspath(PREFERENCES_TEST_PATH),
            )
            Preference.preferences_all(DATA_PATH, args.tmpreference)
            print_build_message(
                '🛠️  Creating all icons sublime-syntaxes:',
                os.path.abspath(ICONS_SYNTAXES_TEST_PATH),
            )
            IconSyntax.icons_syntaxes(DATA_PATH, args.syntax)
        elif args.file and not (args.all or args.data):
            print_build_message('🛠️  Generating PNGs file:', args.png)
            IconPNG.svg_to_png(args.file, args.icon, args.png)
            print_build_message('🛠️  Creating icon tmPreferences:', args.tmpreference)
            Preference.preferences(args.file, args.tmpreference)
            print_build_message('🛠️  Creating icon sublime-syntaxes:', args.syntax)
            IconSyntax.icon_syntax(args.file, args.syntax)
        elif args.data and not (args.all or args.file):
            print(
                f'{ Color.BLUE }[⚙] Starting building all icons PNGs, sublime-syntaxes '
                f'and tmPreferences.{ Color.END }'
            )
            print_build_message('🛠️  Generating all PNGs files:', args.png)
            IconPNG.svg_to_png_all(args.data, args.icon, args.png)
            print_build_message(
                '🛠️  Creating all icons tmPreferences:', args.tmpreference
            )
            Preference.preferences_all(args.data, args.tmpreference)
            print_build_message('🛠️  Creating all icons sublime-syntaxes:', args.syntax)
            IconSyntax.icons_syntaxes(args.data, args.syntax)
        else:
            print(parser.print_help())
    # PNGs
    elif parser == 'png':
        if args.all and not (args.file or args.data):
            print_build_message(
                '🛠️  Generating all PNGs files:', os.path.abspath(ICONS_PNG_TEST_PATH)
            )
            IconPNG.svg_to_png_all(DATA_PATH, args.icon, args.png)
        elif args.file and not (args.all or args.data):
            print_build_message('🛠️  Generating PNGs file:', args.png)
            IconPNG.svg_to_png(args.file, args.icon, args.png)
        elif args.data and not (args.all or args.file):
            print_build_message('🛠️  Generating all PNGs files:', args.png)
            IconPNG.svg_to_png_all(args.data, args.icon, args.png)
        else:
            print(parser.print_help())
    # tmPreferences
    elif parser == 'preference':
        if args.all and not (args.file or args.data):
            print_build_message(
                '🛠️  Creating all icons tmPreferences:',
                os.path.abspath(PREFERENCES_TEST_PATH),
            )
            Preference.preferences_all(DATA_PATH, args.tmpreference)
        elif args.file and not (args.all or args.data):
            print_build_message('🛠️  Creating icon tmPreferences:', args.tmpreference)
            Preference.preferences(args.file, args.tmpreference)
        elif args.data and not (args.all or args.file):
            print_build_message(
                '🛠️  Creating all icons tmPreferences:', args.tmpreference
            )
            Preference.preferences_all(args.data, args.tmpreference)
        else:
            print(parser.print_help())
    # Sublime-syntaxes
    elif parser == 'syntax':
        if args.all and not (args.file or args.data):
            print_build_message(
                '🛠️  Creating all icons sublime-syntaxes:',
                os.path.abspath(ICONS_SYNTAXES_TEST_PATH),
            )
            IconSyntax.icons_syntaxes(DATA_PATH, args.syntax)
        elif args.file and not (args.all or args.data):
            print_build_message('🛠️  Creating icon sublime-syntaxes:', args.syntax)
            IconSyntax.icon_syntax(args.file, args.syntax)
        elif args.data and not (args.all or args.file):
            print_build_message('🛠️  Creating all icons sublime-syntaxes:', args.syntax)
            IconSyntax.icons_syntaxes(args.data, args.syntax)
        else:
            print(parser.print_help())
    else:
        print(parser.print_help())


if __name__ == '__main__':
    main()