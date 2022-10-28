from typing import List
from kubiya import ActionStore

ENVIRONMENTS = {
    "prod": "prod.example.com",
    "staging": "staging.example.com",
    "dev": "dev.example.com",
    "local": "localhost:8000",
}

def get_all_envs() -> List[str]:
    return list(ENVIRONMENTS.keys())

def get_host_for_env(env: str) -> str:
    host = ENVIRONMENTS.get(env)
    if host:
        return host
    raise ValueError(f"Invalid environment: {env}")

actionstore = ActionStore("env getter", "0.0.1")
actionstore.register_action("get_all_envs", get_all_envs)
actionstore.register_action("get_host_for_env", get_host_for_env)