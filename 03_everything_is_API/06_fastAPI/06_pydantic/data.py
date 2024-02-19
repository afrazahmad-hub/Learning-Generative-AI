from model import Ahmad_family

_family: list[Ahmad_family] = [
     Ahmad_family(
        name = "Afraz Ahmad",
        age = 34,
        phone = 32158,
        education = "P.Graduate",
        currently_residing = "Islamabad",
        aka = "Afraz",
    ),
    Ahmad_family(
        name = "Fahad Ahmad",
        age = 28,
        phone = 32177,
        education = "Diploma",
        currently_residing = "France",
        aka = "Fahad",
    ),
    Ahmad_family(
        name = "Hammad Ahmad",
        age = 22,
        phone = 31258,
        education = "HSC",
        currently_residing = "Gujrat",
        aka = "Hammad",
    )
]

def get_member() -> list[Ahmad_family]:
    return _family
   