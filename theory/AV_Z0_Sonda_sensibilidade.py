import numpy as np
import matplotlib.pyplot as plt

# Dados reais atuais - 140h IXPE Magnetar 1E 1547.0-5408
# PD=0.556, chi2_QED=18.12/14, Delta=6.46 LIMITE
exposure_now = 140
delta_now = 6.46

exposures = np.array([140, 200, 300, 400, 500, 600, 800])
deltas = delta_now * (exposures / exposure_now)

plt.figure(figsize=(8,5))
plt.plot(exposures, deltas, 'o-', linewidth=2, label='Forecast Z0-unit k=8.45 Ohm, N=22')
plt.axhline(9, color='red', linestyle='--', linewidth=2, label='Limite 3 sigma Discovery (Delta>9)')
plt.axhline(6.46, color='gray', linestyle=':', label='Atual 140h Delta=6.46 LIMITE')
plt.axvline(140, color='gray', linestyle=':', alpha=0.5)
plt.axvline(500, color='blue', linestyle=':', alpha=0.5)
plt.scatter([500], [23.0], color='blue', s=150, zorder=5, label='Forecast 500h Delta=23.0')
plt.text(510, 23.5, '500h -> Delta=23.0\n>9 DISCOVERY se Z0=1', fontsize=9, color='blue', weight='bold')
plt.xlabel('Exposicao IXPE [horas]')
plt.ylabel('Delta chi2 = chi2_QED - chi2_AV')
plt.title('AETERNVM VACUVM v5.0 - Falsificabilidade Z0 como unidade\n1E 1547.0-5408 - PD=0.556 - S=280, k=8.45 Ohm')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('teoria_Z0_sensibilidade.png', dpi=200)
print(f"Atual: {exposure_now}h Delta={delta_now:.2f} LIMITE")
print(f"Forecast: 500h Delta={delta_now*500/exposure_now:.1f} >9 DISCOVERY")
