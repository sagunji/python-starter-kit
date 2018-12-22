import click


@click.group(invoke_without_command=True)
@click.option("--info", is_flag=True, help="Prints the information of the application")
def main(info):
    """Prints out the name of the application"""
    print("Python-Starter-Kit")


@main.command()
def looper():
    """Runs a for loop"""
    for i in range(1, 10):
        print(i)
