from data_collection.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "E07000225"
    addresses_name = "parl.maybe/Version 1/chichester-Democracy_Club__15October2019.tsv"
    stations_name = "parl.maybe/Version 1/chichester-Democracy_Club__15October2019.tsv"
    elections = ["parl.maybe"]
    csv_delimiter = "\t"

    allow_station_point_from_postcode = False

    def station_record_to_dict(self, record):
        if record.polling_place_name == '2978':  # Rake Village Hall; wrong postcode
            record = record._replace(polling_place_postcode='GU33 7JA')  # still outside district, but legit
        return super().station_record_to_dict(record)

    def address_record_to_dict(self, record):
        if record.post_code in [
            'PO20 8SP',
            'PO19 7UD',
            'PO19 7BB',
            'PO18 8FT',
        ]:
            return None  # These look to be in another polling district, so unsure

        rec = super().address_record_to_dict(record)
        uprn = record.property_urn.strip().lstrip("0")

        if uprn in [
            "10002466508",  # GU84TA -> GU84SX : The Lodge, Shillinglee, Chiddingfold, Godalming
            "10002469418",  # GU273NG -> GU273NE : The Old School, Linchmere, Haslemere
            "10002469481",  # GU273PT -> GU273PS : Fern Owls, Marley Common, Haslemere
            "10002471049",  # GU273HG -> GU273HQ : Verdley Hill House, Henley Hill, Henley, Haslemere
            "10002471776",  # GU290DL -> GU290DH : The Rectory, Heyshott, Midhurst
            "10002473175",  # PO207BZ -> PO207DA : Rideau Cottage, Shipton Green, Itchenor, Chichester
            "10002474152",  # PO180QA -> PO180QB : 2 Parks Cottages, Goodwood, Chichester
            "10002474153",  # PO180QA -> PO180QB : 3 Parks Cottages, Goodwood, Chichester
            "10002482519",  # GU315BU -> GU315EB : The Log Cabin Fyning Hill, Rogate, Petersfield
            "100061736996",  # PO208EB -> PO208AA : Buckleberries, 11 Cakeham Road, West Wittering, Chichester
            "100061750085",  # PO188QG -> PO188RQ : Fairview, Priors Leaze Lane, Hambrook, Chichester
            "100062185216",  # PO188QG -> PO188RQ : Fairsend (Winter Quarters), Priors Leaze Lane, Hambrook, Chichester
            "10008886679",  # PO197BB -> PO197JR : Suite 848, 26 The Hornet, Chichester
            "200001740904",  # GU299QT -> GU299QJ : Pitsham Place, Pitsham, Midhurst
            "200002892282",  # PO188QG -> PO188RQ : Hower Place (Winter Quarters), Priors Leaze Lane, Hambrook, Chichester
        ]:
            rec["accept_suggestion"] = True

        if uprn in [
            "10014108090",  # GU273NQ -> GU273NG : Rose Cottage Linchmere Marsh, Linchmere, Haslemere
            "100062416341",  # PO209DR -> PO209EL : 10 Granada, Selsey Country Club, Golf Links Lane, Selsey, Chichester
            "100062416343",  # PO209DR -> PO209EL : 12 Granada, Selsey Country Club, Golf Links Lane, Selsey, Chichester
            "100062186194",  # PO197QL -> PO197HN : Over the Way, Westhampnett Road, Chichester
        ]:
            rec["accept_suggestion"] = False

        return rec
