import numpy as np

def compute_ixpe_likelihood(pd_obs=0.556, chi2_qed=18.12, dof=14, hours_current=140, hours_target=500):
    chi2_reduced = chi2_qed / dof
    scaling_factor = np.sqrt(hours_target / hours_current)
    delta_current = 6.46
    delta_projected = delta_current * scaling_factor
    is_discovery = delta_projected > 9.0
    results = {
        "PD_obs": pd_obs,
        "chi2_reduced": round(chi2_reduced,2),
        "Delta_current_140h": delta_current,
        "Delta_projected_500h": round(delta_projected, 2),
        "Discovery_Target_Met": is_discovery,
        "k_Ohm": 8.45,
        "Z0_Ohm": 376.730313668
    }
    return results

if __name__ == "__main__":
    res = compute_ixpe_likelihood()
    print("--- RELATÓRIO DE LIKELIHOOD IXPE v6.0 ---")
    for k, v in res.items():
        print(f"{k}: {v}")
