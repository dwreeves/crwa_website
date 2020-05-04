import yaml

from crwa_flagging_site.config import KEYS_FILE


def load_keys() -> dict:
    with open(KEYS_FILE, 'r') as f:
        d = yaml.load(f, Loader=yaml.BaseLoader)
    return d


class HTTPException(Exception):  # TODO: put this in a better spot?
    pass

