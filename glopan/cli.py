"""Command line interface for Glowing Pancake"""
from pathlib import Path
import typing as t

import typer

import glopan

VERSION_STR = glopan.__version__
CONTEXT_SETTINGS = {'help_option_names': ['-h', '--help']}

# Initialize Typers
# Main
main = typer.Typer(
    add_completion=False,
    context_settings=CONTEXT_SETTINGS,
    no_args_is_help=True,
    help=f'✨🥞✨v{VERSION_STR}.',
)

config_typer = typer.Typer(
    name='config',
    context_settings=CONTEXT_SETTINGS,
    no_args_is_help=True,
    help='Configuration',
)

main.add_typer(config_typer)


@main.command(
    no_args_is_help=True,
)
def convert(
    filename: str = typer.Argument(..., help='The file to convert.'),
    from_format: t.Optional[str] = typer.Option(
        None, '--fromformat', '-ff', help='The format to convert from'
    ),
    to_format: str = typer.Option(
        ..., '--toformat', '-tf', help='The format to convert to'
    ),
):
    """Convert a file to a given format."""
    if from_format is None:
        from_format = filename[filename.index('.') + 1 :]
    converter = from_format.lower() + '_to_' + to_format.lower()
    converter_function = getattr(glopan, converter, None)
    if converter_function is not None:
        if Path(filename).exists():
            converter_function(filename)
        else:
            typer.echo(f'The file {filename} does not exist.')
    else:
        typer.echo(
            'No available function to convert from '
            f'{from_format} to {to_format}.'
        )


@main.command(
    no_args_is_help=True,
)
def combine(
    filenames: str = typer.Argument(..., help='The files to combine.')
):
    """Combine several files to one."""
    print(filenames)


# Config commands
@config_typer.command(
    'set',
    no_args_is_help=True,
)
def set_config(
    key: str = typer.Argument(..., help='The key to set'),
    value: str = typer.Argument(..., help='The value of the key to set'),
):
    """Set the value of a configuration key."""
    glopan.config.set(key, value)


@config_typer.command()
def reset():
    """Reset the configuration to an empty state."""
    glopan.config.reset()
