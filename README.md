# MVTS Edge Simulator 

## Requisitos

* Docker Desktop
* Python
* VS Code

## Pasos para ejecutar

### 1. Levantar RabbitMQ

```bash
docker-compose up -d
```

Abrir en navegador:
http://localhost:15672
Usuario: guest
Contraseña: guest

### 2. Instalar dependencias

```bash
pip install pika
```

### 3. Ejecutar simulador

```bash
python simulador_camion.py
```

## Descripción

Este simulador genera coordenadas GPS simuladas de un camión minero y las envía a RabbitMQ cada 3 segundos usando el contrato JSON definido por el equipo.


