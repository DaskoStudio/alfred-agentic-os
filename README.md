# ALFRED — Agentic OS (copie publique / architecture)

> ℹ️ **Dépôt vitrine.** Ceci est une **copie publique épurée** d'un projet personnel : elle présente l'**architecture** et les choix techniques, **sans code sensible, secrets ni modules privés**. Le cœur applicatif reste privé.

**ALFRED** est un *agentic OS* : un assistant autonome multi-plateforme capable d'orchestrer des tâches via un registre d'outils **MCP (Model Context Protocol)**, avec des clients bureau et mobile connectés à un backend.

## 🗺️ Vue d'ensemble

```
┌────────────┐     ┌────────────┐
│  Desktop   │     │   Mobile   │
│ Tauri+React│     │   (app)    │
└─────┬──────┘     └─────┬──────┘
      │                  │
      └────────┬─────────┘
               ▼
        ┌─────────────┐      ┌──────────────┐
        │   Backend   │◄────►│ Registre MCP │
        │  (FastAPI)  │      │  + Outils    │
        └──────┬──────┘      └──────────────┘
               ▼
        ┌─────────────┐
        │  Orchestr.  │  agents / tâches / mémoire
        └─────────────┘
```

## 🧱 Structure

```
app/
  core/      # noyau backend, registre MCP, orchestration
  agents/    # agents et coordination
  skills/    # outils / compétences natifs
  api/       # routes REST + WebSocket
bridge/      # pont entre clients et backend
desktop/     # app bureau (Tauri Rust + React)
mobile/      # app mobile
scripts/     # utilitaires
docs/        # documentation & schémas
tests/
```

## 🧩 Concepts clés

- **Registre MCP** : découverte et appel d'outils standardisés par les agents
- **Orchestration multi-agents** : décomposition et exécution de tâches
- **Multi-plateforme** : bureau (local) + mobile (backend distant)
- **Sécurité** : secrets et exécution côté serveur ; les clients n'exposent que l'UI

## 🛠️ Stack

Python · FastAPI · MCP · Tauri (Rust) · React · WebSocket

## 👤 Auteur

Konaté Adama (**[@DaskoStudio](https://github.com/DaskoStudio)**) — Ynov Campus

---

*Les dossiers de ce dépôt décrivent l'organisation du projet ; le code d'implémentation n'est pas inclus dans cette version publique.*

## ✨ Fonctionnalités

- API FastAPI : `GET /health` retourne `{"status":"ok"}`.
- Routes `GET /api/tools`, `POST /api/tools/{name}/call` et `POST /api/agents/run` : HTTP 501 `not implemented`.
- Contrats `ToolRegistry` et `Agent.run()` : stubs uniquement.
- Manifestes Tauri/React pour desktop et mobile ; aucun client exécutable fourni.

Les concepts présentés plus haut décrivent l’architecture cible privée. Aucun serveur MCP, outil réel, orchestration, WebSocket ni client fonctionnel n’est implémenté ici.

## 🚀 Lancer

Prérequis : Python 3.11+.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1
```

Vérifier : `curl http://127.0.0.1:8000/health`. Documentation API : `http://127.0.0.1:8000/docs`.
Aucun secret ni service externe requis. Les routes métier répondent volontairement 501.

Les fichiers `desktop/package.json` et `mobile/package.json` déclarent uniquement des dépendances ; ils ne fournissent pas de commande de lancement.
