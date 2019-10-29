from data_collection.management.commands import BaseHalaroseCsvImporter


class Command(BaseHalaroseCsvImporter):
    council_id = "E07000118"
    addresses_name = (
        "parl.maybe/Version 1/chorley-polling_station_export-2019-09-16.csv"
    )
    stations_name = (
        "parl.maybe/Version 1/chorley-polling_station_export-2019-09-16.csv"
    )
    elections = ["parl.maybe"]
    allow_station_point_from_postcode = False

    def address_record_to_dict(self, record):
        rec = super().address_record_to_dict(record)
        uprn = record.uprn.strip().lstrip("0")

        # # This is a hotel which isn't in AddressBase, but which doesn't cause any harm if the record is left in.
        # # Leaving this as a comment in case it becomes useful again in future.
        # if record.housepostcode == "PR6 7ED":
        #     return None

        if uprn in [
            "100010362601",  # PR69NN -> PR69NW : 14 BABYLON LANE, ADLINGTON, CHORLEY, LANCASHIRE
            "100010367883",  # PR69LB -> PR69LJ : 6 CHORLEY ROAD, HEATH CHARNOCK, CHORLEY, LANCASHIRE
            "200004063697",  # PR68NT -> PR68NS : JACK GREEN COTTAGE, ORAM ROAD, BRINDLE, CHORLEY, LANCASHIRE
            "200004063671",  # PR50SD -> PR76ND : BRIDGE END COTTAGE, VALLEY ROAD, HOGHTON, PRESTON, LANCASHIRE
            "100012384782",  # PR60HT -> PR60HP : ST PETERS VICARAGE, HARPERS LANE, CHORLEY, LANCASHIRE
            "200004070947",  # PR72QL -> PR73QL : 2 PLYMOUTH COTTAGES, BIRKACRE ROAD
            "10002076206",  # PR67LB -> PR67LS : HILLSIDE COTTAGE, 1 NAYLORS FOLD HILL TOP LANE
            "100010385659",  # PR75DB -> PR75DE : THE BUNGALOW SPENDMORE LANE, COPPULL
            "10070372269",  # PR69AT -> PR269AT : SNOWDROP COTTAGE BANK HALL DRIVE, BRETHERTON
        ]:
            rec["accept_suggestion"] = True
        #
        # # just bin the UPRNs on these ones
        if uprn in [
            "10091495601",  # PR69RF -> PR60QF : GROVE FARM, RAILWAY ROAD, ADLINGTON, CHORLEY, LANCASHIRE
            "100010391254",  # PR75TW -> L402QN : 41 NEW STREET, ECCLESTON
            "100010391256",  # PR75TW -> L402QN : 43 NEW STREET, ECCLESTON
            "10070371313",  # L402QN -> PR75TW : 41 NEW STREET, MAWDESLEY, ORMSKIRK
            "10070371314",  # L402QN -> PR75TW : 43 NEW STREET, MAWDESLEY, ORMSKIRK
        ]:
            rec["accept_suggestion"] = False

        return rec
