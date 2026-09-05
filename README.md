# VACUO-ATIVO-3-PROVAS
### Três evidências convergentes de um vácuo ativo — JWST + Magnetar + LZ

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22307797.svg)](https://doi.org/10.5281/zenodo.22307797)

**Autor:** Gustavo Alves Condé — ORCID: 0009-0003-8264-7907  
**Zenodo:** 10.5281/zenodo.22307797  
**Status:** Ciclo metodológico fechado, comprovação aberta

## As 3 provas

| Prova | Dado | Resultado atual |
|-------|------|-----------------|
| 1. JWST | z>10 | Limite em lambda/M_Pl |
| 2. Magnetar 1E 1547.0-5408 | IXPE 140h - 15 bins (Stewart et al. Nature 2026) | PD=0.556, chi2=18.12/14, Delta=6.46 → LIMITE M > few TeV |
| 3. LZ | WIMP | Limite em xi |

**Critério:** Delta chi2 >9 para 3 sigma. Abaixo = limite, não detecção.

## Prova 2 - Detalhe

Dado real: data/rvm_params_1e1547_15bins.csv
Figura: figures/IXPE_PD_phase.png

Roda:
python likelihood/AV_likelihood_real_IXPE.py

## Sobre Z0 (texto corrigido)

We implement a vacuum-depletion potential whose scale can be motivated by Z0 ~376.73 ohm. With S_inst~280, V0 compatible with rho_Lambda ~1e-47 GeV4. This link is exploratory, not proof.

## Estrutura

- data/rvm_params_1e1547_15bins.csv
- likelihood/AV_likelihood.py (seu arquivo editado)
- figures/
- joss/
- docs/ Mhhs4GmNsxb(11).PDF, (12).PDF, (14).PDF
