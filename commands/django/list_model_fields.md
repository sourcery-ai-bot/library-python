# List All Model Fields

Opening up the iPython shell with all the model fields loaded.

```sh
docker-compose exec web python manage.py shell_plus --ipython
```

Enter the below command will give a nice list of individual field names.

```python
{my_model}_fields = [field.name for field in {MyModel}._meta.get_fields()]
```
