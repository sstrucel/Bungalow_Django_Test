from django.core.management.base import BaseCommand, CommandError
import csv
import re

from Bungalow.Rental_API.models import Listing

class Command(BaseCommand):
    help = 'Adds a CSV to the database'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
        with open(options['filename']) as data:
            csv_reader = csv.reader(data, delimiter=',')
            lineNo = 0
            for line in csv_reader:
                if lineNo!=0:
                    listing = parse_line(self,line)
                    try:
                        listing.save()
                    except BaseException as e:
                        self.stdout.write(str(e))
                        raise CommandError('Record "%s" encountered an error' % listing.address)
                lineNo+=1
                

        self.stdout.write('Successfully imported data from "%s"' % options['filename'])

def parse_line(self,line):
   area_unit=line[0]
   bathrooms= defaultIfEmpty(line[1],0)
   bedrooms=defaultIfEmpty(line[2],0)
   home_size=defaultIfEmpty(line[3],0)
   home_type=line[4]
   last_sold_date=parse_slash_date(line[5])
   last_sold_price=defaultIfEmpty(line[6],0)
   link=line[7]
   price=parsePrice(line[8])
   property_size=defaultIfEmpty(line[9],0)
   rent_price=defaultIfEmpty(line[10],0)
   rentzestimate_amount=defaultIfEmpty(line[11],0)
   rentzestimate_last_updated=parse_slash_date(line[12])
   tax_value=defaultIfEmpty(line[13],0)
   tax_year=defaultIfEmpty(line[14],0)
   year_built=defaultIfEmpty(line[15],0)
   zestimate_amount=defaultIfEmpty(line[16],0)
   zestimate_last_updated=parse_slash_date(line[17])
   zillow_id=defaultIfEmpty(line[18],0)
   address=line[19]
   city=line[20]
   state=line[21]
   zipcode=line[22]
   return Listing(area_unit=area_unit,bathrooms=bathrooms,bedrooms=bedrooms,home_size=home_size,home_type=home_type,last_sold_date=last_sold_date,last_sold_price=last_sold_price,link=link,price=price,property_size=property_size,rent_price=rent_price,rentzestimate_amount=rentzestimate_amount,rentzestimate_last_updated=rentzestimate_last_updated,tax_value=tax_value,tax_year=tax_year,year_built=year_built,zestimate_amount=zestimate_amount,zestimate_last_updated=zestimate_last_updated,zillow_id=zillow_id,address=address,city=city,state=state,zipcode=zipcode)

def defaultIfEmpty(value,default):
    #if the string is all spaces, null or empty return the default
    return value if value and value.strip() else default
def parsePrice (value):
    if not( value and value.strip()):
        return 0
    number =  float(value[1:-1])
    multiplierChar = value[-1:]
    if multiplierChar=='M':
        return number*1000000
    elif multiplierChar=='K':
        return number*1000
    
def parse_slash_date(value):
    if not( value and value.strip()):
        return '1900-1-1'
    m = re.match(r'^(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})/(?P<year>[0-9]{4})$', value)
    if m:
        return '%s-%s-%s' % (
            m.group('year'), m.group('month'), m.group('day'))