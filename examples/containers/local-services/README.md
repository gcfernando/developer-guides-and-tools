---
title: "Local Development Services with Podman Compose"
description: "Configure an opt-in Podman Compose stack with 11 database, messaging, search and identity services. Review credentials, port bindings and resource needs."
permalink: /examples/local-services/
---

[Developer guides and tools](../../../README.md)

<a id="local-development-services"></a>

# Local Development Services with Podman Compose

Use [compose.yml](compose.yml) to explore local database, messaging, search and identity services with Podman Compose. Its 11 services are SQL Server, Elasticsearch, Kibana, Oracle XE, MongoDB, RabbitMQ, MySQL, Kafka, Kafka UI, Redis and Keycloak. Configure and start only the services you need for practice.

<a id="guide-configure"></a>

## Configure

Install Podman and a compatible Compose provider. Work in a separate local copy of this example. Create or review its `.env` file with values you choose for `SQL_PASSWORD`, `ORACLE_PASSWORD` and `DEFAULT_ROOT_PASSWORD`, and an optional `TZ`; use the requirements shown in `compose.yml`. The checkout currently tracks an `.env` file despite the ignore rule: do not commit personal credentials, and do not treat the tracked values as private. There is no supplied `.env.example`. Relative paths below assume the repository root of your practice copy.

Image tags are the imported snapshot. Check availability, architecture, licensing and resource requirements before pulling images. Starting every service can use substantial memory and disk.

~~~powershell
podman compose --env-file examples/containers/local-services/.env -f examples/containers/local-services/compose.yml config
podman compose --env-file examples/containers/local-services/.env -f examples/containers/local-services/compose.yml up -d mysql
podman compose --env-file examples/containers/local-services/.env -f examples/containers/local-services/compose.yml ps
podman compose --env-file examples/containers/local-services/.env -f examples/containers/local-services/compose.yml logs mysql
podman compose --env-file examples/containers/local-services/.env -f examples/containers/local-services/compose.yml down
~~~

The resolved config includes credentials; do not publish it. Published ports bind to loopback in this consolidated example. Elasticsearch security remains disabled for local development. Kibana depends on Elasticsearch startup order, without a health condition.

Nine named data volumes survive normal shutdown. Adding the volume-deletion option removes stored data. This merge did not start the services or verify the imported image tags.

[Docker reference](../../../docs/containers/docker-cheat-sheet.md) · [Podman reference](../../../docs/containers/podman-cheat-sheet.md)
