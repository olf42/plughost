#!/usr/bin/env python3
import click
import importlib
import plughost.signal as signal
import weakref

from pkg_resources import iter_entry_points

for entry_point in iter_entry_points(
        group='plughost.plugin'):
    importlib.import_module(entry_point.module_name)

def modify_names(names):
    for name in names:
        results = signal.name_pre_modification.emit(name)
        for result in results:
            print(result)
        name_mod = modify_name(name)
        signal.name_post_modification.emit(name)
        yield name_mod

def modify_name(name):
    name_mod = f"{name}_Rosenkohl"
    return name_mod


@click.command()
@click.argument("name", nargs=-1)
def main(name):
    for n in modify_names(name):
        print(n)

if __name__ == "__main__":
    main()
