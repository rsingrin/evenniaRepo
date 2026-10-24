# CLAUDE.md

## Layout

- `starterGame/` — **the game being developed.** All edits go here.
  - `typeclasses/` — custom typeclasses (characters, rooms, objects, `customObjects.py`, …)
  - `commands/` — custom commands (`mycommands.py`) and cmdsets (`default_cmdsets.py`)
  - `world/` — prototypes, help entries
  - `server/conf/` — game settings (`settings.py`)
- `evennia/` — Evennia framework source (v6.0.0, installed editable into `evenv`). **Reference only — do not edit.** Read it to check base classes, hooks, and default behavior (e.g. `evennia/evennia/objects/objects.py`, `evennia/evennia/commands/default/`). It is gitignored.
- `evenv/` — Python virtualenv. Ignore it; don't search in it.

## Running

Activate the venv first: `source evenv/bin/activate`, then from `starterGame/`:

- `evennia start` / `evennia stop` / `evennia reload` (reload picks up code changes)
- `evennia migrate` after model/setting changes
- `evennia test --settings settings.py .` to run the game's tests

## Notes

- Don't commit `server/evennia.db3`, logs, or pid files.
