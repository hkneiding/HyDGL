from enum import Enum, auto


class QmTarget(Enum):

    '''Enum class for the different QM attributes to be used.'''

    # POLARISABILITY
    POLARISABILITY = auto()
    NORMALISED_POLARISABILITY = auto()

    # dispersion energy
    SVP_DISPERSION_ENERGY = auto()
    TZVP_DISPERSION_ENERGY = auto()

    # electronic energy
    SVP_ELECTRONIC_ENERGY = auto()
    TZVP_ELECTRONIC_ENERGY = auto()

    # dipole moment
    SVP_DIPOLE_MOMENT = auto()
    TZVP_DIPOLE_MOMENT = auto()

    # orbitals
    SVP_HOMO_ENERGY = auto()
    SVP_LUMO_ENERGY = auto()
    TZVP_HOMO_ENERGY = auto()
    TZVP_LUMO_ENERGY = auto()

    SVP_HOMO_LUMO_GAP = auto()
    TZVP_HOMO_LUMO_GAP = auto()

    # frequencies
    LOWEST_VIBRATIONAL_FREQUENCY = auto()
    HIGHEST_VIBRATIONAL_FREQUENCY = auto()

    # thermo chemistry
    HEAT_CAPACITY = auto()
    ENTROPY = auto()

    ZPE_CORRECTION = auto()
    ENTHALPY_ENERGY = auto()
    GIBBS_ENERGY = auto()
    ENTHALPY_ENERGY_CORRECTION = auto()
    GIBBS_ENERGY_CORRECTION = auto()

    # delta values
    DISPERSION_ENERGY_DELTA = auto()
    ELECTRONIC_ENERGY_DELTA = auto()
    DIPOLE_MOMENT_DELTA = auto()
    HOMO_LUMO_GAP_DELTA = auto()
