import click, datetime, logging
from casters import casters
from wand.image import Image, COMPOSITE_OPERATORS
from wand.drawing import Drawing, TEXT_ALIGN_TYPES
from wand.display import display
from wand.color import Color

@click.command()
@click.option('--date', '-d', help='The date of the match (x/x/xxxx)')
@click.option('--time', '-t', help='The time that the match will be played at (x:xxPM)')
@click.option('--casterone', '-c1', help='Caster of Player One')
@click.option('--castertwo', '-c2', help='Caster of Player Two')

def setup(date, time, casterone, castertwo):
    appSetup()

    # Validate input
    p1 = casters.get(casterone)
    p2 = casters.get(castertwo)
    d = datetime.datetime.strptime(date, "%m/%d/%Y")
    formattedMatchDate = d.strftime("%a") + ', ' + d.strftime('%b') + ' ' + d.strftime('%d')

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

    # Build social image
    with Drawing() as draw:
        with Image(filename='template/social_template.png') as original:
            with original.clone() as bg:
                f1 = 'template/casters/' + casterone + '.png'
                f2 = 'template/casters/' + castertwo + '.png'
                with Image(filename=f1) as casterOneImage:
                    bg.composite(casterOneImage, left=90, top=625)
                with Image(filename=f2) as casterTwoImage:
                    bg.composite(casterTwoImage, left=570, top=625)

                draw.font = 'template/strikefighter.ttf'
                draw.font_size = 48
                draw.stroke_width = 1
                draw.stroke_color = Color('black')
                draw.fill_color = Color('#f08728')
                draw.text_alignment = 'center'
                draw.text(480, 430, formattedMatchDate + ' @ ' + time + ' CST')

                draw.fill_color = Color('white')
                draw.stroke_opacity = 0

                formattedCasterOneText = formatCasterText(p1)
                draw.font_size = formattedCasterOneText.fontSize
                if (formattedCasterOneText.bottom == ''):
                    draw.text(260, 585, formattedCasterOneText.top)
                else:
                    draw.text(260, 560, formattedCasterOneText.top)
                    draw.text(260, 605, formattedCasterOneText.bottom)

                formattedCasterTwoText = formatCasterText(p2)
                draw.font_size = formattedCasterTwoText.fontSize
                if (formattedCasterTwoText.bottom == ''):
                    draw.text(730, 585, formattedCasterTwoText.top)
                else:
                    draw.text(730, 560, formattedCasterTwoText.top)
                    draw.text(730, 605, formattedCasterTwoText.bottom)

                with Image(filename='template/vs_text.png') as vsText:
                    bg.composite(vsText, left=320, top=710)

                draw(bg)
                socialFilename = 'output/social_' + casterone + '_' + castertwo + '.png'
                bg.save(filename=socialFilename)

def appSetup():
    logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def formatCasterText(caster):
    text = CasterText()
    l = len(caster)
    
    if (l > 32):
        text.fontSize = 30

    if (l <= 12):
        text.top = caster
        return text
    else:
        words = caster.split()
        topCharCount = 0
        for x in words:
            if (topCharCount <= 12):
                if (len(text.top) == 0):
                    text.top = x
                else:
                    text.top = text.top + ' ' + x

                topCharCount = topCharCount + len(x)
            else:
                if (len(text.bottom) == 0):
                    text.bottom = x
                else:
                    text.bottom = text.bottom + ' ' + x
        
        return text

class CasterText:
    top = ''
    bottom = ''
    fontSize = 40

if __name__ == '__main__':
    setup()