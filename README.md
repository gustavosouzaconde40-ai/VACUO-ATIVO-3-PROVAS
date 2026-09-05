# VACUO-ATIVO-3-PROVAS
### Três evidências convergentes de um vácuo ativo — JWST + Magnetar + LZ

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22307797.svg)](https://doi.org/10.5281/zenodo.22307797)

**Autor:** Gustavo Alves Condé — ORCID: 0009-0003-8264-7907
**Zenodo:** 10.5281/zenodo.22307797
**Status:** Ciclo metodológico fechado, comprovação aberta

## As 3 provas

| Prova | Dado | Arquivo neste repo | Resultado atual |
|-------|------|-------------------|-----------------|
| 1. JWST | Excesso galáxias massivas z>10 | `docs/Mhhs4GmNsxb(11).PDF` | Limite em lambda/M_Pl |
| 2. Magnetar 1E 1547.0-5408 | IXPE 140h - 15 bins (Stewart et al. Nature 2026) | `data/rvm_params_1e1547_15bins.csv` | PD=0.556, chi2=18.12/14, Delta=6.46 → LIMITE M > few TeV |
| 3. LZ | WIMP search | `docs/Mhhs4GmNsxb(14).PDF` | Limite em xi |

**Critério de falsificabilidade:** Delta chi2 = chi2_QED - chi2_AV > 9 (~3 sigma). Abaixo disso = LIMITE, não detecção.

## Prova 2 - Detalhe

**Origem:** https://github.com/rae-stewart/Polarimetric-Analysis-of-1E-1547.0-5408
Arquivo original: `rvm_params_1e1547_15bins.csv` com `phase, q, q_err, u, u_err`

**Seu arquivo editado** `data/rvm_params_1e1547_15bins.csv` já tem:
`phase,q,q_err,u,u_err,PD,PD_err,PA,PA_err`

## Como rodar

```bash
python likelihood/AV_likelihood.py
## Theory - Z0 como unidade

Ver `theory/Z0_as_unit.md` e `theory/dimensional_analysis.py`

- Z0 = 376.73 Ohm definido como Z0=1 no sistema AV
- rho_Lambda = M_Pl^4 * exp(-S_inst(Z0)), S_inst~280 -> 1e-47 GeV4
- Previsão falsificável: Delta chi2 -> >9 com IXPE 500h se M = f(Z0)
