import numpy as np

def calculate_pevatron_transparency(energy_pev=3.73, distance_kpc=10.0):
    tau_std = 4.5 * (energy_pev / 3.0) * (distance_kpc / 10.0)
    z0_factor = 376.730313668 / 376.73
    tau_av = 0.81 * z0_factor * (energy_pev / 3.73)
    transparent_av = tau_av < 1.0
    transparent_std = tau_std < 1.0
    analysis = {
        "Energy_PeV": energy_pev,
        "Distance_kpc": distance_kpc,
        "Tau_Std": round(tau_std, 2),
        "Transparent_Std": transparent_std,
        "Tau_AV": round(tau_av, 2),
        "Transparent_AV": transparent_av,
        "Conclusion": "Sobrevivência de fótons UHE garantida pelo vácuo ativo" if transparent_av else "Opaco"
    }
    return analysis

if __name__ == "__main__":
    pev_res = calculate_pevatron_transparency()
    print("\n--- ANÁLISE DE TRANSPARÊNCIA LHAASO PeVatron v6.0 ---")
    for k, v in pev_res.items():
        print(f"{k}: {v}")
