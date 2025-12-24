import json
from utils.logger import log_info
from utils.paths import project_path

class PermissionEngine:
    def __init__(self, default_policy_path, user_policy_path):
        self.policy = {}
        self.load_policies(default_policy_path, user_policy_path)

    def load_policies(self, default_path, user_path):
        default_path = project_path(default_path)
        user_path = project_path(user_path)

        with open(default_path, "r") as f:
            default_policy = json.load(f)

        try:
            with open(user_path, "r") as f:
                user_policy = json.load(f)
        except FileNotFoundError:
            user_policy = {}

        self.policy = default_policy
        self.policy.update(user_policy)

        log_info("Permission policies loaded")

    def check(self, action: str) -> str:
        decision = self.policy.get("actions", {}).get(action, "deny")
        log_info(f"Permission check: action={action}, decision={decision}")
        return decision
