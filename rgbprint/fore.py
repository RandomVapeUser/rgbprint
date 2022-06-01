from .supported_colors import SupportedColors
from .color import Color


__all__ = ["Fore", "supported_colors"]


class Fore:
    BLACK                   = Color(SupportedColors.BLACK.value)
    WHITE                   = Color(SupportedColors.WHITE.value)
    RED                     = Color(SupportedColors.RED.value)
    LIME                    = Color(SupportedColors.LIME.value)
    BLUE                    = Color(SupportedColors.BLUE.value)
    YELLOW                  = Color(SupportedColors.YELLOW.value)
    CYAN                    = Color(SupportedColors.CYAN.value)
    MAGENTA                 = Color(SupportedColors.MAGENTA.value)
    SILVER                  = Color(SupportedColors.SILVER.value)
    GRAY                    = Color(SupportedColors.GRAY.value)
    MAROON                  = Color(SupportedColors.MAROON.value)
    OLIVE                   = Color(SupportedColors.OLIVE.value)
    GREEN                   = Color(SupportedColors.GREEN.value)
    PURPLE                  = Color(SupportedColors.PURPLE.value)
    TEAL                    = Color(SupportedColors.TEAL.value)
    NAVY                    = Color(SupportedColors.NAVY.value)
    DARK_RED                = Color(SupportedColors.DARK_RED.value)
    BROWN                   = Color(SupportedColors.BROWN.value)
    FIREBRICK               = Color(SupportedColors.FIREBRICK.value)
    CRIMSON                 = Color(SupportedColors.CRIMSON.value)
    TOMATO                  = Color(SupportedColors.TOMATO.value)
    CORAL                   = Color(SupportedColors.CORAL.value)
    INDIAN_RED              = Color(SupportedColors.INDIAN_RED.value)
    LIGHT_CORAL             = Color(SupportedColors.LIGHT_CORAL.value)
    DARK_SALMON             = Color(SupportedColors.DARK_SALMON.value)
    SALMON                  = Color(SupportedColors.SALMON.value)
    LIGHT_SALMON            = Color(SupportedColors.LIGHT_SALMON.value)
    ORANGE_RED              = Color(SupportedColors.ORANGE_RED.value)
    DARK_ORANGE             = Color(SupportedColors.DARK_ORANGE.value)
    ORANGE                  = Color(SupportedColors.ORANGE.value)
    GOLD                    = Color(SupportedColors.GOLD.value)
    DARK_GOLDEN_ROD         = Color(SupportedColors.DARK_GOLDEN_ROD.value)
    GOLDEN_ROD              = Color(SupportedColors.GOLDEN_ROD.value)
    PALE_GOLDEN_ROD         = Color(SupportedColors.PALE_GOLDEN_ROD.value)
    DARK_KHAKI              = Color(SupportedColors.DARK_KHAKI.value)
    KHAKI                   = Color(SupportedColors.KHAKI.value)
    YELLOW_GREEN            = Color(SupportedColors.YELLOW_GREEN.value)
    DARK_OLIVE_GREEN        = Color(SupportedColors.DARK_OLIVE_GREEN.value)
    OLIVE_DRAB              = Color(SupportedColors.OLIVE_DRAB.value)
    LAWN_GREEN              = Color(SupportedColors.LAWN_GREEN.value)
    CHARTREUSE              = Color(SupportedColors.CHARTREUSE.value)
    GREEN_YELLOW            = Color(SupportedColors.GREEN_YELLOW.value)
    DARK_GREEN              = Color(SupportedColors.DARK_GREEN.value)
    FOREST_GREEN            = Color(SupportedColors.FOREST_GREEN.value)
    LIME_GREEN              = Color(SupportedColors.LIME_GREEN.value)
    LIGHT_GREEN             = Color(SupportedColors.LIGHT_GREEN.value)
    PALE_GREEN              = Color(SupportedColors.PALE_GREEN.value)
    DARK_SEA_GREEN          = Color(SupportedColors.DARK_SEA_GREEN.value)
    MEDIUM_SPRING_GREEN     = Color(SupportedColors.MEDIUM_SPRING_GREEN.value)
    SPRING_GREEN            = Color(SupportedColors.SPRING_GREEN.value)
    SEA_GREEN               = Color(SupportedColors.SEA_GREEN.value)
    MEDIUM_AQUA_MARINE      = Color(SupportedColors.MEDIUM_AQUA_MARINE.value)
    MEDIUM_SEA_GREEN        = Color(SupportedColors.MEDIUM_SEA_GREEN.value)
    LIGHT_SEA_GREEN         = Color(SupportedColors.LIGHT_SEA_GREEN.value)
    DARK_SLATE_GRAY         = Color(SupportedColors.DARK_SLATE_GRAY.value)
    DARK_CYAN               = Color(SupportedColors.DARK_CYAN.value)
    AQUA                    = Color(SupportedColors.AQUA.value)
    LIGHT_CYAN              = Color(SupportedColors.LIGHT_CYAN.value)
    DARK_TURQUOISE          = Color(SupportedColors.DARK_TURQUOISE.value)
    TURQUOISE               = Color(SupportedColors.TURQUOISE.value)
    MEDIUM_TURQUOISE        = Color(SupportedColors.MEDIUM_TURQUOISE.value)
    PALE_TURQUOISE          = Color(SupportedColors.PALE_TURQUOISE.value)
    AQUA_MARINE             = Color(SupportedColors.AQUA_MARINE.value)
    POWDER_BLUE             = Color(SupportedColors.POWDER_BLUE.value)
    CADET_BLUE              = Color(SupportedColors.CADET_BLUE.value)
    STEEL_BLUE              = Color(SupportedColors.STEEL_BLUE.value)
    CORN_FLOWER_BLUE        = Color(SupportedColors.CORN_FLOWER_BLUE.value)
    DEEP_SKY_BLUE           = Color(SupportedColors.DEEP_SKY_BLUE.value)
    DODGER_BLUE             = Color(SupportedColors.DODGER_BLUE.value)
    LIGHT_BLUE              = Color(SupportedColors.LIGHT_BLUE.value)
    SKY_BLUE                = Color(SupportedColors.SKY_BLUE.value)
    LIGHT_SKY_BLUE          = Color(SupportedColors.LIGHT_SKY_BLUE.value)
    MIDNIGHT_BLUE           = Color(SupportedColors.MIDNIGHT_BLUE.value)
    DARK_BLUE               = Color(SupportedColors.DARK_BLUE.value)
    MEDIUM_BLUE             = Color(SupportedColors.MEDIUM_BLUE.value)
    ROYAL_BLUE              = Color(SupportedColors.ROYAL_BLUE.value)
    BLUE_VIOLET             = Color(SupportedColors.BLUE_VIOLET.value)
    INDIGO                  = Color(SupportedColors.INDIGO.value)
    DARK_SLATE_BLUE         = Color(SupportedColors.DARK_SLATE_BLUE.value)
    SLATE_BLUE              = Color(SupportedColors.SLATE_BLUE.value)
    MEDIUM_SLATE_BLUE       = Color(SupportedColors.MEDIUM_SLATE_BLUE.value)
    MEDIUM_PURPLE           = Color(SupportedColors.MEDIUM_PURPLE.value)
    DARK_MAGENTA            = Color(SupportedColors.DARK_MAGENTA.value)
    DARK_VIOLET             = Color(SupportedColors.DARK_VIOLET.value)
    DARK_ORCHID             = Color(SupportedColors.DARK_ORCHID.value)
    MEDIUM_ORCHID           = Color(SupportedColors.MEDIUM_ORCHID.value)
    THISTLE                 = Color(SupportedColors.THISTLE.value)
    PLUM                    = Color(SupportedColors.PLUM.value)
    VIOLET                  = Color(SupportedColors.VIOLET.value)
    ORCHID                  = Color(SupportedColors.ORCHID.value)
    MEDIUM_VIOLET_RED       = Color(SupportedColors.MEDIUM_VIOLET_RED.value)
    PALE_VIOLET_RED         = Color(SupportedColors.PALE_VIOLET_RED.value)
    DEEP_PINK               = Color(SupportedColors.DEEP_PINK.value)
    HOT_PINK                = Color(SupportedColors.HOT_PINK.value)
    LIGHT_PINK              = Color(SupportedColors.LIGHT_PINK.value)
    PINK                    = Color(SupportedColors.PINK.value)
    ANTIQUE_WHITE           = Color(SupportedColors.ANTIQUE_WHITE.value)
    BEIGE                   = Color(SupportedColors.BEIGE.value)
    BISQUE                  = Color(SupportedColors.BISQUE.value)
    BLANCHED_ALMOND         = Color(SupportedColors.BLANCHED_ALMOND.value)
    WHEAT                   = Color(SupportedColors.WHEAT.value)
    CORN_SILK               = Color(SupportedColors.CORN_SILK.value)
    LEMON_CHIFFON           = Color(SupportedColors.LEMON_CHIFFON.value)
    LIGHT_GOLDEN_ROD_YELLOW = Color(SupportedColors.LIGHT_GOLDEN_ROD_YELLOW.value)
    LIGHT_YELLOW            = Color(SupportedColors.LIGHT_YELLOW.value)
    SADDLE_BROWN            = Color(SupportedColors.SADDLE_BROWN.value)
    SIENNA                  = Color(SupportedColors.SIENNA.value)
    CHOCOLATE               = Color(SupportedColors.CHOCOLATE.value)
    PERU                    = Color(SupportedColors.PERU.value)
    SANDY_BROWN             = Color(SupportedColors.SANDY_BROWN.value)
    BURLY_WOOD              = Color(SupportedColors.BURLY_WOOD.value)
    TAN                     = Color(SupportedColors.TAN.value)
    ROSY_BROWN              = Color(SupportedColors.ROSY_BROWN.value)
    MOCCASIN                = Color(SupportedColors.MOCCASIN.value)
    NAVAJO_WHITE            = Color(SupportedColors.NAVAJO_WHITE.value)
    PEACH_PUFF              = Color(SupportedColors.PEACH_PUFF.value)
    MISTY_ROSE              = Color(SupportedColors.MISTY_ROSE.value)
    LAVENDER_BLUSH          = Color(SupportedColors.LAVENDER_BLUSH.value)
    LINEN                   = Color(SupportedColors.LINEN.value)
    OLD_LACE                = Color(SupportedColors.OLD_LACE.value)
    PAPAYA_WHIP             = Color(SupportedColors.PAPAYA_WHIP.value)
    SEA_SHELL               = Color(SupportedColors.SEA_SHELL.value)
    MINT_CREAM              = Color(SupportedColors.MINT_CREAM.value)
    SLATE_GRAY              = Color(SupportedColors.SLATE_GRAY.value)
    LIGHT_SLATE_GRAY        = Color(SupportedColors.LIGHT_SLATE_GRAY.value)
    LIGHT_STEEL_BLUE        = Color(SupportedColors.LIGHT_STEEL_BLUE.value)
    LAVENDER                = Color(SupportedColors.LAVENDER.value)
    FLORAL_WHITE            = Color(SupportedColors.FLORAL_WHITE.value)
    ALICE_BLUE              = Color(SupportedColors.ALICE_BLUE.value)
    GHOST_WHITE             = Color(SupportedColors.GHOST_WHITE.value)
    HONEYDEW                = Color(SupportedColors.HONEYDEW.value)
    IVORY                   = Color(SupportedColors.IVORY.value)
    AZURE                   = Color(SupportedColors.AZURE.value)
    SNOW                    = Color(SupportedColors.SNOW.value)
    DIM_GRAY                = Color(SupportedColors.DIM_GRAY.value)
    DARK_GRAY               = Color(SupportedColors.DARK_GRAY.value)
    LIGHT_GRAY              = Color(SupportedColors.LIGHT_GRAY.value)
    GAINSBORO               = Color(SupportedColors.GAINSBORO.value)
    WHITE_SMOKE             = Color(SupportedColors.WHITE_SMOKE.value)

    RESET                   = "\033[0m"
