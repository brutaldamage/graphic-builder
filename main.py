import click, datetime
from casters import casters

@click.command()
@click.option('--date', '-d', help='The date of the match (x/x/xxxx)')
@click.option('--time', '-t', help='The time that the match will be played at (x:xxPM)')
@click.option('--casterone', '-c1', help='Caster of Player One')
@click.option('--castertwo', '-c2', help='Caster of Player Two')

#def getCasterImage(caster):
    # Pull prebuilt image of caster by name

def setup(date, time, casterone, castertwo):

    # Validate input
    p1 = casters.get(casterone)
    p2 = casters.get(castertwo)
    d = datetime.datetime.strptime(date, "%m/%d/%Y")
    formattedMatchDate = d.strftime("%A") + ', ' + d.strftime('%b') + ' ' + d.strftime('%d')

    if (p1 and p2):
        print('\r')
        print('-------------------')
        print('- Graphic Builder -')
        print('-------------------')
        print('\r')
        print('Match will be on ' + formattedMatchDate + ' starting at ' + time + ' CST')
        print(p1 + ' vs ' + p2)
    else:
        print('You dun goofed. Type better!')
        exit()

    # Use valid keys to get data

    # Build image

    # Return image

    

if __name__ == '__main__':
    setup()