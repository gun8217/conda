from utils import *

scores = func_input()
print(f"{scores = }")

passY, passN = func_pass_yes_no(scores, threshold=80)
print(f"{passY = }\n{passN = }")