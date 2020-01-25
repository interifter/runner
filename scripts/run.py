import pkg_resources

import click

from colors import COLORS

discovered_plugins = {
    entry_point.name: entry_point.load()
    for entry_point
    in pkg_resources.iter_entry_points('runner.colors.plugins')
}

@click.group("run")
def main():
    return 0

def find_colors():
    for plugin in discovered_plugins.keys():
        upper = plugin.upper()
        if not upper in COLORS:
            COLORS[upper] = discovered_plugins[plugin]
    return COLORS.keys()

@main.command()
@click.argument('color', type=click.Choice(find_colors(), case_sensitive=False))
def ride(color):
    color = color.upper()
    click.echo(COLORS[color]())
    click.echo("Discovered Plugins:")
    click.echo(discovered_plugins)
    


