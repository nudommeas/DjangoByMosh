\\ ------------------------------------ ------------------------------------ \\ 

**Extending the User Model**
- Adding fields or extra data
- The best approach depends on whether you need new database columns or just new methods
- For new Fields, inheriting `AbstractUser` and setting `AUTH_USER_MODEl` is often the best for new project.

1. `How:` Create a new model (e.g., User) that inherits `from django.contrib.auth.models import AbstractUser`, add your fields, and set `AUTH_USER_MODEL` = 'your_app.CustomUser' in `settings.py`.

2. `When to Use:` You're starting fresh and need custom fields (like date_of_birth, phone_number) directly in the user table.

3. `Pros:` Full control over the user model, fields are in one table.