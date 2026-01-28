# ⌨️ KeyL - Advanced Educational Keylogger

**KeyL** es una herramienta de auditoría desarrollada en Python para la exploración de conceptos avanzados de seguridad informática, específicamente en las áreas de **multithreading**, **sincronización de procesos** y **criptografía simétrica**.

---

## ⚠️ ADVERTENCIA LEGAL
> **IMPORTANTE:** Este software ha sido creado exclusivamente con fines educativos y de investigación ética. El uso de esta herramienta para monitorizar dispositivos sin el consentimiento explícito del propietario es **ilegal**. El desarrollador no se hace responsable del mal uso de este programa.

---

## 🚀 Características Técnicas

* **Arquitectura Multihilo (Asíncrona):** Utiliza `threading.Timer` para realizar volcados de datos al disco sin interrumpir la captura de eventos en tiempo real.
* **Cifrado Robusto (AES-128):** Implementa el estándar Fernet de la librería `cryptography`. Los datos nunca se almacenan en texto plano en el disco.
* **Gestión de Buffer con Locks:** Implementación de `threading.Lock()` para prevenir **Race Conditions** entre el hilo de escucha y el hilo de escritura.
* **Tratamiento de Datos:**
    * Mapeo completo de teclado numérico (Numpad).
    * Detección de combinaciones con la tecla `CTRL`.
    * Limpieza de buffer mediante `backspace` antes del ciclo de guardado.



---
