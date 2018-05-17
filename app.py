import click
import utils as ut

@click.group()
@click.option('--hellow', is_flag=True)
def cli(hellow):
    if hellow:
        click.echo('Hellow World')

@cli.command()
#@click.option('--download', default = False, help="Downloda Dataset")
def download():
    """Command for Download the Dataset"""
    ut.download_dataset()

if __name__ == '__main__':
    cli()
