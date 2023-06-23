CAN_VOLUME = 0.355
BOTTLE_VOLUME = 2.0
cansPerPack = 6
tVolume = cansPerPack * CAN_VOLUME
print("A six-pack of 12-ounce cans contains", tVolume, "liters.")
# Calculate total volume in the cans and a two-liter bottle.
tVolume = tVolume + BOTTLE_VOLUME
print("A six-pack and a two-liter bottle contain", tVolume, "liters.")
