import typer
import os


app = typer.Typer()




@app.command()
def hello(name: str):
    os.system(f'echo {name}')
    # os.environ['HELLO'] = 'Bob'
    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")

@app.command()
def hey():

    typer.echo(f"hey {os.environ.get('HELLO', 'Not Set')}!")


if __name__ == "__main__":
    app()