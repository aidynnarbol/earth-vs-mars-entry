from entry_simulation import simulate_entry
from plots import plot_comparison, plot_deceleration

# Earth parameters
earth = simulate_entry(
    rho0=1.225,
    H=8500.0,
    g=9.81
)

# Mars parameters
mars = simulate_entry(
    rho0=0.020,
    H=11100.0,
    g=3.71
)

plot_comparison(earth, mars)
plot_deceleration(earth, mars)

print("Earth final speed:", earth["v"][-1])
print("Mars final speed:", mars["v"][-1])
