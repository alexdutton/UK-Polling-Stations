from data_collection.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "E07000122"
    addresses_name = (
        "parl.2019-12-12/Version 1/Democracy_Club__12December2019pendle.tsv"
    )
    stations_name = "parl.2019-12-12/Version 1/Democracy_Club__12December2019pendle.tsv"
    elections = ["parl.2019-12-12"]
    csv_delimiter = "\t"
    allow_station_point_from_postcode = False

    def station_record_to_dict(self, record):
        if record.polling_place_id == "3538":
            # Rolls Royce Leisure
            record = record._replace(polling_place_postcode="BB18 6HJ")
        if record.polling_place_id == "3638":
            # New Life Christian Centre
            record = record._replace(polling_place_postcode="BB8 0HP")
        if record.polling_place_id == "3522":
            # Thomas Street Bowling Pavilion, Percy Street, Nelson
            record = record._replace(
                polling_place_postcode="BB9 9BZ",
                polling_place_northing=437261,
                polling_place_easting=386085,
            )

        return super().station_record_to_dict(record)
