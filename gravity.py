import numpy as np

"""

This script is to generate correct number based on true physics.

For fiction and imagination.

For gravity related stuff

All units are SI unless otherwise specified.

"""

# Constant of Gravity
G=6.67*10E-11

def verbose_logger(log, verbose):
    if verbose:
        print(log)


def mass_volume_calculator(diameter, density, verbose=False):
    volume = np.pi*(diameter/2)**3*4/3
    verbose_logger("Volume of the object is {:,} cubic meters".format(volume), verbose)
    mass = volume * density
    verbose_logger("Mass of the object is {:,} metric tonnes".format(mass/1000), verbose)
    return mass, volume


def g_calculator(diameter, density, verbose=False):
    """
    diameter: meters
    density: kg/(meters**)
    result: g on the surface of such sphere.
    """
    mass, _ = mass_volume_calculator(diameter, density, verbose=verbose)
    g = mass*G/(diameter/2)**2
    verbose_logger("Surface Acceleration on this object is {} m/s".format(g), verbose)
    return g


def escape_velocity(diameter, density, verbose=False):
    mass, _ = mass_volume_calculator(diameter, density, verbose=verbose)
    escape_v = (4*G*mass/diameter)**0.5
    verbose_logger("Escape velocity of this object is {} m/s".format(escape_v), verbose)
    return escape_v


def orbital_velocity(mass, orbit_radius, verbose=False):
    orbit_v = G*mass/orbit_radius
    verbose_logger("Orbital period of this object at {} meter distance from center of object is {} m/s".format(orbit_radius, orbit_v), verbose)
    return orbit_v
