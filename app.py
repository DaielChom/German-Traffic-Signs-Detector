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
    """Download and prepare dataset for training usaging kiwi Challenge structure of data"""
    ut.download_dataset()

@cli.command()
@click.option('--model', '-m', default = False, help=" Model to use for train \n1. Use 'LRSL' for logistic regression model using scikit-learn\n2.")
@click.option('--directory', '-d', default = False, help = "Directory with trainig data")
def train(model, directory):
    """Train a model """

    if model and directory:
        ut.select_train_model(model, directory)
    else:
        print("Options not select")

@cli.command()
@click.option('--model','-m', default = False, help=" Model to use for test \n1. Use 'LRSL' for logistic regression model using scikit-learn\n2.")
@click.option('--directory', '-d', default = False, help = "Directory with test data")
def test(model, directory):
    """Test a model"""
    if model and directory:
        ut.select_test_model(model, directory)
    else:
        print("Options not found")

if __name__ == '__main__':
    cli()
