# Prueba de código Divain

Este proyecto es una prueba de código para Divain, cuyo objetivo es integrar una **API** con una base de datos **PostgreSQL** y consumir los datos desde un **frontend**.

## API

La API está desarrollada con **FastAPI** y expone los siguientes endpoints:

- `GET /products`: Lista todos los productos con **SKU**, **EAN13** y **stock**.
- `PATCH /products/{id}`: Actualiza un producto, utilizado principalmente para modificar el **stock**.
- `GET /stock`: Lista los movimientos de **stock** realizados.

El objetivo principal era crear una base de datos en **PostgreSQL**, desarrollar la **API** para proveer datos al frontend y permitir la actualización de los productos.

## Frontend

El frontend está construido con **React**. Contiene dos páginas principales:

- `/`: Lista los productos con **SKU**, **EAN13** y **stock**, y permite modificar la cantidad en stock.
- `/stock`: Muestra un historial de los movimientos de stock.

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
| `make test-api`    | Ejecuta los tests de la API                        |

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

## Tests

Para ejecutar los tests de la API, ejecuta el siguiente comando:

```bash
make test_api
```

En caso de no usar Make:

```bash
docker compose exec -it api sh -c "ENV=TEST python -m pytest"
```

## URLs de la Aplicación

- Frontend: [http://localhost:5174](http://localhost:5174)
- API: [http://localhost:8080](http://localhost:8080)
