def calcular_costo_total(costo_usd, tipo_cambio, gastos_fijos, impuestos_pct):
    costo_ars = costo_usd * tipo_cambio
    impuestos = costo_ars * (impuestos_pct / 100)
    total = costo_ars + impuestos + gastos_fijos
    return {
        "costo_ars": round(costo_ars, 2),
        "impuestos": round(impuestos, 2),
        "total": round(total, 2)
    }
