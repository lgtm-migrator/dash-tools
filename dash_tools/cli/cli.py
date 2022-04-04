'''
 # @ Author: Andrew Hossack
 # @ Create Time: 2022-04-01 12:47:58
'''
import os
import argparse
from dash_tools.templating import buildTemplate
from dash_tools.templating import templateUtils
from dash_tools.version import __version__


def handle_args(parser: argparse.ArgumentParser, invoke_directory: os.PathLike):
    """
    Handles the arguments passed to the CLI.
    """
    args = parser.parse_args()

    if not (args.init or args.templates):
        parser.print_help()
        exit('\ndash-tools: error: too few arguments')

    if args.init:

        possible_template = args.init[1] if len(
            args.init) > 1 else templateUtils.Templates.DEFAULT

        buildTemplate.create_app(
            base_dir=invoke_directory,
            app_name=args.init[0],
            use_template=possible_template)

        print(f'dash-tools: init: finished')

    if args.templates:
        print('dash-tools: templates: List of available templates:')

        for template in templateUtils.Templates:
            print(f'{template.value}')


def main():
    """
    dash-tools CLI entry point.
    """
    invoke_directory = os.getcwd()

    parser = argparse.ArgumentParser(
        description='The dash-tools CLI for Plotly Dash.')

    parser.add_argument(
        '--version',
        action='version',
        version=__version__)

    parser.add_argument(
        '-i',
        '--init',
        help='Create a new Dash app. Args: REQUIRED: <app name> OPTIONAL: <template> (Default: "default").',
        nargs='+')

    parser.add_argument(
        '--templates',
        help='List available templates.',
        default=False,
        action='store_true')

    handle_args(parser, invoke_directory)
