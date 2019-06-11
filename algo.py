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


CASTRUM_ORIENS      = Aetheryte("Castrum Oriens",                    Location( 8.8, 11.4))
PEERING_STONES      = Aetheryte("The Peering Stones",                Location(29.8, 26.4))
RHALGRS_FRINGES     = Aetheryte("Rhalgr's Reach (Fringes Gate)",     Location(34.2,  8.7))  # see assumptions below
RHALGRS_PEAKS       = Aetheryte("Rhalgr's Reach (Peaks Gate)",       Location( 4.2,  3.6))  # see assumptions below
ALA_GANNHA          = Aetheryte("Ala Gannha",                        Location(23.6,  6.6))
ALA_GHIRI           = Aetheryte("Ala Ghiri",                         Location(16.0, 36.6))
PORTA_PRAETORIA     = Aetheryte("Porta Praetoria",                   Location( 8.4, 21.2))
ALA_MHIGAN_QUARTER  = Aetheryte("The Ala Mhigan Quarter",            Location(33.7, 34.6))
TAMAMIZU            = Aetheryte("Tamamizu",                          Location(28.6, 16.4))
ONOKORO             = Aetheryte("Onokoro",                           Location(23.2,  9.9))
ONOKORO_FERRY       = Aetheryte("Onokoro (Ferry)",                   Location(41.4, 43.2))  # see assumptions below
NAMAI               = Aetheryte("Namai",                             Location(30.1, 19.8))
HOUSE_OF_THE_FIERCE = Aetheryte("The House of the Fierce",           Location(26.3, 13.5))
DOMAN_ENCLAVE       = Aetheryte("The Doman Enclave (The One River)", Location( 8.4, 35.6))  # see assumptions below
REUNION             = Aetheryte("Reunion",                           Location(32.5, 28.4))
DAWN_THRONE         = Aetheryte("The Dawn Throne",                   Location(23.0, 22.3))
DHORO_ILOH          = Aetheryte("Dhoro Iloh",                        Location( 6.3, 23.9))
BOGUS_AETHERYTE     = Aetheryte("Unknown",                           Location(99.9, 99.9))

# Doman Enclave assumptions:
# # Aethernet to The One River
# # Zone + mount time: 12 seconds
# # Yanxia flight speed: 2.5 seconds per unit
# # Actual entry point to Yanxia: (11.7, 32.2)

# Rhalgr's Reach (The Fringes) assumptions:
# # Aethernet to Fringes Gate
# # Zone + mount time: 12 seconds
# # The Fringes flight speed: 2.5 seconds per unit
# # Actual entry point to The Fringes: (29.9, 10.8)

# Rhalgr's Reach (The Peaks) assumptions:
# # Aethernet to Peaks Gate
# # Zone + mount time: 12 seconds
# # The Peaks flight speed: 2.5 seconds per unit
# # Actual entry point to The Peaks: (8.5, 5.7)

# Onokoro (Ferry) assumptions:
# # Zone + walk to Confederate Skipper + load time: 25 seconds
# # The Ruby Sea flight speed: 2.5 seconds per unit
# # Actual entry point to The Ruby Sea: 23.1. 9.9
# # Actual landing point from Ferry: 32.7, 38.2


aetherytes = {
    "The Fringes":     [CASTRUM_ORIENS, PEERING_STONES, RHALGRS_FRINGES],
    "The Peaks":       [ALA_GANNHA, ALA_GHIRI, RHALGRS_PEAKS],
    "The Lochs":       [PORTA_PRAETORIA, ALA_MHIGAN_QUARTER],
    "The Ruby Sea":    [TAMAMIZU, ONOKORO, ONOKORO_FERRY],
    "Yanxia":          [NAMAI, HOUSE_OF_THE_FIERCE, DOMAN_ENCLAVE],
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
