from django.contrib.gis.geos import Point
from data_collection.github_importer import BaseGitHubImporter


class Command(BaseGitHubImporter):

    srid = 4326
    districts_srid = 4326
    council_id = "E07000114"
    elections = ["parl.2019-12-12"]
    scraper_name = "wdiv-scrapers/DC-PollingStations-Thanet"
    geom_type = "geojson"

    def district_record_to_dict(self, record):
        poly = self.extract_geometry(record, self.geom_type, self.get_srid("districts"))
        return {
            "internal_council_id": record["Code"],
            "name": record["Name"] + " - " + record["Code"],
            "area": poly,
            "polling_station_id": record["Code"],
        }

    def station_record_to_dict(self, record):
        location = self.extract_geometry(
            record, self.geom_type, self.get_srid("stations")
        )
        codes = record["DISTRICT"].split("&")
        address = record["ADDRESS"]
        postcode = record["POSTCODE"]
        if postcode and postcode in address:
            address = address.replace(postcode, "").strip()

        stations = []
        for code in codes:

            # point supplied is bang on the building
            # but causes google directions API to give us a strange route
            if code == "MA" and address.startswith(
                "Christ Church United Reformed Church"
            ):
                location = Point(1.338154, 51.38301, srid=4326)

            stations.append(
                {
                    "internal_council_id": code.strip(),
                    "postcode": postcode,
                    "address": address,
                    "location": location,
                }
            )
        return stations
