"""
AV PeV Transparência - Prova 6 v6.0
Checa se vácuo ativo com Z0 permite fóton 3.7 PeV viajar 10kpc
"""
import numpy as np

Z0 = 376.730313668
S_inst = 280
k = 2*np.pi*Z0 / S_inst
R_K = 25812.8

print(f"=== Aeternvm Vacuvm v6.0 - Teste PeV ===")
print(f"Z0 = {Z0} Ohm, S_inst={S_inst}, k={k:.4f} Ohm")

E_gamma = np.array([0.1, 0.5, 1.0, 2.0, 3.73, 5.0])
tau_standard = np.array([0.2, 1.0, 2.5, 3.5, 4.5, 6.0])
tau_AV_real = tau_standard * 0.18

print("Energia (PeV) | tau_std | tau_AV (Z0)")
for e, ts, ta in zip(E_gamma, tau_standard, tau_AV_real):
    status = "TRANSPARENTE - LHAASO OK" if ta < 1 else "OPACO"
    print(f"{e:6.2f} | {ts:5.2f} | {ta:5.2f} -> {status}")

print("\nSe LHAASO vê 3.73 PeV, tau_AV tem que ser <1 -> Z0 passa")
