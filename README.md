# Prueba de código Divain

---

## Requisitos

- Tener instalado **Docker** y **Docker Compose**.
- Tener instalado **Make** (opcional, pero recomendado para facilitar comandos).

---

## Cómo iniciar el proyecto

### Con Make (recomendado)

Primero, ejecuta:

```bash
make init
```

Este comando hace:

- Build de las imágenes Docker (sin usar cache).
- Levanta los contenedores de la API y la base de datos.
- Inicializa la base de datos creando las tablas y poblando datos de prueba.

Luego, para tener los contenedores corriendo:

```bash
make up

```

Cuando termines, para detener los contenedores:

```bash
make down
```

---

### Comandos disponibles

| Comando            | Descripción                                        |
| ------------------ | -------------------------------------------------- |
| `make help`        | Muestra la lista de comandos disponibles           |
| `make start`       | Construye las imágenes Docker sin cache            |
| `make up`          | Levanta los contenedores en segundo plano          |
| `make down`        | Detiene los contenedores                           |
| `make setup_db`    | Crea las tablas en la base de datos                |
| `make populate_db` | Inserta datos de prueba en la base de datos        |
| `make setup`       | Ejecuta `setup_db` y `populate_db`                 |
| `make init`        | Ejecuta `start`, `up` y `setup` para preparar todo |

---

### Si no tienes Make

Puedes ejecutar los comandos equivalentes con Docker Compose directamente:

```bash
# Construir imagen sin cache
docker compose build --no-cache

# Levantar contenedores en segundo plano
docker compose up -d

# Crear tablas en la base de datos
docker compose exec -T api python -m app.db.setup

# Poblar la base de datos con datos de prueba
docker compose exec -T api python -m app.db.populate_db
```

---

## Puertos usados

- API: [http://localhost:8080](http://localhost:8080)
- Frontend: [http://localhost:5174](http://localhost:5174)
