from data_collection.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "E07000226"
    addresses_name = "parl.maybe/Version 1/crawley-Democracy_Club__15October2019.tsv"
    stations_name = "parl.maybe/Version 1/crawley-Democracy_Club__15October2019.tsv"
    elections = ["parl.maybe"]
    csv_delimiter = "\t"

    def station_record_to_dict(self, record):
        if record.polling_place_id == '795':  # Southgate West Community Centre
            record = record._replace(polling_place_uprn='100062475395', polling_place_easting='', polling_place_northing='')
        if record.polling_place_id == '789':  # Wakehams Green Community Centre
            record = record._replace(polling_place_uprn='200001230277', polling_place_easting='', polling_place_northing='',
                                     polling_place_postcode='RH10 3NU')
        if record.polling_place_id == '774':  # Furnace Green Community Centre
            record = record._replace(polling_place_uprn='100062615172', polling_place_easting='', polling_place_northing='',
                                     polling_place_postcode='RH10 6QZ')
        return super().station_record_to_dict(record)

    def address_record_to_dict(self, record):
        rec = super().address_record_to_dict(record)
        uprn = record.property_urn.strip().lstrip("0")

        # if record.addressline6 == "RH10 3HW":
        #     rec["postcode"] = "RH10 3GW"

        if uprn in [
            "10024122201"  # RH110EA -> RH110AE : 50A Ifield Drive, Ifield, Crawley
        ]:
            rec["accept_suggestion"] = True

        return rec
    #
    # def station_record_to_dict(self, record):
    #     if record.polling_place_id == "675":
    #         record = record._replace(polling_place_easting="526564")
    #         record = record._replace(polling_place_northing="135576")
    #     if record.polling_place_id == "692":
    #         record = record._replace(polling_place_easting="528408")
    #         record = record._replace(polling_place_northing="135808")
    #     return super().station_record_to_dict(record)
