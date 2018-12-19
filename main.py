import click

@click.command()
@click.option('--date', '-d', help='The date of the match')
@click.option('--time', '-t', help='The time that the match will be played at')
@click.option('--casterOne', '-c1', help='Caster of Player One')
@click.option('--casterTwo', '-c2', help='Caster of Player Two')

def getCasterName(caster):
    # Look up caster by name

def getCasterImage(caster):
    # Pull prebuilt image of caster by name

def setup(date, time, casterOne, casterTwo):
    print('Graphic Builder')

if __name__ == '__main__':
    setup()