# Bungalow Django Test
Basic Django API for Bungalow Technical Test
## Required Libraries
Requires the following libraries:

django 

djangorestframework

django-filters

## Description

This API provides access to query a set of Rental records which have information about availible rental property and their associated attributes

### Usage

http://\<server>:8000/api/listings/\<querystring>

where \<querystring> starts with a ? and an attribute query followed by an susequent attribute queries append with a &

### Atributes
| Attribute     | Description   | Sample Query  |
| ------------- |---------------| --------------|
| area_unit     | Units for area values  | area_unit=SqFt |
| bathrooms| # of bathrooms (includes .5s)| bathrooms  |
| bedrooms | # of bedrooms      |  bedrooms=4 |
| home_size | Size of home (in units specified by area unit)    |  home_size=4695 |
| home_type | Type of Home (SingleFamily, VacantResidentialLand, Miscellaneous, MultiFamily2To4,Condominium, Apartment, Duplex)     |home_type=SingleFamily |
| last_sold_date | Date when the property was last sold     | last_sold_date=03/04/2016 |
| last_sold_price | Last price the property was sold at      |    last_sold_price=2450000 |
| link | Link to the rental listing     |   link=https://www.zillow.com/homedetails/3923-Carpenter-Ct-Studio-City-CA-91604/20028217_zpid/ |
| price | Price the property is worth currently     | ?price=739000 |
| property_size | Size of property (in units specified by area unit)     |    property_size=10611 |
| rent_price | Price of rent    |   rent_price=0 |
| rentzestimate_amount | Rent estimate     |    rentzestimate_amount=2850 |
| rentzestimate_last_updated | Date when the rent estimate was last updated    |    rentzestimate_last_updated=08/07/2018|
| tax_value | Cost of taxes     |    tax_value=215083 |
| tax_year | Year when taxes where calculated   |  tax_year=2017 |
| year_built | Year when the property was built    |  year_built=1956|
| zestimate_amount | Estimate property worth?      |   zestimate_amount=709630 |
| zestimate_last_updated |Date when the property estimate was last updated     |     zestimate_last_updated=08/07/2018 |
| zillow_id | Unique Zillow ID     |    zillow_id=19866015 |
| address | Address of the property     |   address=11554%20Kelsey%20St |
| city | City of property     |   city=West%20Hills |
| state | State of property    |  state=CA |
| zipcode | Zipcode     |   zipcode=91307|

## Seeding Data 

As part of the exercise a function was made to consume an excel file and populate the database. This function can be invoked by the following command

python manage.py readcsv C:\challenge_data.csv

where C:\challenge_data.csv can be replaced with the location of the specified CSV

## Creation of New Records

To create a new record with this api you can use a POST Ajax call to /api/listings/ with the required data in the data parameter. 
### Example

$.ajax({

    url: '/api/listings/',
    method: 'POST',
    data: "{
        "area_unit": "SqFt",
        "bathrooms": "4.50",
        "bedrooms": 5,
        "home_size": 3760,
        "home_type": "SingleFamily",
        "last_sold_date": "2015-09-15",
        "last_sold_price": 2775000,
        "link": "https://www.zillow.com/homedetails/11554-Kelsey-St-Studio-City-CA-91604/20027035_zpid/",
        "price": 277000,
        "property_size": 27799,
        "rent_price": 0,
        "rentzestimate_amount": 11970,
        "rentzestimate_last_updated": "2018-08-07",
        "tax_value": "2856000.00",
        "tax_year": 2017,
        "year_built": 1934,
        "zestimate_amount": 3431400,
        "zestimate_last_updated": "2018-08-07",
        "zillow_id": 20027035,
        "address": "11554 Kelsey St",
        "city": "Studio City",
        "state": "CA",
        "zipcode": "91604"
    }",
    contentType: "application/json",
    processData: false,
    headers: {
      'Accept': 'text/html; q=1.0, */*'
    },
  });
 
## Notes

Currently the API only allows for exact match queries with the DjangoFilterBackend. However the model was made using field that use type chosen to reflect the source data. Therefore future extension could be made include greater than or less than filter for number or other type specfic filter on certain fields.
