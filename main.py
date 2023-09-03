#!/usr/bin/env python

import jwt
import sys
import datetime

class jwt_bot_token_generator:

    def __init__(self) -> None:
        self.secret_key = ""
        self.adm_id_bot = 0
        self.allowed_pc = ""
        self.exp_date = datetime.datetime.strptime("01/01/1900", r"%d/%m/%Y")
        self.interate_arguments()
        self.validate_arguments()
        print(self.generate_token())

    def interate_arguments(self) -> None:
        interator = 1
        argc = len(sys.argv)

        while(interator < argc):
            arg = sys.argv[interator]
            if (arg == None):
                raise Exception(f"The {arg} argument is missing!")
            elif (arg.startswith("--secret")):
                self.secret_key = arg.split("=")[1]
            elif (arg.startswith("--adm-id")):
                self.adm_id_bot = arg.split("=")[1]
            elif (arg.startswith("--pc-host")):
                self.allowed_pc = arg.split("=")[1]
            elif (arg.startswith("--exp-days")):
                days = arg.split("=")[1]
                self.exp_date = datetime.datetime.now() + datetime.timedelta(days=int(days))
            else:
                raise Exception(f"The argument {arg} is invalid!")
            interator = interator + 1

    def validate_arguments(self):
        missing_arguments = []

        if not self.secret_key:
            missing_arguments.append("secret_key")
        if not self.adm_id_bot:
            missing_arguments.append("adm-id")
        if not self.allowed_pc:
            missing_arguments.append("pc-host")
        if (self.exp_date < datetime.datetime.now()):
            missing_arguments.append("exp-days")

        if (len(missing_arguments) > 0):
            missing_arguments_string = ", ".join(str(miss) for miss in missing_arguments)
            raise Exception(f"The following argument(s) are not optional and have not been entered: {missing_arguments_string}.")
        else:
            consolidated_arguments_string = f"{{secret_key: {self.secret_key}, adm-id: {self.adm_id_bot}, allowed_pc: {self.allowed_pc}, exp_date: {self.exp_date}}}"
            print(f" {consolidated_arguments_string}.")

    def generate_token(self) -> str:
        claims = {
            'adm_id_bot': self.adm_id_bot,
            'allowed_pc': self.allowed_pc,
            'exp': self.exp_date
        }

        return jwt.encode(claims, self.secret_key, algorithm='HS256')

if __name__ == '__main__': jwt_bot_token_generator()