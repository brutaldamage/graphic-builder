import click
from casters import casters

@click.command()
@click.option('--date', '-d', help='The date of the match')
@click.option('--time', '-t', help='The time that the match will be played at')
@click.option('--casterone', '-c1', help='Caster of Player One')
@click.option('--castertwo', '-c2', help='Caster of Player Two')

#def getCasterImage(caster):
    # Pull prebuilt image of caster by name

def setup(date, time, casterone, castertwo):

    # Validate input
    p1 = casters.get(casterone)
    p2 = casters.get(castertwo)

    if (p1 and p2):
        print('\r')
        print('-------------------')
        print('- Graphic Builder -')
        print('-------------------')
        print('\r')
        print('Match will be on ' + date + ', starting at ' + time + ' CST')
        print(p1 + ' vs ' + p2)
    else:
        print('You dun goofed. Type better!')
        exit()

    # Use valid keys to get data

    # Build image

    # Return image

    

if __name__ == '__main__':
    setup()