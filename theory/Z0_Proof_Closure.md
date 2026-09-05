# Fechamento da prova Z0 como Unidade de Lambda

## Status atual (08:59 - seu print)
- PD = 0.556, chi2_QED = 18.12 /14 =1.29, Delta =6.46
- Resultado: LIMITE M > few TeV (consistente com QED puro)
- Isso NÃO refuta Z0, só coloca limite

## O que falta para PROVAR Z0 (falsificável)

### 1. Derivar k = 8.44 de primeira princípios
S_inst = 2*pi*Z0 / k
k = 2*pi*376.73 / 280 = 8.44 Ohm

Provar que k = 8.44 vem de topologia U(1) do vácuo:
- Fluxo quantizado: phi0 = h / (2e) = 2.07e-15 Wb
- Z0 = phi0 * (algo) / e ?

Se provar k, então:
rho_Lambda = M_Pl^4 * exp(-2*pi*Z0/k)  sem ajuste fino

### 2. Conectar as 3 provas com mesmo Z0

- JWST (Prova 1): lambda/M_Pl ~ (Z0/Z_Pl)^n * exp(-S/4)
- Magnetar (Prova 2): M ~ 3 TeV * (Z0/376.73) → amp=0.14
- LZ (Prova 3): xi ~ (Z0 factor)

Se mesmo Z0 explica 3 limites independentes, é unidade.

### 3. Previsão que fecha ou falsifica

IXPE 500h:
- Se Z0-unit verdadeiro: Delta chi2 = 6.46 * (500/140) = 23.0 >9 → DISCOVERY
- Se Z0-unit falso: Delta fica <9 mesmo com 500h → REFUTADO

Isso está em AV_Z0_Probe_sensitivity.py e gera theory_Z0_sensitivity.png

## Conclusão para Zenodo 22307797 v4.0

Z0 NÃO é prova de Lambda hoje, é HIPÓTESE falsificável com unidade definida.
O repo v4.0 Z0-UNIT contém todos os arquivos para falsificar.

Para v5.0 PROOF, falta derivar k=8.44.
