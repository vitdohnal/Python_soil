# PSP_basicProperties
from __future__ import print_function, division


def computePorosity(bulkDensity, gravWaterContent):
    """Compute basic soil porosity and water-content properties.

    Parameters
    ----------
    bulkDensity : float
        Soil bulk density [kg/m^3].
    gravWaterContent : float
        Gravimetric water content [kg/kg].
    """

    # Density of water and soil particles [kg/m^3]
    waterDensity = 1000
    particleDensity = 2650

    # Fraction of the total soil volume occupied by pores
    porosity = 1 - (bulkDensity / particleDensity)

    # Ratio between pore volume and solid volume
    voidRatio = porosity / (1 - porosity)

    # Convert gravimetric water content to volumetric water content
    waterContent = gravWaterContent * (bulkDensity / waterDensity)

    # Fraction of soil volume occupied by air
    gasPorosity = porosity - waterContent

    # Fraction of pore space filled with water
    degreeSaturation = waterContent / porosity

    print("\nTotal porosity [m^3/m^3] = ", format(porosity, ".3f"))
    print("Void ratio [m^3/m^3] = ", format(voidRatio, ".3f"))
    print("Volumetric water content [m^3/m^3] = ", format(waterContent, ".3f"))
    print("Gas filled porosity [m^3/m^3] = ", format(gasPorosity, ".3f"))
    print("Degree of saturation [-] =", format(degreeSaturation, ".3f"))


def computeSaturationWetness(bulkDensity):
    """Compute gravimetric water content corresponding to saturation."""

    waterDensity = 1000
    particleDensity = 2650

    # Calculate total soil porosity
    porosity = 1 - (bulkDensity / particleDensity)

    # Convert saturated volumetric water content (porosity)
    # to gravimetric water content
    return porosity / (bulkDensity / waterDensity)


def main():
    """Read user input, validate it, and calculate soil properties."""

    bulkDensity = float(input("Enter bulk density [kg/m^3]: "))
    gravWaterContent = float(
        input("Enter gravimetric water content [kg/kg]: ")
    )

    # Maximum possible gravimetric water content at saturation
    satMassWetness = computeSaturationWetness(bulkDensity)

    # Water content must be non-negative and below saturation
    if 0 <= gravWaterContent < satMassWetness:
        computePorosity(bulkDensity, gravWaterContent)
    else:
        print(
            "Wrong Water Content! value at saturation = ",
            satMassWetness
        )


if __name__ == "__main__":
    main()