import numpy as np

# Vehicle parameters (same for Earth and Mars)
MASS = 3000.0       # kg
CD = 1.5
AREA = 12.0         # m^2

# Entry conditions
H0 = 120_000.0      # m
V0 = 6000.0         # m/s
DT = 0.05           # s
T_MAX = 500.0       # s


def rho_exponential(h, rho0, H):
    return rho0 * np.exp(-h / H)


def simulate_entry(rho0, H, g):
    h = H0
    v = V0
    t = 0.0

    history = {
        "t": [],
        "h": [],
        "v": [],
        "a": []
    }

    while h > 0 and t < T_MAX:
        rho = rho_exponential(h, rho0, H)
        drag = 0.5 * rho * v**2 * CD * AREA
        a = -drag / MASS - g

        v += a * DT
        h += v * DT

        history["t"].append(t)
        history["h"].append(h)
        history["v"].append(v)
        history["a"].append(a)

        t += DT

    for k in history:
        history[k] = np.array(history[k])

    return history
