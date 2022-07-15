import Get_Info as info
from console import console
from rich.table import Table
from rich import box


# Add ability to export results
def setup():
    do_again = 'y'
    while(do_again == 'y' or do_again == 'Y'):
        console.rule('[bold]Select an Action')
        table = Table(box=box.HEAVY_EDGE, show_lines=True, expand=True)

        table.add_column('Action')
        table.add_column('Description')

        table.add_row('[bold]0. Check Collection(s) Information', 'Check listings for a specified collection.')
        table.add_row('[bold]1. Check Launchpad', 'Check current and upcoming launches on Magic Eden.')
        # TODO - Rename 0 and 2 to be more appropriate
        table.add_row('[bold]2. Check Listed', 'Set up floor price alerts for specified collections')
        table.add_row('[bold]3. Floor Price Alerts', 'Set up or view floor price alerts for specified collections')
        table.add_row('[bold]4. Generate Collection', 'Generate NFT collection')
        console.print(table)

        action = input('Action: ')
        if(action.__contains__('0')):
            check_collection_information()
        elif(action.__contains__('1')):
            check_launchpad()
        elif(action.__contains__('2')):
            check_listed()
        elif(action.__contains__('3')):
            set_up_alerts()
        elif(action.__contains__('4')):
            generate_collection()

        do_again = input('Select another action? (Y/N):')


def check_collection_information():
    ## Test List:        Mintin, yetai, lost souls, sol drunks      ,      DegenDoJo, succuverse, bulldog_billionaiRes,   bullDog doghouses    , degods
    console.print('[green underline]Check Collection(s) Information')
    console.print('[blue]Enter collection name(s) (seperate multiple with commas):')
    collections = input().split(',')

    with console.status('Retreiving Collections...'):
        for x in collections:
            # TODO - Check for empty strings
            listing_info = info.getListingInfo(x.strip().replace(' ', '_').lower())
            
            # console.print(listing_info)

            if(len(listing_info) > 1):
                console.rule(listing_info['symbol'])
                console.print('[bold]Floor Price[/bold]: %s' %(listing_info['floorPrice'] / 1000000000))
                console.print('[bold]Listed Count[/bold]: %s' %(listing_info['listedCount']))
                if(len(listing_info) >= 5):
                    console.print('[bold]Average Price (24hr): %s' %(listing_info['avgPrice24hr'] / 1000000000))
                console.print('[bold]Volume All Time[/bold]: %s' %(listing_info['volumeAll'] / 1000000000))


def check_launchpad():
    console.print('[green underline]Check Launchpad')
    launch_info = info.getLaunchpadInfo()
    # return launch_info
    for x in launch_info:
        console.rule('[bold]%s' %(x['name']))
        table = Table(box=box.HEAVY_EDGE, show_lines=True, expand=True)

        table.add_column('')
        table.add_column('')

        table.add_row('[bold]Description:[/bold]', str(x['description']))
        table.add_row('[bold]Price:[/bold]', str(x['price']))
        table.add_row('[bold]Size:[/bold]', str(x['size']))
        table.add_row('[bold]Launch Time:[/bold]', str(x['launchTime']))
        console.print(table)


def check_listed():
    console.print('[green underline]Check Listed')
    console.print('[blue]Enter collection name(s) (seperate mutliple with commas):')
    collections = input().split(',')

    console.print('[blue]Enter max SOL to be included or \'fp\' for floorprice:')
    max_sol = input()

    if(max_sol.lower().__contains__('fp')):
        max_sol = info.getListingInfo(collections[0].replace(' ', '_'))['floorPrice'] / 1000000000
        console.print('[blue]Using current floor price of %s SOL' %(max_sol))
    
    listings = info.getCollectionListed(collections[0].replace(' ', '_'), float(max_sol))
    listings.sort(key=arrSortKey)

    for x in listings:
        console.rule('')
        table = Table(box=box.HEAVY_EDGE, show_lines=True, expand=True)

        table.add_column('Name')
        table.add_column('Information')

        table.add_row('[bold]%s' %(x['name']), '[bold]Price:[/bold] %s\n[bold]Link:[/bold] %s' %(x['price'], x['link']))
        console.print(table)
    console.print('%s listings found under %s SOL' %(len(listings), max_sol))


# TODO - Make it work
def set_up_alerts():
    # TODO - Use subprocess to set up alerts on linux
    # TODO - Figure out how to setup alerts on Window
    console.print('[green underline]Set up Alerts')

# TODO - Make it work
def generate_collection():
    console.print('[green underline]Generate Collection')


def arrSortKey(e):
    '''Sort array of retreived NFT's from lowest to highest price'''
    return e['price']

setup()