#!/usr/bin/env python3
"""
AV_likelihood_real_IXPE.py
Aeternvm Vacuvm - Magnetar 1E 1547.0-5408 likelihood with REAL IXPE data
Source: Stewart et al. (Nature 2026) GitHub
Falsifiability: Delta chi2 = chi2_QED - chi2_AV > 9 (~3 sigma)
Author: Gustavo Alves Conde - ORCID 0009-0003-8264-7907
Zenodo: 10.5281/zenodo.22307797
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Caminho corrigido para seu repo: data/rvm_params...
DATA_FILE = Path(__file__).parent.parent / "data" / "rvm_params_1e1547_15bins.csv"

def load_ixpe_data(path=DATA_FILE):
    df = pd.read_csv(path)
    df.columns = [c.strip().lower() for c in df.columns]
    if "pd" not in df.columns:
        df["pd"] = np.sqrt(df["q"]**2 + df["u"]**2)
        df["pd_err"] = np.sqrt((df["q"] * df["q_err"] / df["pd"])**2 + (df["u"] * df["u_err"] / df["pd"])**2)
        df["pa"] = 0.5 * np.arctan2(df["u"], df["q"]) * 180.0 / np.pi
    return df

def pd_qed_constant(phase, pd0):
    return np.full_like(phase, pd0, dtype=float)

def pd_av_model(phase, pd0, amp, phi0=0.0):
    return pd0 + amp * np.cos(2 * np.pi * (phase - phi0))

def chi2(pd_obs, pd_err, pd_model):
    return np.sum(((pd_obs - pd_model) / pd_err)**2)

def run_likelihood(df):
    phase = df["phase"].values
    pd_obs = df["pd"].values
    pd_err = df["pd_err"].values
    pd0_best = np.average(pd_obs, weights=1.0 / pd_err**2)
    chi2_qed = chi2(pd_obs, pd_err, pd_qed_constant(phase, pd0_best))
    amps = np.linspace(-0.25, 0.25, 201)
    chi2_av_list = []
    for a in amps:
        chi2_a = min(
            chi2(pd_obs, pd_err, pd_av_model(phase, pd0_best, a, 0.0)),
            chi2(pd_obs, pd_err, pd_av_model(phase, pd0_best, a, 0.25))
        )
        chi2_av_list.append(chi2_a)
    chi2_av = np.array(chi2_av_list)
    idx_best = np.argmin(chi2_av)
    return {
        "pd0_best": pd0_best,
        "chi2_qed": chi2_qed,
        "amp_best": amps[idx_best],
        "chi2_av_min": chi2_av[idx_best],
        "delta_chi2": chi2_qed - chi2_av[idx_best],
        "amps": amps,
        "chi2_av": chi2_av,
        "ndof": len(phase) - 1,
    }

def make_plots(df, results, outdir=Path(".")):
    outdir = Path(outdir)
    phase = df["phase"].values
    pd_obs = df["pd"].values
    pd_err = df["pd_err"].values
    q = df["q"].values
    u = df["u"].values
    fig, ax = plt.subplots(figsize=(8,5))
    ax.errorbar(phase, pd_obs, yerr=pd_err, fmt="o", color="k", label="IXPE data", capsize=3)
    ax.axhline(results["pd0_best"], color="C0", ls="--", label=f"QED constant {results['pd0_best']:.3f}")
    ax.plot(phase, pd_av_model(phase, results["pd0_best"], results["amp_best"]), color="C3", lw=2, label=f"AV best amp={results['amp_best']:.3f}")
    ax.set_xlabel("Pulse phase"); ax.set_ylabel("PD"); ax.set_ylim(0,1.2); ax.legend(); ax.grid(alpha=0.3)
    fig.savefig(outdir / "IXPE_PD_phase.png", dpi=180); plt.close(fig)

if __name__ == "__main__":
    df = load_ixpe_data()
    results = run_likelihood(df)
    print(f"Loaded {len(df)} bins")
    print(f"Weighted mean PD = {results['pd0_best']:.3f}")
    print(f"chi2_QED = {results['chi2_qed']:.2f}")
    print(f"chi2_AV min = {results['chi2_av_min']:.2f}")
    print(f"Delta chi2 = {results['delta_chi2']:.2f}")
    if results["delta_chi2"] > 9:
        print(">>> possible evidence")
    else:
        print(">>> consistent with pure QED - LIMIT")
