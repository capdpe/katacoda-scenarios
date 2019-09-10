import os
os.system("if grep -q "db-user-pass" db-secret.yaml; then echo done; fi")
