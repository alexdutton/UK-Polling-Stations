from django.contrib.gis.geos import Point
from data_collection.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "E09000019"
    addresses_name = "europarl.2019-05-23/Version 1/islington.gov.uk-1557480923000-.TSV"
    stations_name = "europarl.2019-05-23/Version 1/islington.gov.uk-1557480923000-.TSV"
    elections = ["europarl.2019-05-23"]
    csv_delimiter = "\t"

    def address_record_to_dict(self, record):
        rec = super().address_record_to_dict(record)
        uprn = record.property_urn.strip().lstrip("0")

        # postcode corrections
        if uprn in ["10093623311", "10093623312", "10093623313"]:
            rec["postcode"] = "EC1M 5UD"
        if uprn == "10012788158":
            rec["postcode"] = "EC1V 0ET"

        if uprn in [
            "5300061815",  # N194PY -> N194PS : 105A Mercers Road, London
            "5300061816",  # N194PY -> N194PS : 105B Mercers Road, London
            "5300061817",  # N194PY -> N194PS : 105C Mercers Road, London
            "5300062775",  # N14NB -> N14NA : 75C Mildmay Park, London
            "5300086829",  # N12LL -> N12LJ : 222A St Paul`s Road, London
            "10012785747",  # N12LL -> N12LJ : 222B St Paul`s Road, London
            "10091006175",  # N51HP -> N52HP : Flat 17, 1A Petherton Road, London
            "5300002493",  # N79RB -> N70RB : Ground Floor Flat, 27 Anson Road, London
            "10091002258",  # N79RE -> N76RE : Ground Floor Flat, 115 Tollington Way, London
        ]:
            rec['accept_suggestion'] = True

        if uprn in [
            "5300031832",  # N193JS -> N13PB : 37 Harberton Road, London
            "5300050916",  # N195NJ -> N193QL : Flat 1, 1A Waterlow Road, London
            "5300050917",  # N195NJ -> N193QL : Flat 2, 1A Waterlow Road, London
            "5300050918",  # N195NJ -> N193QL : Flat 3, 1A Waterlow Road, London
            "10093624121",  # N195NJ -> N193QL : Flat 4, 1A Waterlow Road, London
            "5300082350",  # N194QN -> N195JS : Ground Floor Flat, 64 Shaftesbury Road, London
            "10012785703",  # N13NP -> N11EB : Basement Flat, 42 Ockendon Road, London
            "5300073507",  # EC1V0HN -> EC1V0HU : 16 Tompion Street, London
            "10091002696",  # N78RH -> N51TX : 73B Lough Road, London
            "10090262726",  # N17AD -> N18ED : Penthouse, 14-22 Coleman Fields, London

            # These all have the right postcode in the council data, but are wrong in AddressBase.
            "10023220854",  # N14AU -> N11AU : Flat 1, 34 Balls Pond Road, London
            "10023220855",  # N14AU -> N11AU : Flat 2, 34 Balls Pond Road, London
            "10023220856",  # N14AU -> N11AU : Flat 3, 34 Balls Pond Road, London
            "10023220857",  # N14AU -> N11AU : Flat 4, 34 Balls Pond Road, London
            "10023220858",  # N14AU -> N11AU : Flat 5, 34 Balls Pond Road, London
            "10023220859",  # N14AU -> N11AU : Flat 6, 34 Balls Pond Road, London
            "10093113360",  # N194EB -> N195SE : Ground Floor Flat, 410 Hornsey Road, London
            "10090548425",  # N79RP -> N79DQ : First Floor Flat, 494 Caledonian Road, London
            "10093113306",  # N70SH -> N70HS : Flat 6, 369 Camden Road, London
            "10091003209",  # N13PH -> N12PH : 3A City View Apartments, 207 Essex Road, London
            "10093113237",  # N18JF -> N18LT : Flat 4, 1 St Peter`s Street Mews, London

        ]:
            rec['accept_suggestion'] = False

        return rec

    def station_record_to_dict(self, record):
        rec = super().station_record_to_dict(record)

        # # Location corrections carried forward
        # if rec["internal_council_id"] == "1531":  #    St. Thomas` Church Hall
        #     rec["location"] = Point(-0.104049, 51.560139, srid=4326)
        # if rec["internal_council_id"] == "1519":  # St Joan of Arc Community Centre
        #     rec["location"] = Point(-0.0966823, 51.5559102, srid=4326)

        return rec
