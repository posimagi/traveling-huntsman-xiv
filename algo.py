import math


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from(self, other):
        return math.sqrt(math.pow(math.fabs(self.x - other.x), 2) +
                         math.pow(math.fabs(self.y - other.y), 2))


class Aetheryte:
    def __init__(self, name, location):
        self.name = name
        self.location = location


class Mark:
    def __init__(self, name):
        self.name = name
        self.location = Location(99.9, 99.9)

    def distance_from(self, other):
        return self.location.distance_from(other.location)


CASTRUM_ORIENS      = Aetheryte("Castrum Oriens",          Location( 8.8, 11.4))
PEERING_STONES      = Aetheryte("The Peering Stones",      Location(29.8, 26.4))
ALA_GANNHA          = Aetheryte("Ala Gannha",              Location(23.6,  6.6))
ALA_GHIRI           = Aetheryte("Ala Ghiri",               Location(16.0, 36.6))
PORTA_PRAETORIA     = Aetheryte("Porta Praetoria",         Location( 8.4, 21.2))
ALA_MHIGAN_QUARTER  = Aetheryte("The Ala Mhigan Quarter",  Location(33.7, 34.6))
TAMAMIZU            = Aetheryte("Tamamizu",                Location(28.6, 16.4))
ONOKORO             = Aetheryte("Onokoro",                 Location(23.2,  9.9))
NAMAI               = Aetheryte("Namai",                   Location(30.1, 19.8))
HOUSE_OF_THE_FIERCE = Aetheryte("The House of the Fierce", Location(26.3, 13.5))
REUNION             = Aetheryte("Reunion",                 Location(32.5, 28.4))
DAWN_THRONE         = Aetheryte("The Dawn Throne",         Location(23.0, 22.3))
DHORO_ILOH          = Aetheryte("Dhoro Iloh",              Location( 6.3, 23.9))
BOGUS_AETHERYTE     = Aetheryte("Unknown",                 Location(99.9, 99.9))

aetherytes = {
    "The Fringes":     [CASTRUM_ORIENS, PEERING_STONES],
    "The Peaks":       [ALA_GANNHA, ALA_GHIRI],
    "The Lochs":       [PORTA_PRAETORIA, ALA_MHIGAN_QUARTER],
    "The Ruby Sea":    [TAMAMIZU, ONOKORO],
    "Yanxia":          [NAMAI, HOUSE_OF_THE_FIERCE],
    "The Azim Steppe": [REUNION, DAWN_THRONE, DHORO_ILOH]
}

ERLE        = Mark("Erle")
ORCUS       = Mark("Orcus")
AQRABUAMELU = Mark("Aqrabuamelu")
VOCHSTEIN   = Mark("Vochstein")
LUMINARE    = Mark("Luminare")
MAHISHA     = Mark("Mahisha")
FUNA_YUREI  = Mark("Funa Yurei")
ONI_YUMEMI  = Mark("Oni Yumemi")
GAJASURA    = Mark("Gajasura")
ANGADA      = Mark("Angada")
SUM         = Mark("Sum")
GIRIMEKHALA = Mark("Girimekhala")
BOGUS_MARK  = Mark("None")

marks = {
    "The Fringes":     [ERLE, ORCUS],
    "The Peaks":       [AQRABUAMELU, VOCHSTEIN],
    "The Lochs":       [LUMINARE, MAHISHA],
    "The Ruby Sea":    [FUNA_YUREI, ONI_YUMEMI],
    "Yanxia":          [GAJASURA, ANGADA],
    "The Azim Steppe": [SUM, GIRIMEKHALA]
}


def main():
    plan = {}
    for zone in marks:
        nearest_aetheryte = BOGUS_AETHERYTE
        nearest_mark_to_aetheryte = BOGUS_MARK
        farther_mark_from_aetheryte = BOGUS_MARK
        for mark in marks[zone]:
            if mark.location is None:
                continue
            for aetheryte in aetherytes[zone]:
                if mark.distance_from(aetheryte) < mark.distance_from(nearest_aetheryte):
                    nearest_aetheryte = aetheryte
                    nearest_mark_to_aetheryte = mark
                    for other_mark in marks[zone]:
                        if other_mark.name != mark.name:
                            farther_mark_from_aetheryte = other_mark
                            break
        plan[zone] = [nearest_aetheryte.name, nearest_mark_to_aetheryte.name, farther_mark_from_aetheryte.name]
    return plan


if __name__ == "__main__":
    print main()
