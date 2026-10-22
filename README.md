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

Présentation de l’architecture et emplacements des composants ; implémentation privée non incluse.

## 🚀 Lancer

Cette vitrine ne fournit pas d’application exécutable ni de procédure d’installation : parcourir les dossiers et la documentation d’architecture.
