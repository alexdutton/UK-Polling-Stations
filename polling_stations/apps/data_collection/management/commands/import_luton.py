from data_collection.management.commands import BaseDemocracyCountsCsvImporter


class Command(BaseDemocracyCountsCsvImporter):
    council_id = "E06000032"
    addresses_name = "parl.maybe/Version 1/luton-DC - Polling Districts.csv"
    stations_name = "parl.maybe/Version 1/luton-DC - Polling Stations.csv"
    elections = ["parl.maybe"]
    csv_encoding = "windows-1252"

    def address_record_to_dict(self, record):
        rec = super().address_record_to_dict(record)
        uprn = record.uprn.strip().lstrip("0")

        if uprn == "10001037360":
            rec["postcode"] = "LU2 7QG"
            rec["accept_suggestion"] = False

        if uprn == '200003278390':
            rec['postcode'] = "LU2 0TQ"
            rec['accept_suggestion'] = False

        if uprn == '10004923705':
            rec['postcode'] = "LU4 8NP"
            rec['accept_suggestion'] = False

        if uprn == '100081194537':
            rec['postcode'] = "LU4 8LT"
            rec['accept_suggestion'] = False

        if uprn == '10001037743':
            rec['postcode'] = 'LU1 3UB'
            rec['accept_suggestion'] = False

        if uprn in [
            "200003273279",  # LU31TL -> LU27AU : SCHOOL HOUSE BARNFIELD COLLEGE, BARNFIELD AVENUE, LUTON
        ]:
            rec["accept_suggestion"] = True

        return rec
