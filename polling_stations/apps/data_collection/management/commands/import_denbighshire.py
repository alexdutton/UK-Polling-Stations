from data_collection.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "W06000004"
    addresses_name = "parl.maybe/Version 1/denbighshire-Democracy_Club__15October2019.tsv"
    stations_name = "parl.maybe/Version 1/denbighshire-Democracy_Club__15October2019.tsv"
    csv_delimiter = "\t"
    csv_encoding = "windows-1252"
    elections = ["parl.maybe"]
    allow_station_point_from_postcode = False

    def address_record_to_dict(self, record):
        rec = super().address_record_to_dict(record)

        # print(record)
        uprn = record.post_code.lstrip('0')

        if uprn in [
            "10023749403",  # LL210HN -> LL210HW : Bryn Ffynnon Bungalow, Corwen, Sir Ddinbych/Denbighshire
            "200004301825",  # LL165AF -> LL165UP : Plas Heaton Farm, Plas Chambres Road, Dinbych/Denbigh
            "10003926062"  # LL164BS -> LL164BY : Plaen Cottage, Waen, Bodfari, Dinbych/Denbigh
            "10023750314",   # LL170EW -> LL170EN : 21 Brenig, Eryl Hall Caravan Park, Lower Denbigh Road, …
            "10023752307",  # LL170EW -> LL170EN : 1 Conway, Eryl Hall Caravan Park, Lower Denbigh Road, …
            "100100946123",  # LL170BP -> LL170EP : Pen-Y-Bont, Allt Goch, Llanelwy/St Asaph
            "10023750424",  # LL170UR -> LL170TY : Annexe At Penisa`r Mynydd, Rhuallt, Llanelwy/St Asaph
            "200004315583",  # LL170EW -> LL170EH : 2 Poplar Cottage, Lower Denbigh Road, Llanelwy/St Asaph
            "10093589383",  # LL170HT -> LL170TH : Dolafon Lodge, Rhyl Road, Llanelwy/St Asaph
            "10012913875",  # LL198RL -> LL198LT : 1 Llys Isfryn, Ffordd Gallt Melyd/Meliden Road, Prestatyn
            "10091598193",  # LL184DY -> LL184QA : D 57 New Pines Caravan Park, Dyserth Road, Rhyl
            "10023752567",  # LL184DY -> LL184QJ : E 67 New Pines Caravan Park, Dyserth Road, Rhyl
            "10091598194",  # LL184DY -> LL184QA : E 82 New Pines Caravan Park, Dyserth Road, Rhyl
            "10091601258",  # LL184DY -> LL184QA : D 42 New Pines Caravan Park, Dyserth Road, Rhyl
            "100100946917",  # LL181PG -> LL181PH : Flat 1, 20 Aquarium Street, Rhyl
            "10091597812",  # LL151EE -> LL151SL : Wynne House Staff Flat, Ruthin School, Mold Road, Rhuthun/Ruthin
            "10023750202",  # LL152HS -> LL152AT : Orchard House, Clocaenog, Rhuthun/Ruthin
            "200004293591",  # CH74DE -> CH74DD : Ty Minffordd, Eryrys, Yr Wyddgrug/Mold
            "200001729468",  # CH75FD -> CH75SN : Ffrith Isaf, Ruthin Road, Llanferres, Yr Wyddgrug/Mold
        ]:
            rec['accept_suggestion'] = True

        return rec