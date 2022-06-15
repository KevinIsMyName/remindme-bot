from dotenv import dotenv_values
import os


def get_env(fpath) -> dict:
    env_vars = dict(**dotenv_values(fpath))
    for key, value in env_vars.items():
        try:
            env_vars[key] = int(value)
        except:
            pass
    return env_vars

if __name__ == "__main__":
    from pprint import pprint
    pprint(get_env("./.env"), sort_dicts=True)