import math
from dataclasses import dataclass
from typing import Dict


# physical constants (SI)
elementary_charge = 1.602176634e-19  # elementary charge (C)
hbar = 1.054571817e-34  # reduced Planck constant (J·s)
c_light = 299792458  # speed of light (m/s)

# fine‑structure constant (dimensionless)
alpha = elementary_charge**2 / (4 * math.pi * hbar * c_light)

# approximate rest masses (kg) 
# quarks
mass_up = 2.213e-27
mass_down = 3.877e-27
mass_charm = 2.655e-27
mass_strange = 4.669e-27
mass_top = 3.677e-27
mass_bottom = 9.883e-27

# charged leptons
mass_electron = 9.10938356e-31
mass_muon = 1.883531627e-28
mass_tau = 3.16747e-27

# neutrinos (≈ massless, values are upper limits)
mass_neutrino_e = 1.8755e-36
mass_neutrino_mu = 2.0e-36
mass_neutrino_tau = 3.5e-36

# gauge bosons
mass_photon = 0.0
mass_gluon = 0.0
mass_w = 8.055e-26  # W± (same for both charges)
mass_z = 2.582e-25
mass_higgs = 1.0e-25
mass_graviton = 0.0  # hypothetical, massless

# helper constants
JOULE_PER_EV = 1.602176634e-19  # 1 eV = … J
KG_PER_AMU = 1.66053906660e-27  # 1 u (atomic mass unit) = … kg
EV_PER_MEV = 1.0e6  # 1 MeV = … eV


@dataclass(frozen=True)
class Particle:
    name: str  # readable name, e.g. 'electron'
    mass: float  # kg
    charge: float  # in units of e (elementary charge)
    spin: float  # ℏ/2 units (e.g. 0.5, 1.0, 2.0 …)
    kind: str  # 'quark', 'lepton' or 'boson'
    
    def rest_energy_joules(self):
        """Return the rest‑energy *E = m·c²* in joules."""
        return self.mass * c_light ** 2

    def rest_energy_electron_volts(self):
        """Return the rest‑energy in electron‑volts (eV)."""
        return self.rest_energy_joules() / JOULE_PER_EV

    def rest_energy_mev(self):
        """Return the rest‑energy in mega‑electron‑volts (MeV)."""
        return self.rest_energy_electron_volts() / EV_PER_MEV

    def mass_in_amu(self):
        """Return the particle mass in atomic mass units (u)."""
        return self.mass / KG_PER_AMU


particles: Dict[str, Particle] = {
    "up_quark": Particle("up_quark", mass_up, 2/3, 0.5, "quark"),
    "down_quark": Particle("down_quark", mass_down, -1/3, 0.5, "quark"),
    "charm_quark": Particle("charm_quark", mass_charm, 2/3, 0.5, "quark"),
    "strange_quark": Particle("strange_quark", mass_strange,-1/3, 0.5, "quark"),
    "top_quark": Particle("top_quark", mass_top, 2/3, 0.5, "quark"),
    "bottom_quark": Particle("bottom_quark", mass_bottom,-1/3, 0.5, "quark"),

    # charged leptons 
    "electron": Particle("electron", mass_electron, -1, 0.5, "lepton"),
    "muon": Particle("muon", mass_muon, -1, 0.5, "lepton"),
    "tau": Particle("tau", mass_tau, -1, 0.5, "lepton"),

    # neutrinos (≈ massless)
    "neutrino_e": Particle("neutrino_e", mass_neutrino_e, 0.0, 0.5, "lepton"),
    "neutrino_mu": Particle("neutrino_mu", mass_neutrino_mu, 0.0, 0.5, "lepton"),
    "neutrino_tau": Particle("neutrino_tau", mass_neutrino_tau, 0.0, 0.5, "lepton"),

    # gauge bosons
    "photon": Particle("photon", mass_photon, 0.0, 0.0, "boson"),
    "gluon": Particle("gluon", mass_gluon, 0.0, 1.0, "boson"),
    "w_plus": Particle("w_plus", mass_w, 1.0, 1.0, "boson"),
    "w_minus": Particle("w_minus", mass_w, -1.0, 1.0, "boson"),
    "z0": Particle("z0", mass_z, 0.0, 1.0, "boson"),
    "higgs": Particle("higgs", mass_higgs, 0.0, 0.0, "boson"),
    "graviton": Particle("graviton", mass_graviton, 0.0, 2.0, "boson"),
}

all_particle_names = []
for item in particles.values():
    print(item.name,'mass:',item.mass,'charge:',item.charge,'spin:',item.spin,'kind:',item.kind)
    all_particle_names.append(item.name)

for name in all_particle_names:
    p = particles[name]
    print(f"{name} rest energy (J):", p.rest_energy_joules())
    print(f"{name} rest energy (eV):", p.rest_energy_electron_volts())
    print(f"{name} rest energy (MeV):", p.rest_energy_mev())
    print(f"{name} mass (AMU):", p.mass_in_amu())
    print('\n')

