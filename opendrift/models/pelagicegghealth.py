from opendrift.models.pelagicegg import PelagicEggDrift, Lagrangian3DArray
import numpy as np


class PelagicEggHealth(Lagrangian3DArray):
    """
    Extending PelagicEgg with health property
    """

    variables = Lagrangian3DArray.add_variables([
        ('diameter', {'dtype': np.float32,
                      'units': 'm',
                      'default': 0.0014}),  # for NEA Cod
        ('neutral_buoyancy_salinity', {'dtype': np.float32,
                                       'units': '[]',
                                       'default': 31.25}),  # for NEA Cod
        ('density', {'dtype': np.float32,
                     'units': 'kg/m^3',
                     'default': 1028.}),
        ('hatched', {'dtype': np.float32,
                     'units': '',
                     'default': 0.}),
        ('health', {'dtype': np.float32,
                     'units': '',
                     'default': 100.})])


class PelagicEggHealthDrift(PelagicEggDrift):

    ElementType = PelagicEggHealth
    required_variables = {
    'x_sea_water_velocity': {'fallback': 0},
    'y_sea_water_velocity': {'fallback': 0},
    'sea_surface_height': {'fallback': 0},
    'sea_surface_wave_significant_height': {'fallback': 0},
    'sea_ice_area_fraction': {'fallback': 0},
    'x_wind': {'fallback': 0},
    'y_wind': {'fallback': 0},
    'land_binary_mask': {'fallback': None},
    'sea_floor_depth_below_sea_level': {'fallback': 100},
    'ocean_vertical_diffusivity': {'fallback': 0.02, 'profiles': True},
    'ocean_mixed_layer_thickness': {'fallback': 50},
    'sea_water_temperature': {'fallback': 10, 'profiles': True},
    'sea_water_salinity': {'fallback': 34, 'profiles': True},
    'surface_downward_x_stress': {'fallback': 0},
    'surface_downward_y_stress': {'fallback': 0},
    'turbulent_kinetic_energy': {'fallback': 0},
    'turbulent_generic_length_scale': {'fallback': 0},
    'upward_sea_water_velocity': {'fallback': 0},
    }


    # Default colors for plotting
    status_colors = {'initial': 'green', 'active': 'blue',
                     'hatched': 'red', 'eaten': 'yellow', 'died': 'magenta'}

    def __init__(self, *args, **kwargs):

        # Calling general constructor of parent class
        super(PelagicEggDrift, self).__init__(*args, **kwargs)