---
title: "Local Development Services with Podman Compose"
description: "Configure an opt-in Podman Compose stack with 11 database, messaging, search and identity services. Review credentials, port bindings and resource needs."
permalink: /examples/local-services/
---

[Developer guides and tools](../../../README.md)

<a id="local-development-services"></a>

# Local Development Services with Podman Compose

[compose.yml](compose.yml) contains 11 services: SQL Server, Elasticsearch, Kibana, Oracle XE, MongoDB, RabbitMQ, MySQL, Kafka, Kafka UI, Redis and Keycloak. It is an example environment, not a production deployment.

> **In this guide:** [Get started](#guide-configure)

<a id="guide-configure"></a>

## Configure

Install Podman and a compatible Compose provider. Copy [.env.example](.env.example) to .env in this folder and replace the example values. The .env file is ignored by Git. Relative paths below assume the repository root.

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
