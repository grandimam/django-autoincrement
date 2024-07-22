# Django AutoIncrementField

Django Autoincrement for non-primary key fields

## Create Sequences

To create sequences for `AutoIncrementField`, run:

```commandline
python manage.py create_sequences --sequence-names my_custom_sequence --start-values 100
```

## Multiple Sequences

To create multiple sequences for `AutoIncrementField`, run:

```commandline
python manage.py create_sequences --sequence-names seq1 seq2 --start-values 100 200
```

### Summary

- **`AutoIncrementField`**: Updated to accept and use a `start_value` argument.
- **Management Command**: Updated to accept start values for sequences and apply them during sequence creation.
- **Documentation**: Updated to provide instructions on how to use the new `start_value` feature.

This setup ensures that your auto-increment fields start from the specified value, allowing for more flexibility and control over sequence generation.

