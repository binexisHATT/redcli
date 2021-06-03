"""
File: iam.py
Description: contains revelant AWS IAM functions and actions
"""

class Iam():

    def __init__(self, session, console) -> None:
        self.iam = session.client("iam")
        self.console = console

  # [START get_policies]
    def get_policies(self) -> list:
        policy_name = []
        policy_arns = []
        for user_perm in self.iam.get_account_authorization_details(Filter=["User"])["UserDetailList"]:
            for policy in user_perm["AttachedManagedPolicies"]:
                policy_name.append(policy["PolicyName"])
                policy_arns.append(policy["PolicyArn"])
        return list(zip(policy_name, policy_arns))
  # [END get_policies]
    