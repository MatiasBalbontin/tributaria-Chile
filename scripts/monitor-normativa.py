#!/usr/bin/env python3
"""
NORMA-CHILE Monitoring Script
Detecta cambios en normativa tributaria y genera commits automáticos

Ejecución: python monitor-normativa.py
Scheduled: Cowork tarea recurrente (Lunes 9 AM)
"""

import os
import json
import yaml
import subprocess
from datetime import datetime
from pathlib import Path
import hashlib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
CONFIG_FILE = SCRIPT_DIR / "config.yaml"

class NormativaMonitor:
    def __init__(self):
        self.repo_root = REPO_ROOT
        self.config = self._cargar_config()
        self.cambios_detectados = []
        self.commit_code = self._generar_codigo_commit()

    def _cargar_config(self):
        """Carga configuración desde YAML"""
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def _generar_codigo_commit(self):
        """Genera código de commit secuencial (001, 002, 003...)"""
        changelog = self.repo_root / "monitoring" / "changelog-commits.log"
        if changelog.exists():
            with open(changelog, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                if lines:
                    # Extraer último código
                    ultima_linea = lines[-1]
                    if "Commit #" in ultima_linea:
                        numero = int(ultima_linea.split("Commit #")[1].split()[0])
                        return str(numero + 1).zfill(3)
        return "001"

    def ejecutar_ciclo(self):
        """Ejecuta ciclo completo de monitoreo"""
        print(f"[{datetime.now()}] Iniciando monitoreo de normativa...")

        # 1. Revisar fuentes (simulado por ahora)
        self._revisar_fuentes()

        # 2. Detectar cambios
        self._detectar_cambios()

        # 3. Actualizar documentos
        if self.cambios_detectados:
            self._actualizar_documentos()

            # 4. Generar commit
            self._generar_commit()

            # 5. Enviar notificación
            self._enviar_notificacion()

            print(f"✓ Ciclo completado. Commit #{self.commit_code} generado.")
        else:
            print("ℹ No se detectaron cambios.")

    def _revisar_fuentes(self):
        """Revisa fuentes oficiales (SII, BCN, Leyes.cl)"""
        print("Revisando fuentes...")
        # Aquí iría scraping real de SII/BCN
        # Por ahora, simulado
        pass

    def _detectar_cambios(self):
        """Detecta cambios en normativa"""
        print("Detectando cambios...")

        # Buscar nuevos archivos en _sources
        sources_dir = self.repo_root / "_sources"
        if sources_dir.exists():
            for pdf_file in sources_dir.rglob("*.pdf"):
                # Crear hash para detectar cambios
                file_hash = self._hash_archivo(pdf_file)

                # Aquí iría lógica de comparación con versión anterior
                # Simulado: registrar como potencial cambio
                self.cambios_detectados.append({
                    "tipo": "nueva_normativa",
                    "archivo": str(pdf_file.relative_to(self.repo_root)),
                    "fecha": datetime.now().isoformat()
                })

    def _hash_archivo(self, archivo):
        """Calcula hash SHA256 de un archivo"""
        sha256_hash = hashlib.sha256()
        with open(archivo, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def _actualizar_documentos(self):
        """Actualiza documentos en normativa/"""
        print(f"Actualizando {len(self.cambios_detectados)} documento(s)...")

        # Actualizar monitoring/vigencias-AAAA.md
        año_actual = datetime.now().year
        monitoring_file = self.repo_root / "monitoring" / f"vigencias-{año_actual}.md"

        contenido = f"""# Vigencias {año_actual}

**Fecha de revisión:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Commit Code:** #{self.commit_code}

## Cambios Detectados

"""

        for cambio in self.cambios_detectados:
            contenido += f"- {cambio['tipo']}: {cambio['archivo']}\n"

        with open(monitoring_file, 'a', encoding='utf-8') as f:
            f.write(contenido)

        # Actualizar metadata-completo.json
        metadata_file = self.repo_root / "index" / "metadata-completo.json"
        with open(metadata_file, 'r', encoding='utf-8') as f:
            metadata = json.load(f)

        metadata["fecha_generacion"] = datetime.now().isoformat()
        metadata["total_documentos"] = len(metadata.get("documentos", []))

        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)

    def _generar_commit(self):
        """Genera commit automático con cambios"""
        os.chdir(self.repo_root)

        # Stage changes
        subprocess.run(["git", "add", "monitoring/", "index/", "normativa/"], check=False)

        # Crear mensaje de commit
        mensaje = f"""monitoring: Cambios detectados - Commit #{self.commit_code}

{len(self.cambios_detectados)} cambio(s) encontrado(s):
"""

        for cambio in self.cambios_detectados:
            mensaje += f"- {cambio['tipo']}: {cambio['archivo']}\n"

        mensaje += f"\nFecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

        # Ejecutar commit
        subprocess.run(["git", "commit", "-m", mensaje], check=False)

        # Log en changelog
        changelog = self.repo_root / "monitoring" / "changelog-commits.log"
        with open(changelog, 'a', encoding='utf-8') as f:
            f.write(f"[{datetime.now()}] Commit #{self.commit_code} - {len(self.cambios_detectados)} cambio(s)\n")

    def _enviar_notificacion(self):
        """Envía email con resumen de cambios"""
        print("Enviando notificación por email...")

        destinatario = self.config['output']['email_destinatario']
        asunto = self.config['output']['email_asunto'].format(commit_code=self.commit_code)

        # Construir cuerpo del email
        cuerpo = f"""
NORMA-CHILE | Monitoreo de Normativa Tributaria
================================================

Cambios Detectados: {len(self.cambios_detectados)}
Commit Code: #{self.commit_code}
Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

DETALLES DE CAMBIOS
-------------------
"""

        for cambio in self.cambios_detectados:
            cuerpo += f"\n• {cambio['tipo']}\n  Archivo: {cambio['archivo']}\n"

        cuerpo += f"""

PRÓXIMA ACCIÓN
--------------
Revisa los cambios arriba. Si todo está correcto, solicita en Claude:

  "push commit {self.commit_code}"

El sistema ejecutará automáticamente: git push origin main

---
NORMA-CHILE Monitoring System
Última ejecución: {datetime.now().isoformat()}
"""

        print(f"Email listo para {destinatario}")
        print(f"Asunto: {asunto}")
        print(f"Cambios: {len(self.cambios_detectados)}")

        # Nota: Email real se configuraría con credenciales SMTP
        # Por ahora solo logged localmente

    def _generar_reporte_local(self):
        """Genera archivo de reporte local"""
        reporte = self.repo_root / "monitoring" / f"reporte-{self.commit_code}.txt"

        contenido = f"""
REPORTE DE MONITOREO
====================
Commit: #{self.commit_code}
Fecha: {datetime.now().isoformat()}

CAMBIOS DETECTADOS: {len(self.cambios_detectados)}

"""

        for cambio in self.cambios_detectados:
            contenido += f"- {cambio}\n"

        with open(reporte, 'w', encoding='utf-8') as f:
            f.write(contenido)


def main():
    monitor = NormativaMonitor()
    monitor.ejecutar_ciclo()


if __name__ == "__main__":
    main()
