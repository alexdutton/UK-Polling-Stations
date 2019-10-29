from data_collection.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "E07000131"
    addresses_name = (
        "parl.maybe/Version 1/harborough-Democracy_Club__15October2019.tsv"
    )
    stations_name = (
        "parl.maybe/Version 1/harborough-Democracy_Club__15October2019.tsv"
    )
    elections = ["parl.maybe"]
    csv_delimiter = "\t"

    def station_record_to_dict(self, record):
        station_uprns = {
            '5110': '100032073908',  # Broughton Astley Village Hall (Main Hall)
            '4924': '200003742088',  # Meadowdale Primary School
            # '5029': '',  # Bruntingthorpe Vilalge Hall
        }
        if record.polling_place_id in station_uprns:
            record = record._replace(polling_place_uprn=station_uprns[record.polling_place_id])

        if record.polling_place_id == '4949':
            record = record._replace(polling_place_postcode='LE7 9FL')

        return super().station_record_to_dict(record)

    def address_record_to_dict(self, record):
        rec = super().address_record_to_dict(record)
        uprn = record.property_urn.strip().lstrip("0")

        if uprn == "200003741884":
            rec["postcode"] = "LE14 2QY"

        if uprn == '10093549892':
            return None  # UPRN/address confusion; removing means both affected postcodes return correct results

        if (
            record.addressline1.strip() == "69 Main Street"
            and record.addressline2.strip() == "Great Bowden"
            and record.addressline3.strip() == "Market Harborough, Leics"
        ):
            rec["postcode"] = "LE16 7HD"
            rec["accept_suggestion"] = False

        if uprn in [
            "100030474314",  # LE79DE -> LE79DP : Grange Barn, Loddington Road, Tilton on the Hill, Leicester
            "100030474315",  # LE79DE -> LE79DP : Grange Yard, Loddington Road, Tilton on the Hill, Leicester
            "200003741317",  # LE79DE -> LE79DP : Robin A Tiptoe Farm, Loddington Road, Tilton on the Hill, Leicester
            "200003742237",  # LE79XE -> LE79XB : Ash Tree Cottage, Launde Road, Loddington, Leicester
            "100030477785",  # LE96PU -> LE96PW : 102 Station Road, Broughton Astley, Leics
            "10093549578",  # LE169FR -> LE176PU : 19 Marsh Drive, Husbands Bosworth, Leics
            "10093551803",  # LE79EX -> LE79LX : 1 Stacey Avenue, Houghton on the Hill, Leicester
        ]:
            rec["accept_suggestion"] = True

        if uprn in [
            "200003741417",  # LE79YE -> LE79FN : Park Farm, Uppingham Road, Skeffington, Leicester
            "200003737159",  # LE175EA -> LE175RA : Hillcrest Farm, Frolesworth Road, Leire, Lutterworth, Leics
            "200003737160",  # LE175EA -> LE175RA : Mount Pleasant, Frolesworth Road, Leire, Lutterworth, Leics
            "100032072508",  # LE88AQ -> LE88AN : Wayside, Arnesby Road, Fleckney, Leicestershire
            "100030493011",  # LE167SZ -> LE167SX : The Old Rectory, Stonton Road, Church Langton, Market Harborough, Leics
            "200003739029",  # LE167RU -> LE167RT : Hunters Lodge, Main Street, Gumley, Market Harborough, Leics
            "100030480043",  # LE174RU -> LE174RX : Toll Gate Cottage, Bitteswell Road, Lutterworth, Leics
            "10034458557",  # LE175LE -> LE174LE : The Milking Parlour Boston Lodge, Lutterworth Road, Gilmorton, Lutterworth, Leics
            "200003744797",  # LE175PL -> LE175RZ : Ewe Cottage Gilmorton Lodge, Kimcote Road, Gilmorton, Lutterworth, Leics
        #     "100030493741",  # LE167TT -> LE167TX : Birchtree Farm, Welham Road, Thorpe Langton, Leics
            "200003742100",  # LE174LH -> LE174LR : The Mere, Mere Road, Bitteswell, Lutterworth, Leics
            "200003741377",  # LE79XL -> LE79XJ : 3 Fiddlers Green, Uppingham Road, East Norton, Leicester
            "200003741379",  # LE79XL -> LE79XJ : 2 Fiddlers Green, Uppingham Road, East Norton, Leicester
            "200003741382",  # LE79XL -> LE79XJ : 1 Fiddlers Green, Uppingham Road, East Norton, Leicester
        ]:
            rec["accept_suggestion"] = False

        return rec
