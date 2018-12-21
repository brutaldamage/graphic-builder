import click, datetime, logging
from casters import casters
from wand.image import Image

@click.command()
@click.option('--date', '-d', help='The date of the match (x/x/xxxx)')
@click.option('--time', '-t', help='The time that the match will be played at (x:xxPM)')
@click.option('--casterone', '-c1', help='Caster of Player One')
@click.option('--castertwo', '-c2', help='Caster of Player Two')

#def getCasterImage(caster):
    # Pull prebuilt image of caster by name

def setup(date, time, casterone, castertwo):
    appSetup()

    # Validate input
    p1 = casters.get(casterone)
    p2 = casters.get(castertwo)
    d = datetime.datetime.strptime(date, "%m/%d/%Y")
    formattedMatchDate = d.strftime("%A") + ', ' + d.strftime('%b') + ' ' + d.strftime('%d')

    if (p1 and p2):
        print('\r')
        print('---------------------------------------------------------')
        print('-------------------- Graphic Builder --------------------')
        print('---------------------------------------------------------')
        print('\r')
        print('Match will be on ' + formattedMatchDate + ' starting at ' + time + ' CST')
        print(p1 + ' vs ' + p2)
    else:
        logging.error('Not able to find one or both of the casters passed in.')
        exit()

    # Use valid keys to get data
        # getCasterImage(casterone)
        # getCasterImage(castertwo)
    # Build image
        #with Image(width=200, height=100) as img:
            #img.save(filename='200x100-transparent.png')
    # Return image

def appSetup():
    logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    

if __name__ == '__main__':
    setup()