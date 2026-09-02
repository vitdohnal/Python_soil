# PSP_basicProperties
from __future__ import print_function, division

def computePorosity(bulkDensity, gravWaterContent):
    waterDensity = 1000
    particleDensity = 2650
    porosity = 1- (bulkDensity / particleDensity)
    voidRatio = porosity / (1- porosity)
    waterContent = gravWaterContent * (bulkDensity / waterDensity)
    gasPorosity = porosity- waterContent
    degreeSaturation = waterContent / porosity
    print ("\nTotal porosity [m^3/m^3] = ",format
        (porosity, '.3f'))
    print ("Void ratio [m^3/m^3] = ", format
        (voidRatio, '.3f'))
    print ("Volumetric water content [m^3/m^3] = ", format
        (waterContent, '.3f'))
    print("Gas filled porosity [m^3/m^3] = ", format
        (gasPorosity, '.3f'))
    print("Degree of saturation [-] =", format
        (degreeSaturation, '.3f'))
    return

def computeStaturationWettness(bulkDensity):
    waterDensity = 1000
    particleDensity = 2650
    porosity = 1- (bulkDensity / particleDensity)
    return (porosity / (bulkDensity / waterDensity))
def main():
    bulkDensity = float(input("Enter bulk density [m^3/m^3]: "))
    gravWaterContent = float(input("Enter gravity water content ""[kg/kg]: "))
    satMassWettness = computeStaturationWettness(bulkDensity)
    if (gravWaterContent >= 0) and (gravWaterContent < satMassWettness):
        computePorosity(bulkDensity, gravWaterContent)
    else:
        print("Wrong Water Content! value at saturation = ", satMassWettness)
main()
