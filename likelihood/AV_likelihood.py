import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

# Carrega dado REAL do magnetar - caminho relativo ao repo
df = pd.read_csv('data/rvm_params_1e1547_15bins.csv')
phi = df['phase'].values
PD = df['PD'].values
PD_err = df['PD_err'].values
PA = df['PA'].values

# Prova 2: Teste A
PD_mean = np.average(PD, weights=1/PD_err**2)
chi2_qed = np.sum(((PD-PD_mean)/PD_err)**2)
print(f"[PROVA 2 - Magnetar 1E 1547.0-5408]")
print(f"PD weighted mean = {PD_mean:.3f}")
print(f"chi2 QED (const) = {chi2_qed:.2f} / {len(PD)-1} dof = {chi2_qed/(len(PD)-1):.2f}")

def pd_av_model(phi, pd0, c1):
    return pd0 + c1*np.sin(2*np.pi*phi)

popt,_ = curve_fit(pd_av_model, phi, PD, sigma=PD_err, p0=[PD_mean, 0.1])
chi2_av = np.sum(((PD - pd_av_model(phi,*popt))/PD_err)**2)
dchi2 = chi2_qed - chi2_av
print(f"chi2 AV dim-8 = {chi2_av:.2f}")
print(f"Delta chi2 = {dchi2:.2f}")
if dchi2 < 9:
    print("Resultado: LIMITE - M > few TeV (não detecção)")
else:
    print("Resultado: HINT de sinal")

# Prova 1 e 3
print("\n[PROVA 1 - JWST] e [PROVA 3 - LZ] -> ver docs/")
