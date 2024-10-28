import yaml


class RecapGateway:

    @staticmethod
    def load(file_path: str) -> dict | None:
        with open(file_path) as f:
            try:
                return yaml.safe_load(f)
            except yaml.YAMLError as e:
                print(f'yaml error: {e}')
        return None
