# Reflex Demo Web App
This is a reflex demo app using uv as package manager.

## Rerequirement
[uv](https://docs.astral.sh/uv/) installed.

## Getting Started
1. Clone and download this repository.
2. Go into app folder.
   ```bash
   cd reflex-demo-app
   ```
3. Install all required dependencies listed in the pyproject.toml or uv.lock file.
   ```bash
   uv sync --all-extras
   ```
4. Run the Development Server.
   ```bash
   uv run reflex run
   ```
   
## Project Type
[Reflex](https://reflex.dev/) Demo Project managed by [uv (package and project manager)](https://docs.astral.sh/uv/).