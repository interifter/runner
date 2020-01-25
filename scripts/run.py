import pkg_resources

import click

from colors import COLORS, WRITERS

discovered_plugins = {
    entry_point.name: entry_point.load()
    for entry_point
    in pkg_resources.iter_entry_points('runner.colors.plugins')
}

@click.group("run")
def main():
    return 0



def find_plugin_info(name, collection):
    for plugin in discovered_plugins.keys():
        upper = plugin.upper()
        if not upper in collection:
            ride_attr = getattr(discovered_plugins[plugin], name)
            if ride_attr:
                collection[upper] = ride
    return collection.keys()


@main.command()
@click.argument('color', type=click.Choice(find_plugin_info('ride', COLORS), case_sensitive=False))
def ride(color):
    color = color.upper()
    click.echo(COLORS[color]())
    

@main.command()
@click.argument('color', type=click.Choice(find_plugin_info('write', WRITERS), case_sensitive=False))
def write(color):
    color = color.upper()
    click.echo(WRITERS[color]())

@main.command()
def plugins():
    click.echo("Discovered Plugins:")
    click.echo(discovered_plugins)


